import json
import os

FILE_NAME = "students.json"


def load_students():

    if not os.path.exists(FILE_NAME):
        return {}

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except (json.JSONDecodeError, FileNotFoundError):
        return {}


student_list = load_students()


def save_students():

    with open(FILE_NAME, "w") as file:
        json.dump(student_list, file, indent=4)