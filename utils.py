import json

with open('candidates.json', 'r') as fp:
    data = json.load(fp)


def load_candidates_from_json():
    return data


def get_candidate(candidate_id):
    return data[int(candidate_id) - 1]


def get_candidates_by_name(name):
    search_data = []
    for item in data:
        if item["name"].split(" ")[0].lower() == name.lower():
            search_data.append(item)
    return search_data


def get_candidates_by_skill(skill_name):
    skill_data = []
    for item in data:
        if skill_name.lower() in item["skills"].lower().split(", "):
            skill_data.append(item)
    return skill_data
