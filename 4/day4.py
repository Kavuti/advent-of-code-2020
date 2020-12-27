import re

mandatory_fields = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid"
]

def get_input():
    with open("input.txt", "r") as file:
        return file.read()

def quiz1(data):
    valids = 0
    for passport in data:
        if all([field in passport for field in mandatory_fields]):
            valids += 1
    print(valids)

def quiz2(data):
    valids = 0
    for passport in data:
        if re.match(r"(?=.*byr:((19[2-9]\d)|200[0-2])\s)(?=.*iyr:((201[0-9])|2020)\s)(?=.*eyr:((202[0-9])|2030)\s)(?=.*hgt:(((59|6[0-9]|7[0-6])in)|((1[5-8][0-9]|19[0-3])cm))\s)(?=.*hcl:#[0-9a-f]{6}\s)(?=.*ecl:(amb|blu|brn|gry|grn|hzl|oth)\s)(?=.*pid:\d{9}\s)", 
            passport.replace("\n", " ")+" "):
            valids += 1
    print(valids)

if __name__ == "__main__":
    data = get_input().split("\n\n")
    quiz1(data)
    quiz2(data)