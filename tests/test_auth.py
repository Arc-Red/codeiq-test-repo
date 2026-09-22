from app.auth import authenticate


def test_valid_credentials():
    assert authenticate("admin", "admin123") is True


def test_invalid_credentials():
    assert authenticate("admin", "wrong") is False