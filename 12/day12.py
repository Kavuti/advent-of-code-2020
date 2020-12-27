from math import *

def get_input():
    with open("input.txt", "r") as file:
        return file.read()


def quiz1(instructions):
    pos = [0, 0]
    factor = [1, 0]
    for inst in instructions:
        val = int(inst[1:])
        if inst[0] == 'N':
            pos[1] += val
        if inst[0] == 'W':
            pos[0] -= val
        if inst[0] == 'S':
            pos[1] -= val
        if inst[0] == 'E':
            pos[0] += val
        if inst[0] == 'F':
            pos[0] += factor[0]*val
            pos[1] += factor[1]*val
        if inst[0] == 'L':
            for i in range(int(val/90)):
                if factor == [1, 0]:
                    factor = [0, 1]
                elif factor == [0, 1]:
                    factor = [-1, 0]
                elif factor == [-1, 0]:
                    factor = [0, -1]
                elif factor == [0, -1]:
                    factor = [1, 0]
            
                    
        if inst[0] == 'R':
            for i in range(int(val/90)):
                if factor == [1, 0]:
                    factor = [0, -1]
                elif factor == [0, -1]:
                    factor = [-1, 0]
                elif factor == [-1, 0]:
                    factor = [0, 1]
                elif factor == [0, 1]:
                    factor = [1, 0]

    print(abs(pos[0]) + abs(pos[1]))


def rotate(distance, val):
    degrees = pi/180*val
    x = float(distance[0])*cos(degrees) - float(distance[1])*sin(degrees)
    y = float(distance[0])*sin(degrees) + float(distance[1])*cos(degrees)
    return [int(round(x)), int(round(y))]


def quiz2(instructions):
    waypoint = [10, 1]
    pos = [0, 0]
    factor = [1, 1]
    for inst in instructions:
        val = int(inst[1:])
        if inst[0] == 'N':
            waypoint[1] += val
        if inst[0] == 'W':
            waypoint[0] -= val
        if inst[0] == 'S':
            waypoint[1] -= val
        if inst[0] == 'E':
            waypoint[0] += val
        if inst[0] == 'F':
            pos[0] += waypoint[0]*val
            pos[1] += waypoint[1]*val
        if inst[0] == 'L':
            waypoint = rotate(waypoint, val)
        if inst[0] == 'R':
            waypoint = rotate(waypoint, 360-val)

    print(abs(pos[0])+abs(pos[1]))


if __name__ == "__main__":
    instructions = get_input().splitlines()
    quiz1(instructions)
    quiz2(instructions)


