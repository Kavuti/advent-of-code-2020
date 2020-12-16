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

def get_nearby_tickets(input):
    

if __name__ == "__main__":
    data = get_input()
    get_rules(data)