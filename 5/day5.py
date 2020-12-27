def get_input():
    with open("input.txt", "r") as file:
        return file.read()


def get_seat_row(seat, front, back):
    if len(seat) == 1:
        if seat[0] == "F":
            return front
        return back
    else:
        offset = int((back-front)/2+1)
        if seat[0] == "F":
            return get_seat_row(seat[1:], front, back-offset)
        return get_seat_row(seat[1:], front+offset, back)


def get_seat_column(seat, left, right):
    if len(seat) == 1:
        if seat[0] == "L":
            return left
        return right
    else:
        offset = int((right-left)/2+1)
        if seat[0] == "L":
            return get_seat_column(seat[1:], left, right-offset)
        return get_seat_column(seat[1:], left+offset, right)


def get_seat_id(seat):
    pass

def quiz1(seats):
    max_id = 0
    for seat in seats:
        id = get_seat_row(seat[:7], 0, 127) * 8 + get_seat_column(seat[7:], 0, 7)
        if id > max_id:
            max_id = id
    print(max_id)

# Much better alternative
def quiz1_alternative(seats):
    max_id = 0
    for seat in seats:
        seat = seat.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1")
        id = int(seat[:7], 2) * 8 + int(seat[7:], 2)
        if id > max_id:
            max_id = id
    print(max_id)

def quiz2(seats):
    ids = []
    for seat in seats:
        seat = seat.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1")
        ids.append(int(seat[:7], 2) * 8 + int(seat[7:], 2))
    ids.sort()
    for id in range(ids[1], ids[-1]):
        if not id in ids:
            print(id)
            break

if __name__ == "__main__":
    seats = get_input().splitlines()

    quiz1(seats)
    quiz1_alternative(seats)
    quiz2(seats)

    