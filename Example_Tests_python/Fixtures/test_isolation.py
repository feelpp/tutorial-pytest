
import pytest
import smtplib

# # Exemple 1

def get(data, index, default=None):
    try:
        return data[index]
    except IndexError:
        return default


# On passe de pytest.fixture() à pytest.yield_fixture()
# @pytest.fixture()
# def simple_comme_bonjour():
#     # Executer avant le test, permet de mettre en place l'environnement de test
#     print('Avant !')

#     # Expression générateur, retourne la fixture
#     yield ('pomme', 'banane')

#     # Executer après le test, permet de nettoyer les données du test
#     print('Apres !')

# def test_get(simple_comme_bonjour):
#     element = get(simple_comme_bonjour, 0)
#     assert element == 'pomme'

# def test_element_manquant(simple_comme_bonjour):
#     element = get(simple_comme_bonjour, 1000, 'Je laisse la main')
#     assert element == 'Je laisse la main'

# def test_avec_echec(simple_comme_bonjour):
#     element = get(simple_comme_bonjour, 1000, 'Je laisse la main')
#     assert element == 'Je tres clair, Luc'


# Example 2

@pytest.fixture(scope="module")
def smtp_connection():
    smtp_connection = smtplib.SMTP("smtp.gmail.com", 587, timeout=5)
    yield smtp_connection  # provide the fixture value
    print("teardown smtp")
    smtp_connection.close()


def test_ehlo(smtp_connection):
    response, msg = smtp_connection.ehlo()
    assert response == 250
    #assert b"smtp.gmail.com" in msg
    assert b"smtp.gmail.com" in msg
    assert 0  # for demo purposes


def test_noop(smtp_connection):
    response, msg = smtp_connection.noop()
    assert response == 250
    assert 0  # for demo purposes

