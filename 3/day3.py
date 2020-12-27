def get_input():
    with open("input.txt", "r") as file:
        return file.read()

def quiz1(data):
    trees = slope(data, 3, 1)
    print(f"Slope right 3 down 1. Trees encountered: {trees}")

def slope(data, right, down):
    trees = 0
    for i in range(0, len(data), down):
        row = down*i%len(data)
        if data[row][right*i%len(data[row])] == "#":
            trees += 1
    return trees

def quiz2(data):
    oneone = slope(data, 1, 1)
    threeone= slope(data, 3, 1)
    fiveone = slope(data, 5, 1)
    sevenone = slope(data, 7, 1)
    onetwo = slope(data, 1, 2)

    result = oneone * threeone * fiveone * sevenone * onetwo
    print(f"Result: {result}")


if __name__ == "__main__":
    data = get_input()
    data = data.splitlines()
    real_data = []
    for d in data:
        real_data.append(d)
    quiz1(real_data)
    quiz2(real_data)