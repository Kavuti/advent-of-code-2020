def get_input():
    with open("input.txt", "r") as file:
        return file.read()


def get_missing(numbers, preamble):
    for i, number in enumerate(numbers[preamble:]):
        found = False
        for j in numbers[i:preamble+i]:
            for k in numbers[i:preamble+i]:
                if j != k and j+k == number:
                    found = True
                    break
                if found:
                    break
        if not found:
            return number


def quiz1(numbers, preamble):
    print(get_missing(numbers, preamble))

    
def quiz2(numbers, preamble):
    missing = get_missing(numbers, preamble)
    value_dict = {i: [] for i in range(len(numbers))}
    i = 0
    for number in numbers:
        for j in range(0, i+1):
            value_dict[j].append(number)
            if sum(value_dict[j]) == missing:
                print(min(value_dict[j])+max(value_dict[j]))
                return
        i += 1


if __name__ == "__main__":
    numbers = [int(n) for n in get_input().splitlines()]
    quiz1(numbers, 25)
    quiz2(numbers, 25)