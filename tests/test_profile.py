from app.profile import get_profile


def test_existing_profile():
    profile = get_profile(1)

    assert profile["name"] == "Admin User"
    assert profile["email"] == "admin@example.com"


def test_missing_profile():
    assert get_profile(999) is None