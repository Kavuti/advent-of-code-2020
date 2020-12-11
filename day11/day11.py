def get_input():
    with open("input.txt", "r") as file:
        return file.read()


def count_near(data, i, j, generation):

    i_range = None
    j_range = None

    if i == 0:
        i_range = [0, 1]
    elif i == len(data)-1:
        i_range = [-1, 0]
    else:
        i_range = [-1, 0, 1]


    if j == 0:
        j_range = [0, 1]
    elif j == len(data[i])-1:
        j_range = [-1, 0]
    else:
        j_range = [-1, 0, 1]
                    

    occupied = 0
    for k in i_range:
        for l in j_range:
            if generation == 3:
                print(len(data[i]))
                input()
            if data[i+k][j+l] == "#":
                occupied += 1
    return occupied
            

def simulate(data, generation):
    new_data = []
    for i in range(len(data)):
        new_data.append('')
        for j in range(len(data[i])):
            if data[i][j] == 'L' or data[i][j] == '#':
                near = count_near(data, i, j, generation)
                if near == 0:
                    new_data[i] += '#'
                elif near >= 4:
                    new_data[i] += 'L'
            elif data[i][j] == '.':
                new_data[i] += '.'
    return new_data

def quiz1(data):
    previous = None
    current = data
    generation = 0
    while previous != current:
        previous = current
        generation += 1
        current = simulate(previous, generation)
    print(sum([row.count('#') for row in current]))


if __name__ == "__main__":
    data = get_input().splitlines()
    quiz1(data)