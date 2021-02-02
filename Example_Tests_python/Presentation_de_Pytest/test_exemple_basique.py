from mon_module.module_demo import inc, div


# def test_failed():
#     assert inc(3) == 5


# def test_succeed():
#     print("Coucou, c'est le test qui parle!!!") # demo de pytest -s
#     assert inc(3) == 4


# Tester qu'un code soulève une exception


# import pytest


# def test_div_by_zero():
#     with pytest.raises(ZeroDivisionError):
#         div(1, 0)


# # Exemples additionnels
# # Illustration du mécanisme d'introspection des assertions

# def test_set_comparison():
#     set1 = set("1308")
#     set2 = set("8035")
#     assert set1 == set2


# def test_eq_similar_text():
#     assert "foo 1 bar" == "foo 2 bar"

# # Exemples supplémentaires de tests échouants

# def test_not_div():
#     assert not div(10, 2)


# def test_eq_list():
#     assert [0,4, 1, 2] == [0, 1, 3]

# # Pour plus d'exemples, voir https://docs.pytest.org/en/latest/example/reportingdemo.html