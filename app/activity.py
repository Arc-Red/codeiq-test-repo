activities = []


def record_activity(user_id: int, activity: str):
    activities.append({
        "user_id": user_id,
        "activity": activity,
    })


def get_activities(user_id: int):
    return [
        item for item in activities
        if item["user_id"] == user_id
    ]