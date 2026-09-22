from app.activity import record_activity, get_activities


def test_record_activity():
    record_activity(1, "login")

    activities = get_activities(1)

    assert activities[-1]["activity"] == "login"


def test_multiple_activities():
    record_activity(2, "login")
    record_activity(2, "view_profile")

    activities = get_activities(2)

    assert activities[-2]["activity"] == "login"
    assert activities[-1]["activity"] == "view_profile"