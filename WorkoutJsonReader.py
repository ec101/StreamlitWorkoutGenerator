import json

FILENAME = "exercises.json"


def load_exercises():
    # open and read file as string
    file = open(f"{FILENAME}", "r")
    string_data = file.read()
    file.close()

    # use json to load file string as json object
    json_data = json.loads(string_data)
    # print(type(json_data))
    print(type(json_data[0]))
    return json_data


# TEST 1
# print(load_exercises())

