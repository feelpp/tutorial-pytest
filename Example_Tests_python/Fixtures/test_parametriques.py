import pytest
import smtplib


# Exemple avec @pytest.fixture

# @pytest.fixture(scope="module", params=["smtp.gmail.com", "mail.python.org"])
# def smtp_connection(request):
#     smtp_connection = smtplib.SMTP(request.param, 587, timeout=5)
#     yield smtp_connection
#     print("finalizing {}".format(smtp_connection))
#     smtp_connection.close()


# def test_ehlo(smtp_connection):
#     response, msg = smtp_connection.ehlo()
#     assert response == 250
#     assert b"smtp.gmail.com" in msg
#     assert 0


# def test_noop(smtp_connection):
#     response, msg = smtp_connection.noop()
#     assert response == 250
#     assert 0


# Exemple avec @pytest.mark.parametrize
# @pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
# def test_eval(test_input, expected):
#     assert eval(test_input) == expected