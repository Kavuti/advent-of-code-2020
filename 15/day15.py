import sys
from pprint import pprint
sys.setrecursionlimit(30000010)

def get_input():
    with open("input.txt", "r") as file:
        return file.read()


def elaborate(data, cache):
    if len(data) == 2020:
        return data
    else:        
        num_to_use = None
        if len(cache[data[-1]]) == 1:
            num_to_use = 0
        else:
            num_to_use = cache[data[-1]][-1] - cache[data[-1]][-2]
            
        if not num_to_use in cache:
            cache[num_to_use] = []
        cache[num_to_use].append(len(data))
        cache[num_to_use] = cache[num_to_use][len(cache[num_to_use])-2:]
        return elaborate([*data, num_to_use], cache)

def quiz2(data):
    cache = {d: [i] for i, d in enumerate(data)}
    for i in range(30000000):
        if len(cache[data[-1]]) == 1:
            num_to_use = 0
        else:
            num_to_use = cache[data[-1]][-1] - cache[data[-1]][-2]
        if not num_to_use in cache:
            cache[num_to_use] = []
        cache[num_to_use].append(len(data))
        data.append(num_to_use)
    print(data[30000000-1])


def quiz1(data):
    cache = {d: [i] for i, d in enumerate(data)}
    pprint(elaborate(data, cache)[-1])



if __name__ == "__main__":
    data = [int(n) for n in get_input().split(',')]

    quiz1(data)
    quiz2(data)