import re
from pprint import pprint

def get_input():
    with open("input.txt", "r") as file:
        return file.read()


def get_appearence_dict(data):
    appearence = {}
    for dish in data:
        ingredients = re.search(r"([a-z ]+) \(", dish).groups(1)[0].split(' ')
        allergenes = re.search(r"\(contains (.+)\)", dish).groups(1)[0].split(', ')
        for ingredient in ingredients:
            if not ingredient in appearence:
                appearence[ingredient] = 0
            appearence[ingredient] += 1
    return appearence
    

def parse_data(data):
    regex = re.compile(r"([a-z ]+) \(contains ([a-z, ]+)\)")
    result = []
    for line in data:
        ingredients, allergens = regex.match(line).groups()
        ingredients, allergens = set(ingredients.split()), set(allergens.split(", "))
        result.append((ingredients, allergens))
    return result
        

def get_result_dict(data):
    result_data = parse_data(data)
    all_allergenes = set()
    [[all_allergenes.add(allergene) for allergene in allergenes] for _, allergenes in result_data]
    result_dict = {}
    potential_ingredients = {}
    for allergene in all_allergenes:
        potential_ingredients[allergene] = set.intersection(*[ingredient for ingredient, allergenes in result_data if allergene in allergenes])
    
    while len(result_dict) < len(all_allergenes):
        for allergene in all_allergenes:
            [potential_ingredients[allergene].discard(ingredient) for ingredient in result_dict.keys()]
            if len(potential_ingredients[allergene]) == 1:
                result_dict[potential_ingredients[allergene].pop()] = allergene

    return result_dict


def quiz1(data):
    result_data = parse_data(data)
    result_dict = get_result_dict(data)
    all_ingredients = []
    [[all_ingredients.append(ingredient) for ingredient in ingredients] for ingredients, _ in result_data]
    ingredients = [ingredient for ingredient in result_dict.keys()]
    print(len([ingredient for ingredient in all_ingredients if not ingredient in ingredients]))
    


def quiz2(data):
    result_data = parse_data(data)
    result_dict = get_result_dict(data)
    allergenes = sorted([allergene for _, allergene in result_dict.items()])
    result_inverted = {v: k for k, v in result_dict.items()}
    print(",".join([result_inverted[allergene] for allergene in allergenes]))
    

if __name__ == "__main__":
    data = get_input().splitlines()
    # print(get_result_dict(data))
    quiz1(data)
    quiz2(data)