from pprint import pprint
from functools import lru_cache

def get_input():
    with open("input.txt", "r") as file:
        return file.read()


def count_near(data, i, j):
    occupied = 0

    for k in [-1, 0 ,1]:
        for l in [-1, 0, 1]:
            if k == 0 and l == 0:
                continue
            if (i+k >= 0 and i+k < len(data) and j+l >= 0 and j+l < len(data[i+k])):
                occupied += data[i+k][j+l] == "#"

    return occupied
    

def count_near2(data, i, j):
    occupied = 0

    @lru_cache
    def go_through(i, j, i_fact, j_fact):
        if i < 0 or i > len(data)-1 or j < 0 or j > len(data[i])-1:
            return 0
        if (i <= 0 and i_fact < 0) or (j <= 0 and j_fact < 0) or \
            (i >= len(data)-1 and i_fact > 0) or (j >= len(data[i])-1 and j_fact > 0):
            return data[i][j] == "#"
        else:
            if data[i][j] == "#":
                return 1
            if data[i][j] == "L":
                return 0
            return go_through(i+i_fact, j+j_fact, i_fact, j_fact)


    for k in [-1, 0, 1]:
        for l in [-1, 0, 1]:
            if k == 0 and l == 0:
                continue
            occupied += go_through(i+k, j+l, k, l)

    return occupied


def simulate(data):
    new_data = []
    for i in range(len(data)):
        new_data.append('')
        for j in range(len(data[i])):
            if data[i][j] == 'L' or data[i][j] == '#':
                near = count_near(data, i, j)
                if near == 0:
                    new_data[i] += '#'
                elif near >= 4:
                    new_data[i] += 'L'
                else:
                    new_data[i] += data[i][j]
            elif data[i][j] == '.':
                new_data[i] += '.'
    return new_data


def simulate2(data):
    new_data = []
    for i in range(len(data)):
        new_data.append('')
        for j in range(len(data[i])):
            if data[i][j] == 'L' or data[i][j] == '#':
                near = count_near2(data, i, j)
                if near == 0:
                    new_data[i] += '#'
                elif near >= 5:
                    new_data[i] += 'L'
                else:
                    new_data[i] += data[i][j]
            elif data[i][j] == '.':
                new_data[i] += '.'
    return new_data


def quiz1(data):
    previous = None
    current = data
    while previous != current:
        previous = current
        current = simulate(previous)

    print(sum([row.count('#') for row in current]))


def quiz2(data):
    previous = None
    current = data
    while previous != current:
        previous = current
        current = simulate2(previous)

    print(sum([row.count('#') for row in current]))



if __name__ == "__main__":
    data = get_input().splitlines()
    quiz1(data)
    quiz2(data)