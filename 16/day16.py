import re


def get_input():
    with open("input.txt", "r") as file:
        return file.read()


def get_rules(input):
    results = re.findall(r"([a-z ]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)", input)
    dictionary = {result[0]: [*[n for n in range(int(result[1]), int(result[2])+1)], 
        *[n for n in range(int(result[3]), int(result[4])+1)]] 
        for result in results}
    return dictionary


def parse_tickets(input):
    results = re.findall(r"(?:[0-9]+,)+[0-9]+", input)
    return results


def get_nearby_tickets(input):
    return [[int(n) for n in t.split(',')] for t in parse_tickets(input)[1:]]


def get_your_ticket(input):
    return [int(n) for n in parse_tickets(input)[0].split(',')]


def follows_rules(ticket, rules):
    used_rules = []
    for n in ticket:
        found = False
        for name, vals in rules.items():
            if not name in used_rules and n in vals:
                found = True
                break
        if not found:
            return n
    return 0


def quiz1(data):
    rules = get_rules(data)
    tickets = get_nearby_tickets(data)
    sum_invalids = 0
    for ticket in tickets:
        sum_invalids += follows_rules(ticket, rules)
    print(sum_invalids)


def quiz2(data):
    rules = get_rules(data)
    tickets = get_nearby_tickets(data)
    your_ticket = get_your_ticket(data)

    valid_tickets = []
    for ticket in tickets:
        if follows_rules(ticket, rules) == 0:
            valid_tickets.append(ticket)

    column_rules_list = []
    for i in range(len(rules)):
        column = [t[i] for t in valid_tickets]
        column_rules_list.append([])
        for rule, vals in rules.items():
            if all([c in vals for c in column]):
                column_rules_list[i].append(rule)
    
    ordered_rules = {}
    reexecute = True
    to_delete = []
    while reexecute:     
        reexecute = False
        for i, column_rules in enumerate(column_rules_list):
            [column_rules.remove(t) for t in to_delete if t in column_rules]
            if len(column_rules) == 1:
                to_delete.append(column_rules[0])
                ordered_rules[column_rules[0]] = i
                column_rules.clear()
                reexecute = True
    

    result = 1

    for key, value in ordered_rules.items():
        if key.startswith('departure'):
            result *= your_ticket[value]             
   
    print(result)

if __name__ == "__main__":
    data = get_input()
    quiz1(data)
    quiz2(data)