# Fixtures en tant qu'argument de fonctions
import pytest  # nécessaire lorsque des fixtures sont utilisées


# Exemples basiques
# Exemple 1


def get(data, index, default=None):
    try:
        return data[index]
    except IndexError:
        return default


@pytest.fixture
def simple_comme_bonjour():
    return ('pomme', 'bannane')


def test_get(simple_comme_bonjour):
    # plus besoin de définir les données du test!!
    element = get(simple_comme_bonjour, 0)
    assert element == 'pomme'
    assert 0


def test_element_manquant(simple_comme_bonjour):
    # plus besoin de définir les données du test!!
    element = get(simple_comme_bonjour, 1000, 'Je laisse la main')
    assert element == 'Je laisse la main'
    assert 0


# Exemple 2

@pytest.fixture
def smtp_connection():
    import smtplib
    return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)


def test_ehlo(smtp_connection):
    response, msg = smtp_connection.ehlo()  # on se connecte au serveur, ehlo() récupère un message de bienvenue et un code de retour
    print(msg)
    assert response == 250  # code réponse retourné par le serveur mail
    assert 0  # pour la démo


# Exemple trois, bien choisir la portée des fixtures
import smtplib


@pytest.fixture(scope="module") # scopes available: "class", "module", "package" or "session"
def smtp_connection():
    return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)


def test_ehlo(smtp_connection):
    response, msg = smtp_connection.ehlo()
    assert response == 250
    assert b"smtp.gmail.com" in msg
    assert 0  # for demo purposes


def test_noop(smtp_connection):
    response, msg = smtp_connection.noop()
    assert response == 250
    assert 0  # for demo purposes


# Exemple: fixture tmp_path: permet de créer un dossier temporaire
# rmq: par défaut, seul les trois plus récents dossiers temporaires sont conservés sur le disque dur:
# https://docs.pytest.org/en/stable/tmpdir.html#base-temporary-directory

CONTENT = "contenue de démonstration"


def test_create_file(tmp_path):
    d = tmp_path / "sub_dir"
    d.mkdir()
    p = d / "hello.txt"
    print("voici le chemin du fichier \n", p) # Pour être explicite
    p.write_text(CONTENT)
    assert p.read_text() == CONTENT # le contenue de tmp_path/sub_dir/hello.txt est bien CONTENT
    assert len(list(tmp_path.iterdir())) == 1 # Un seul dossier à été créé!!
    assert 0


# Exemple capsys (permet de capturer les sorties standards et d'erreurs)

import sys

def bonjour(to_out, to_err=None):
    print(to_out)
    if to_err:
        print(to_err, file=sys.stderr)


def test_myoutput(capsys):
    bonjour("Message de démo", "Message d'erreur")
    out, err = capsys.readouterr() # Méthode de capture des sorties standards/d'erreurs
    assert out == "Message de démo\n"
    assert err == "Message d'erreur\n"

    bonjour("Deuxieme message de démo")
    out, err = capsys.readouterr()
    assert out == "Deuxieme message de démo\n"
    assert err == ""
    assert 0
