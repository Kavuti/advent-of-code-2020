from functools import lru_cache
import copy
from pprint import pprint

def get_input():
    with open("input.txt", "r") as file:
        return file.read()


def parse_line(line):
    line = line.split(':')
    if len(line) > 1:
        line[1] = line[1].strip()
        line[1] = line[1].split('|')
        for i, combo in enumerate(line[1]):
            if '"' in combo:
                combo = combo.replace('"', '')
            line[1][i] = combo.strip()
    return line


def get_rules(data):
    rules = {}
    for line in data:
        parsed_line = parse_line(line)
        if len(parsed_line) > 1:
            rules[parsed_line[0]] = parsed_line[1]
    return rules


def get_messages(data):
    messages = []
    for line in data:
        parsed_line = parse_line(line)
        if len(parsed_line) == 1:
            messages.append(parsed_line[0])
    return messages

def get_combo(*args):
    memory = {i: [] for i in range(len(args))}
    for i in range(len(args)):
        if i == 0:
            for arg in args[i]:
                memory[i].append(arg)
        else:
            prec_combos = memory[i-1]
            for prec_combo in prec_combos:
                for arg in args[i]:
                    memory[i].append(prec_combo+arg)
    return memory[len(args)-1]
            

def quiz1(data):
    rules = get_rules(data)

    @lru_cache
    def navigate(current_number):
        if len(rules[current_number]) == 1 and len(rules[current_number][0]) == 1:
            return rules[current_number][0]
        else:
            results = set()
            for combo in rules[current_number]:
                current_result = []
                for char in combo.split(' '):
                    navigation_result = navigate(char)
                    # print(navigation_result)
                    # input()
                    current_result.append(navigation_result) 
                # print(current_result)
                # input()
                [results.add(c) for c in get_combo(*current_result)]
                # print(results)
                # input()
            return results

    available = navigate('0')

    messages = get_messages(data)
    count = 0
    for message in messages:
        if message in available:
            count += 1

    print(count)



if __name__ == "__main__":
    data = get_input().splitlines()
    quiz1(data)
