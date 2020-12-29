import copy


def get_input():
    with open("/home/christian/Scrivania/advent-of-code-2020/23/input2.txt", "r") as file:
        return file.read()


def get_destination(element, pick, total):
    destination = ((element+total-2)%total)+1
    while destination in pick:
        destination = ((destination+total-2)%total)+1
    return destination


def shift(selected, selected_pos, data):
    new_selected_pos = data.index(selected)
    if new_selected_pos < selected_pos:
        data = [*data[len(data)-(selected_pos - new_selected_pos):len(data)], data[0:len(data)-(selected_pos - new_selected_pos)]]
    elif new_selected_pos > selected_pos:
        data = [*data[new_selected_pos-selected_pos:], *data[0:new_selected_pos-selected_pos]]
    return data

    # while data.index(selected) != selected_pos:
    #     data = [*data[1:], data[0]]
    # return data


def pick_nums(selected_pos, data):
    pick = []
    current = selected_pos+1
    for i in range(3):
        pick.append(data[(current+i)%len(data)])
    return pick


def elaborate(iterations, data, debug=False):
    selected_pos = 0
    for i in range(iterations):
        if debug and i % 100 == 0:
            print(i)
        selected = data[selected_pos]
        pick = pick_nums(selected_pos, data)
        destination = get_destination(data[selected_pos], pick, len(data))
        [data.remove(pick_element) for pick_element in pick]
        destination_pos = data.index(destination)
        data = [*data[0:destination_pos+1], *pick, *data[destination_pos+1:]]
        data = shift(selected, selected_pos, data)
        selected_pos = (selected_pos+1)%len(data)
    return data

def quiz1(data):
    data = elaborate(100, data)
    
    result = ""
    current = data.index(1)+1
    for i in range(len(data)-1):
        result += str(data[(current+i)%len(data)])
    print(result)


def quiz2(data):
    max_data = max(data)
    for i in range(max_data+1, 1000001):
        data.append(i)
    
    data = elaborate(10000000, data, True)

    one_index = data.index(1)
    print(data[one_index+1]*data[one_index+2])

if __name__ == "__main__":
    data = [int(n) for n in get_input()]
    quiz1(copy.deepcopy(data))
    quiz2(copy.deepcopy(data))
