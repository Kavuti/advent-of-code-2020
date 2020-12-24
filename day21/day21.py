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
    

def get_responsibles_dict(data):
    memory = {}
    friends = {}
    appearence = {}
    all_allergenes = set()
    for dish in data:
        ingredients = re.search(r"([a-z ]+) \(", dish).groups(1)[0].split(' ')
        allergenes = re.search(r"\(contains (.+)\)", dish).groups(1)[0].split(', ')
        for ingredient in ingredients:
            if not ingredient in appearence:
                appearence[ingredient] = 0
            appearence[ingredient] += 1
            if not ingredient in friends:
                friends[ingredient] = set()
            for i in ingredients:
                friends[ingredient].add(i)
            if not ingredient in memory:
                memory[ingredient] = []
            distinct_ingredients = set(memory[ingredient])
            for allergene in allergenes:
                all_allergenes.add(allergene)
                if not allergene in distinct_ingredients and len(distinct_ingredients) > 0:
                    for i in friends[ingredient]:
                        if i in memory and not allergene in memory[i]:
                            memory[i].append(allergene)
                else:
                    memory[ingredient].append(allergene)

    allerg_resp = {}
    potential_resps = {}

    """
        Fixare da qui in poi. Attualmente il dizionario ha molti conflitti. Bisogna quindi
        prendere per ogni ingrediente gli allergeni potenziali e per ogni ingrediente con un solo
        potenziale allergene si conferma la scelta. Per tutti gli altri ingredienti, si escludono
        poi gli allergeni già utilizzati per gli ingredienti confermati.
    """
    for allergene in all_allergenes:
        max_count = 0
        max_responsible = None
        for ingredient, ing_allergenes in memory.items():
            count = ing_allergenes.count(allergene)
            if count == max_count:
                print(f"Conflicting {ingredient} with {max_responsible} on {allergene}")
            if count > max_count:
                max_count = count
                max_responsible = ingredient
        for ingredient, ing_allergenes in memory.items():
            if ingredient != max_responsible and ingredient in ing_allergenes:
                ing_allergenes.remove(allergene)

        memory[max_responsible] = [allergene]
        allerg_resp[allergene] = max_responsible
    return allerg_resp, appearence


def quiz1(data):
    allerg_resp, appearence = get_responsibles_dict(data)
    without_allergenes = []
    # appearence = get_appearence_dict(data)
    all_ings = set()
    for _, resp_ing in allerg_resp.items():
        all_ings.add(resp_ing)
    for ing in appearence.keys():
        if ing not in all_ings:
            without_allergenes.append(ing)

    result = 0
    for ingredient in without_allergenes:
        result += appearence[ingredient]

    print(result)


def quiz2(data):
    allerg_resp, _ = get_responsibles_dict(data)
    allerg_resp_list = sorted(list(allerg_resp.keys()))
    # result= = ""
    print(allerg_resp)
    ingredients = [allerg_resp[allerg] for allerg in allerg_resp_list]
    print(",".join(ingredients))
    

if __name__ == "__main__":
    data = get_input().splitlines()
    quiz1(data)
    quiz2(data)