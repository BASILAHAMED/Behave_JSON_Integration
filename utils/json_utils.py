import json

def read_json_data(filepath):
    with open(filepath, "r") as file:
        return json.load(file)

def write_test_results(filepath, data):
    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)
