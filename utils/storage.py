import json

DATA_FILE = "data/tracker_data.json"


def load_data(file_path=DATA_FILE):
    with open(file_path, "r") as file:
        data = json.load(file)

    return data


def save_data(data, file_path=DATA_FILE):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=2)