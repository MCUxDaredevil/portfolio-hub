import json


def read_json(file_path="config.json"):
    """ Read a json file and return the data as a dictionary """
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def write_json(data, file_path="config.json"):
    """ Write data to a json file """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
    return True


def update_json(key, value, file_path="config.json"):
    """ Update a json file with a new key value pair """
    data = read_json(file_path)
    data.update({key: value})
    write_json(file_path, data)
    return True


def delete_key(key, file_path="config.json"):
    """ Delete a key value pair from a json file """
    data = read_json(file_path)
    data.pop(key)
    write_json(file_path, data)
    return True


def get_user(file_path="config.json"):
    """ Get the user from a json file """
    data = read_json(file_path)
    return data.get("username", None)
