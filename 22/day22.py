import re
import copy

def get_input():
    with open("input.txt", "r") as file:
        return file.read()


def which_max(n1, n2):
    if n1 > n2: 
        return 0 
    else: 
        return 1


def quiz1(p1, p2):
    while len(p1) > 0 and len(p2) > 0:
        if p1[0] > p2[0]:
            p1.append(p1[0])
            p1.append(p2[0])
            p1 = p1[1:]
            p2 = p2[1:]
        else:
            p2.append(p2[0])
            p2.append(p1[0])
            p1 = p1[1:]
            p2 = p2[1:]
    if len(p1) == 0:
        print(sum([n*(len(p2)-i) for i, n in enumerate(p2)]))
    else:
        print(sum([n*(len(p1)-i) for i, n in enumerate(p1)]))


def string_it(deck):
    return ",".join([str(card) for card in deck])


def elaborate_win(l1, l2, winner):
        if winner == 0 and len(l2) > 0:
            l1.append(l1[0])
            l1.append(l2[0])
            l1 = l1[1:]
            l2 = l2[1:]
        elif winner == 1 and len(l1) > 0:
            l2.append(l2[0])
            l2.append(l1[0])
            l1 = l1[1:]
            l2 = l2[1:]
        return l1, l2


def play_game(l1, l2):
        visited = set()
        while len(l1) > 0 and len(l2) > 0:
            tupled = (tuple(l1), tuple(l2))
            if tupled in visited:
                return 0, l1, l2
            visited.add(tupled)
            if l1[0] < len(l1) and l2[0] < len(l2):
                winner, _1, _2 = play_game(l1[1:l1[0]+1], l2[1:l2[0]+1])
                l1, l2 = elaborate_win(l1, l2, winner)
            else:
                if l1[0] > l2[0]:
                    l1, l2 = elaborate_win(l1, l2, 0)
                else:
                    l1, l2 = elaborate_win(l1, l2, 1)

        if len(l2) == 0:
            return 0, l1, l2
        return 1, l1, l2


def quiz2(p1, p2):
    winner, l1, l2 = play_game(p1, p2)
    if winner == 1:
        print(sum([n*(len(l2)-i) for i, n in enumerate(l2)]))
    else:
        print(sum([n*(len(l1)-i) for i, n in enumerate(l1)]))


if __name__ == "__main__":
    players = get_input().split('\n\n')
    player1 = [int(n) for n in players[0].split('\n')[1:]]
    player2 = [int(n) for n in players[1].split('\n')[1:]]
    quiz1(copy.deepcopy(player1), copy.deepcopy(player2))
    quiz2(copy.deepcopy(player1), copy.deepcopy(player2))