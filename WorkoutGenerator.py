import WorkoutJsonReader
import random

exercise_pattern = ["PUSH", "LEGS", "CARDIO", "ABS",
                    "PULL", "LEGS", "CARDIO", "ABS",
                    "PUSH", "LEGS", "CARDIO", "ABS",
                    "PULL", "LEGS", "CARDIO", "ABS"]

def type_matches(item, item_type):
    type_list = list(item["exerciseTypes"])
    return item_type in type_list


def space_needs_match(item, available_equipment):
    if str(item["spaceNeeded"]) == "true":
        return "Space" in available_equipment
    return True


def equipment_matches(item, available_equipment):
    equipment_needed_for_exercise = list(item["neededEquipment"])
    return set(equipment_needed_for_exercise).issubset(set(available_equipment))


def get_exercise(item_list, item_type, available_equipment):
    for item in item_list:
        if (type_matches(item, item_type)
                and equipment_matches(item, available_equipment)
                and space_needs_match(item, available_equipment)):
            return item
    return get_exercise_basic(item_list, item_type)


def get_exercise_basic(item_list, item_type):
    for item in item_list:
        if type_matches(item, item_type):
            return item
    return None


def get_workout(available_equipment):
    exercises_list = WorkoutJsonReader.load_exercises()
    workout = []
    for exercise_type in exercise_pattern:
        random.shuffle(exercises_list)
        exercise = get_exercise(exercises_list, exercise_type, available_equipment)
        if exercise is not None:
            workout.append(exercise)
        else:
            print(f"Unable to find exercise matching {exercise_type}")
    return workout


# TEST 1
#  print(get_workout(["Chair", "Kettle", "Space"]))


# TEST 2
# test_item_no_space_need = {'name': 'Alt-Single Leg Box Squats',
#                           'description': '',
#                           'exerciseTypes': ['LEGS'],
#                           'neededEquipment': ['Chair'],
#                           'spaceNeeded': 'false'}
# test_item_space_needed = {"name": "Reverse lunge (chair) into front lunge alternate", "description": "",
#                          "exerciseTypes": ["LEGS"], "neededEquipment": ["Chair"], "spaceNeeded": "true"}
# test_equipment_space = ["Resistance Band", "Kettle Bell", "Space"]
# test_equipment_no_space = ["Resistance Band", "Kettle Bell"]
# print(space_needs_match(test_item_no_space_need, test_equipment_space)) #TRUE
# print(space_needs_match(test_item_no_space_need, test_equipment_no_space)) #TRUE
# print(space_needs_match(test_item_space_needed, test_equipment_space)) #TRUE
# print(space_needs_match(test_item_space_needed, test_equipment_no_space)) #FALSE


# TEST 3
# test_item_1 = {'name': 'Alt-Single Leg Box Squats',
#                           'description': '',
#                           'exerciseTypes': ['LEGS'],
#                           'neededEquipment': ['Chair'],
#                           'spaceNeeded': 'false'}
# test_item_2 = {"name": "Reverse lunge (chair) into front lunge alternate", "description": "",
#                "exerciseTypes": ["LEGS"], "neededEquipment": ["Chair", "Kettle Bell"], "spaceNeeded": "true"}
# test_equipment_1 = ["Resistance Band", "Kettle Bell", "Space"]
# test_equipment_2 = ["Resistance Band", "Kettle Bell", "Chair"]
# test_equipment_3 = ["Resistance Band", "Kettle Bell", "Chair"]
# print(equipment_matches(test_item_1, test_equipment_1)) # FALSE
# print(equipment_matches(test_item_1, test_equipment_2)) # TRUE
# print(equipment_matches(test_item_2, test_equipment_3)) # TRUE
# print(equipment_matches(test_item_1, test_equipment_3)) # TRUE
# print(equipment_matches(test_item_2, test_equipment_1)) # FALSE
