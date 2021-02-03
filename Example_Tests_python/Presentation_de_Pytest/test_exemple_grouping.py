# content of test_class.py
from mon_module.module_demo import inc, div
import pytest


class TestInc:
    a = 0
    b = 7

    def test_zero(self):
        assert inc(self.a) == 1

    def test_sept(self):
        assert inc(self.b) == 8


class TestDiv:
    a = 0
    b = 1
    c = 4
    d = 10

    def test_div_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            div(self.b, self.a)

    def test_div_ok(self):
        assert div(self.d, self.c) == 2.5

    @pytest.mark.xfail # marque le test comme échouant obligatoirement
    def test_div_not_ok(self):
        assert div(self.d, self.c) == 3.5

# Remarques:
# @mon_decorateur
# def ma_fonction():
#     pass
# sucre syntaxique pour:
# ma_fonction = mon_decorateur(ma_fonction)


# Il est aussi possible de regrouper les tests avec @pytest.mark.monmarkeur
# On peut sélectionner les tests avec pytest -v -m testsinc test_exemple_class.py
# Ou au contraire les exclure avec pytest -v -m "not testsinc" test_exemple_class.py

@pytest.mark.testsinc
def test_8():
    a = 8
    assert inc(a) == 9

@pytest.mark.testsinc
def test_sept():
    b = 9
    assert inc(b) == 10

# Note: on peut aussi marquer une classe, auquel cas tous les tests de la classe sont executés

# Pour éviter les warning il faudrait enregistrer les markers dans pytests.ini:
# Voir: https://stackoverflow.com/questions/60806473/pytestunknownmarkwarning-unknown-pytest-mark-xxx-is-this-a-typo
