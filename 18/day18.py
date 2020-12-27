import re


PATTERN = r"\([0-9 +*]+\)"

SUM_PATTERN = r"[0-9]+ \+ [0-9]+"

def get_input():
    with open("input.txt", "r") as file:
        return file.read()


def resolve(expression):
    elements = expression.split(' ')
    while len(elements) > 1:
        n1 = elements[0]
        n2 = elements[2]
        op = elements[1]
        elements = elements[3:]
        result = eval(n1+' '+op+' '+n2)
        elements.insert(0, str(result))
    return elements[0]


def execute(expression):
    while True:
        match_obj = re.search(PATTERN, expression)
        if not match_obj:
            break
        match = match_obj.group(0)
        executed_match = resolve(match[1:-1])
        expression = expression.replace(match, executed_match)
    return int(resolve(expression))


def execute_second(expression):
    repeat = True
    while repeat:
        repeat = False
        while True:
            match_obj = re.search(SUM_PATTERN, expression)
            if not match_obj:
                break
            repeat = True
            match = match_obj.group(0)
            executed_match = resolve(match)
            expression = expression.replace(match, executed_match)
        match_obj = re.search(PATTERN, expression)
        if match_obj:
            match = match_obj.group(0)
            executed_match = resolve(match[1:-1])
            expression = expression.replace(match, executed_match)
            repeat = True
    return int(resolve(expression))


def quiz1(data):
    result = 0
    for d in data:
        result += execute(d)
    print(result)

def quiz2(data):
    result = 0
    for d in data:
        res = execute_second(d)
        # print(res)
        # input()
        result += res
    print(result)

if __name__ == "__main__":
    data = get_input().splitlines()
    quiz1(data)
    quiz2(data)