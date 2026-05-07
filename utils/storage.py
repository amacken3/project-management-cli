import json

from models.user import User

DATA_FILE = "data/tracker_data.json"

DEFAULT_DATA = {
    "users": [],
    "projects": [],
    "tasks": []
}


def load_data(file_path=DATA_FILE):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)

        return data

    except FileNotFoundError:
        return DEFAULT_DATA.copy()

    except json.JSONDecodeError:
        return DEFAULT_DATA.copy()


def save_data(data, file_path=DATA_FILE):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=2)

def save_users(users, file_path=DATA_FILE):
    data = {
        "users": [user.to_dict() for user in users],
        "projects": [],
        "tasks": []
    }

    save_data(data, file_path)


def load_users(file_path=DATA_FILE):
    data = load_data(file_path)

    users = []

    for user_data in data["users"]:
        user = User.from_dict(user_data)
        users.append(user)

    return users