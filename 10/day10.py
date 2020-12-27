from functools import lru_cache


def get_input():
    with open("input.txt", "r") as file:
        return file.read()


def quiz1(numbers):
    numbers.sort()
    ones = 0
    threes = 0
    if numbers[0] == 1:
        ones = 1
    elif numbers[0] == 3:
        threes = 1
    for i in range(len(numbers)-1):
        if numbers[i+1]-numbers[i] == 1:
            ones += 1
        elif numbers[i+1]-numbers[i] == 3:
            threes += 1
    threes += 1
    print(ones*threes)


def quiz2(numbers):
    numbers = sorted([0, *numbers, max(numbers)+3])

    @lru_cache
    def get_alternatives(pos):
        if pos == len(numbers)-1:
            return 1
        else:
            alternatives = 0
            for i in range(1, len(numbers)):
                if pos+i < len(numbers) and (numbers[pos+i] - numbers[pos]) <= 3:
                    alternatives += get_alternatives(pos+i)
            return alternatives
    
    print(get_alternatives(0))


if __name__ == "__main__":
    numbers = [int(n) for n in get_input().splitlines()]
    quiz1(numbers)
    quiz2(numbers)
    