from pprint import pprint
import copy
from cube import Cube
from hypercube import HyperCube


def get_input():
    with open("input.txt", "r") as file:
        return file.read()


def quiz1(layer):
    cube = Cube(layer)
    for _ in range(6):
        cube.elaborate()
    print(cube.count_actives())


def quiz2(layer):
    cube = HyperCube(layer)
    for _ in range(6):
        cube.elaborate()
    print(cube.count_actives())


if __name__ == "__main__":
    layer = get_input().splitlines()
    
    quiz1(layer)
    quiz2(layer)