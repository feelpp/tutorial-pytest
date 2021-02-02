# contents of test_module.py with source code and the test
import pytest
import smtplib
import os
from pathlib import Path



# Example 1: on s'affranchit du nom de l'utilisateur

def getssh():
    """Simple function to return expanded homedir ssh path."""
    return Path.home() / ".ssh"


def test_getssh(monkeypatch):
    # mocked return function to replace Path.home
    # always return '/fakeuser'
    def mockreturn():
        return Path("/fakeuser")

    # Application of the monkeypatch to replace Path.home
    # with the behavior of mockreturn defined above.
    monkeypatch.setattr(Path, "home", mockreturn)

    # Calling getssh() will use mockreturn in place of Path.home
    # for this test with the monkeypatch.
    x = getssh()
    #print("\n This is the path of the monkeypatched .ssh folder: ", x) # for demo purpose
    assert x == Path("/fakeuser/.ssh")
    assert 0

# Exemple 2: on évite de se connecter au serveur!!

@pytest.fixture(scope="module")
def smtp_connection():
    smtp_connection = smtplib.SMTP("smtp.gmail.com", 587, timeout=5)
    yield smtp_connection  # provide the fixture value
    print("teardown smtp")
    smtp_connection.close()


def test_ehlo(smtp_connection, monkeypatch):
    def mockreturn():
        return 356, b"Faux message pour le test"

    monkeypatch.setattr(smtp_connection, "ehlo", mockreturn)

    response, msg = smtp_connection.ehlo()
    assert b"Faux message" in msg # et non plus smtp.google.com
    assert response == 356 # et non plus 250!!!
    assert 0  # for demo purposes


# Exemple 3: setitem, delitem ...

def get_os_user_lower():
    """Simple retrieval function.
    Returns lowercase USER or raises OSError."""
    username = os.getenv("USER")

    if username is None:
        raise OSError("USER environment is not set.")

    return username.lower()


def test_upper_to_lower(monkeypatch):
    """Set the USER env var to assert the behavior."""
    monkeypatch.setenv("USER", "TestingUser")
    assert get_os_user_lower() == "testinguser"


def test_raise_exception(monkeypatch):
    """Remove the USER env var and assert OSError is raised."""
    monkeypatch.delenv("USER", raising=False)

    with pytest.raises(OSError):
        _ = get_os_user_lower()


# Exemple 4: les mêmes tests réécrits avec des fixtures

def get_os_user_lower():
    """Simple retrieval function.
    Returns lowercase USER or raises OSError."""
    username = os.getenv("USER")

    if username is None:
        raise OSError("USER environment is not set.")

    return username.lower()

# print(get_os_user_lower())

@pytest.fixture
def mock_env_user(monkeypatch):
    monkeypatch.setenv("USER", "TestingUser")


@pytest.fixture
def mock_env_missing(monkeypatch):
    monkeypatch.delenv("USER", raising=False)


# notice the tests reference the fixtures for mocks
def test_upper_to_lower(mock_env_user):
    assert get_os_user_lower() == "testinguser"


def test_raise_exception(mock_env_missing):
    with pytest.raises(OSError):
        _ = get_os_user_lower()



