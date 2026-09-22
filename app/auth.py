USERS = {
    "admin": "admin123",
    "developer": "dev123",
}


def authenticate(username: str, password: str) -> bool:
    return USERS.get(username) == password