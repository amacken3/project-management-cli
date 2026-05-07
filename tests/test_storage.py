from utils.storage import load_data, save_data


def test_load_data_returns_dictionary():
    data = load_data()

    assert type(data) == dict


def test_load_data_has_required_keys():
    data = load_data()

    assert "users" in data
    assert "projects" in data
    assert "tasks" in data


def test_save_data_writes_to_json_file(tmp_path):
    test_file = tmp_path / "test_data.json"

    test_data = {
        "users": [],
        "projects": [],
        "tasks": []
    }

    save_data(test_data, test_file)
    loaded_data = load_data(test_file)

    assert loaded_data == test_data