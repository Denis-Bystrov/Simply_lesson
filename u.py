import json


def get_all():
    with open("list.json", "r", encoding="utf-8") as file:
        return json.load(file)


def get_man(pk):
    people = get_all()
    maximum = len(people)
    for number in range(0, maximum):
        if people[number]["pk"] == pk:
            return people[number]


def get_by_skill(skill):
    skill = skill.title()
    people = get_all()
    maximum = len(people)
    name = []
    for i in range(0, maximum):
        if skill in people[i]["skills"]:
            name.append(people[i]["name"])

        result = ("")
        for i in range(0, len(name)):
            result += name[i]
            result += ", "
        result = result[0:len(result) - 2]

        if len(name) == 0:
            result = "There are no such people."

    return result
