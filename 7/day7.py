def get_input():
    with open("input2.txt", "r") as file:
        return file.read()

def navigate(whole_dict, shiny_containers):
    restart = True
    while restart:
        restart = False
        for bag, value in whole_dict.items():
            for element in value:
                if (element[2:] == "shiny gold" or element[2:] in shiny_containers) and not bag in shiny_containers:
                    shiny_containers.add(bag)
                    restart = True
    return shiny_containers


def navigate_recursively(whole_dict, current):
    if (not current in whole_dict) or (not whole_dict[current]):
        return 0
    else:
        total = 0
        for element in whole_dict[current]:
            total += int(element[0]) * (navigate_recursively(whole_dict, element[2:])+1)
        return total


def prepare_data(lines):
    whole_dict = {}
    for line in lines:
        line_parts = line.split("contain")
        index = line_parts[0].strip()
        whole_dict[index] = [l.strip() for l in line_parts[1].split(",")]
        if "no other" in whole_dict[index]:
            whole_dict[index].remove("no other")
    return whole_dict

def quiz1(lines):
    whole_dict = prepare_data(lines)
    shiny_containers = navigate(whole_dict, set({}))
    print(len(shiny_containers))

def quiz2(lines):
    whole_dict = prepare_data(lines)
    print(navigate_recursively(whole_dict, "shiny gold"))

if __name__ == "__main__":
    lines = get_input()
    lines = lines.replace(".", "").replace("bags", "").replace("bag", "").splitlines()
    quiz1(lines)
    quiz2(lines)
