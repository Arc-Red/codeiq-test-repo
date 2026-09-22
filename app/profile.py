PROFILES = {
    1: {
        "id": 1,
        "name": "Admin User",
        "email": "admin@example.com",
    },
    2: {
        "id": 2,
        "name": "Developer User",
        "email": "developer@example.com",
    },
}


def get_profile(user_id: int):
    return PROFILES.get(user_id)