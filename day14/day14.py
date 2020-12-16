import re
from pprint import pprint

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
        

def apply_mask_recursively(num, mask, pos):
    if pos == len(num)-1:
        if mask[-1] == '0':
            return set()
        elif mask[-1] == '1':
            num[-1] = 1
            return {"".join(str(n) for n in num)}
        else:
            result = set()
            num[-1] = 0
            result.add("".join(str(n) for n in num))
            num[-1] = 1
            result.add("".join(str(n) for n in num))
            return result
    else:
        if mask[pos] == '0':
            return apply_mask_recursively(num, mask, pos+1)
        elif mask[pos] == '1':

            num[pos] = 1
            return apply_mask_recursively(num, mask, pos+1)

        else:
            result = set()
            num[pos] = 0
           
            first_path = apply_mask_recursively(num, mask, pos+1)
            result.add("".join(str(n) for n in num))
            num[pos] = 1
            second_path = apply_mask_recursively(num, mask, pos+1)
            result.add("".join(str(n) for n in num))
            return {*result, *first_path, *second_path}

            

def mask_address(dec_num, mask):
    stringed_number = f"{dec_num:b}"
    stringed_number = list((36-len(stringed_number))*'0' + stringed_number)
    return [int(n, 2) for n in apply_mask_recursively(stringed_number, mask, 0)]
    

def quiz2(data):
    current_mask = None
    memory = {}
    for row in data:
        if row[0] == 'mask':
            current_mask = row[1]
        else:
            addresses = mask_address(int(row[0]), current_mask)
            for a in addresses:
                memory[a] = int(row[1])

    print(sum(memory.values()))
        



if __name__ == "__main__":
    data = prepare_data(get_input())
    quiz1(data)
    quiz2(data)
