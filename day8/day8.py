def get_input():
    with open("input.txt") as file:
        return file.read()

def quiz1(instructions):
    accumulator = 0
    visited_lines = []
    i = 0
    while True:
        instruction = instructions[i]
        if i in visited_lines:
            break
        visited_lines.append(i)
        if instruction[0] == "acc":
            accumulator += int(instruction[1])
            i += 1
        elif instruction[0] == "jmp":
            i += int(instruction[1])
        else:
            i += 1
    print(accumulator)

def visit_rec(instructions, index, visited, acc, changed):
    if index in visited:
        return None
    if index >= len(instructions):
        return acc
    else:
        visited.append(index)
        inst = instructions[index]
        if inst[0] == "acc":
            acc += int(inst[1])
            return visit_rec(instructions, index+1, visited, acc, changed)
        elif inst[0] == "jmp":
            if not changed:
                inst[0] = "nop"
                orig_visited = [e for e in visited]
                nop_res = visit_rec(instructions, index+1, visited, acc, True)
                visited = orig_visited
                inst[0] = "jmp"
                if nop_res:
                    return nop_res
            return visit_rec(instructions, index+int(inst[1]), visited, acc, changed)
        elif inst[0] == "nop":
            if not changed:
                inst[0] = "jmp"
                orig_visited = [e for e in visited]
                jmp_res = visit_rec(instructions, index+int(inst[1]), visited, acc, True)
                visited = orig_visited
                inst[0] = "nop"
                if jmp_res:
                    return jmp_res
            return visit_rec(instructions, index+1, visited, acc, changed)

def quiz2(instructions):
    accumulator = visit_rec(instructions, 0, [], 0, False)
    print(accumulator)


if __name__ == "__main__":
    lines = get_input().splitlines()
    instructions = [instruction.split(" ") for instruction in lines]
    quiz1(instructions)
    quiz2(instructions)
    
