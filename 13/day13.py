from functools import reduce


def get_input():
    with open("input.txt", "r") as file:
        return file.read()


def quiz1(minimum, ids):
    waitings = [bid - (minimum%bid) for bid in ids]
    min_waiting = min(waitings)
    selected_pos = waitings.index(min_waiting)
    print(min_waiting*ids[selected_pos])


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def quiz2(ids):
    new_ids = [i for i in ids if i != 1]
    offsets = []
    for i in range(len(ids)):
        if ids[i] != 1:
            offsets.append(int(ids[i]) - i)
    print(chinese_remainder(new_ids, offsets))


if __name__ == "__main__":
    data = get_input()
    data = data.splitlines()
    minimum = int(data[0])
    ids = [int(bid) for bid in data[1].split(',') if bid != 'x']
    ids_with_ones = [int(bid) for bid in data[1].replace('x', '1').split(',')]
    quiz1(minimum, ids)
    quiz2(ids_with_ones)
