import re


def get_input():
    with open("input.txt", "r") as file:
        return file.read()


def prepare_data(input_data):
    data = [row.split("=") for row in input_data.splitlines()]
    for row in data:
        match = re.match(r"mem\[([0-9]+)\]", row[0])
        if match:
            row[0] = match.group(1)
        row[0] = row[0].strip()
        row[1] = row[1].strip()
    return data


def get_number(dec_num, mask):
    stringed_number = f"{dec_num:b}"
    stringed_number = list((36-len(stringed_number))*'0' + stringed_number)
    for i in range(36):
        if mask[i] != 'X':
            stringed_number[i] = mask[i]
    masked_number = "".join(stringed_number)
    return int(masked_number, 2)


def quiz1(data):
    current_mask = None
    memory = {}
    for row in data:
        if row[0] == 'mask':
            current_mask = row[1]
        else:
            memory[row[0]] = get_number(int(row[1]), current_mask)
    print(sum([v for _, v in memory.items()]))
        
        
if __name__ == "__main__":
    data = prepare_data(get_input())
    quiz1(data)