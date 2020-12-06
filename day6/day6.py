def get_input():
    with open("input.txt", "r") as file:
        return file.read()


def quiz1(groups):
    result = 0
    for group in groups:
        current = set({})
        for person in group:
            current = current.union(set(person))
        result += len(current)
    print(result)
            

def quiz2(groups):
    result = 0
    for group in groups:
        current = set(group[0])
        for person in group:
            current = current.intersection(set(person))
        result += len(current)
    print(result)


if __name__ == "__main__":
    data = get_input()
    groups = [group.splitlines() for group in data.split("\n\n")]
    quiz1(groups)
    quiz2(groups)