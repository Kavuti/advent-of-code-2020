import os

def get_numbers():
    with open("input.txt", "r") as file:
        text = file.read()
        return text


def quiz1(numbers):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == 2020:
                print(f"{numbers[i]} + {numbers[j]} = 2020 - {numbers[i]} * {numbers[j]} = {numbers[i]*numbers[j]}")
                return

def quiz2(numbers):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            for k in range(j+1, len(numbers)):
                if numbers[i] + numbers[j] + numbers[k] == 2020:
                    print(f"{numbers[i]} + {numbers[j]} + {numbers[k]} = 2020 - {numbers[i]} * {numbers[j]} * {numbers[k]}= {numbers[i]*numbers[j]*numbers[k]}")
                    return

if __name__ == "__main__":
    numbers = [int(n) for n in get_numbers().splitlines()]
    quiz1(numbers)
    quiz2(numbers)