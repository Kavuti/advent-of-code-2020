import re
from pprint import pprint

def get_input():
    with open("input2.txt", "r") as file:
        return file.read()  


class Tile:

    NONE = 0
    TOP = 1
    RIGHT = 2
    BOTTOM = 3
    LEFT = 4

    def __init__(self, id, lines):
        self.id = id
        self.top = []
        self.left = []
        self.right = []
        self.bottom = []

        first_left = []
        first_top = []
        first_bottom = []
        first_right = []
        for i, line in enumerate(lines):
            if line:
                if i == 0:
                    [first_top.append(j) for j, char in enumerate(line) if char == '#']
                elif i == len(lines)-1:
                    [first_bottom.insert(0, j) for j, char in enumerate(line) if char == '#']
                if line[0] == '#':
                    first_left.insert(0, i)
                if line[-1] == '#':
                    first_right.append(i)
            
        first_top.sort()
        first_bottom.sort()
        first_left.sort()
        first_right.sort()

        self.top.append("".join([str(n) for n in first_top]))
        self.right.append("".join([str(n) for n in first_right]))
        self.left.append("".join([str(n) for n in first_left]))
        self.bottom.append("".join([str(n) for n in first_bottom]))

        self.top.append("".join(sorted([str(9-n) for n in first_top])))
        self.right.append("".join(sorted([str(9-n) for n in first_right])))
        self.left.append("".join(sorted([str(9-n) for n in first_left])))
        self.bottom.append("".join(sorted([str(9-n) for n in first_bottom])))
        
    def rotate(self):
        self.top, self.right, self.bottom, self.left = sorted([9-n for n in self.left]), self.top, sorted([9-n for n in self.right]), self.bottom

        
    def matches(self, other):
        if self.top == other.bottom:
            return Tile.TOP
        if self.right == other.left:
            return Tile.RIGHT
        if self.bottom == other.top:
            return Tile.BOTTOM
        if self.left == other.right:
            return Tile.LEFT
        return Tile.NONE


def prepare_data(data):
    results = re.findall(r"Tile ([0-9]+):\n((?:[.#]+\n{1,2})+)", data)
    tiles = []
    for result in results:
        id = result[0]
        lines = result[1].split('\n')
        tile = Tile(id, lines)
        tiles.append(tile)

    
    return tiles


def quiz1(data):
    tiles = prepare_data(data) 

    all_combinations = []
    for tile in tiles:
        current = {*(tile.top), *(tile.bottom), *(tile.left), *(tile.right)}
        [all_combinations.append(c) for c in current]

    singles = []
    for combo in all_combinations:
        if len(x)
        
    singles = list(filter(lambda x: all_combinations.count(x) == 1, all_combinations))
    pprint(singles)


if __name__ == "__main__":
    data = get_input()
    # tiles = prepare_data(data)
    # td = {t.id: t for t in tiles}
    # t1 = td['2729']
    # t2 = td['1951']

    quiz1(data)