import re

def get_input():
    with open("input.txt", "r") as file:
        text = file.read()
        return text

def get_values(line):
    pattern = r"([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)"
    match_obj = re.match(pattern, line)
    if match_obj:
        return match_obj.group(1), match_obj.group(2), match_obj.group(3), match_obj.group(4)
    return None

def quiz1(lines):
    counter = 0
    for line in lines:
        minn, maxn, letter, password = get_values(line)
        letter_count = password.count(letter) 
        if letter_count >= int(minn) and letter_count <= int(maxn):
            counter += 1
    print(f"Valid passwords: {counter}")

def quiz2(lines):
    counter = 0
    for line in lines:
        first, second, letter, password = get_values(line)
        if (password[int(first)-1] == letter) ^ (password[int(second)-1] == letter):
            counter += 1
    print(f"Valid passwords: {counter}")

if __name__ == "__main__":
    lines = get_input().splitlines()
    quiz1(lines)
    quiz2(lines)