def read_input(filename):
    with open(filename) as f:
        input = f.read().splitlines()
    return input

def get_folder_name():
    folders = __file__.split('/')
    return folders[-2]

def get_data_from_input(input):
    moves = []
    stacks = {}
    stack_lines = []
    indexes = []
    for line in input:
        if line.startswith("   ") or line.startswith("["):
            stack_lines.append(line)
        elif line.startswith(" 1 "):
            s_results = line.split()
            for s in s_results:
                if s.isnumeric:
                    indexes.append(int(s))
        elif line.startswith("move "):
            m = {}
            l = line.split()
            m[l[0]] = int(l[1])
            m[l[2]] = int(l[3])
            m[l[4]] = int(l[5]) 
            moves.append(m)
    # print(indexes)
    # print(stack_lines)
    for i in indexes:
        stacks[i] = []
    # print(stacks)
    stack_lines.reverse()
    # print(stack_lines)
    for sl in stack_lines:
        for idx, lst in stacks.items():
            if sl[(idx-1)*4] == "[":
                lst.append(sl[(idx-1)*4+1])
    # print(stacks)
    # print(moves)
    return stacks, moves

def get_top_list(stacks):
    tl = ""
    for idx,stack in stacks.items():
        tl += stack[-1]
    return tl


def sol1(input):
    stacks, moves = get_data_from_input(input)
    for m in moves:
        for it in range(m["move"]):
            crate = stacks[m["from"]].pop()
            stacks[m["to"]].append(crate)
    return get_top_list(stacks)

def sol2(input):
    stacks, moves = get_data_from_input(input)
    for m in moves:
        crates_num = m["move"]
        stack_from = m["from"]
        stack_to = m["to"]
        crates_to_move = stacks[stack_from][-crates_num:]
        stacks[stack_from] = stacks[stack_from][:-crates_num]
        stacks[stack_to].extend(crates_to_move)
    return get_top_list(stacks)

if __name__ == "__main__":
    input = read_input(f"{get_folder_name()}/input")
    get_data_from_input(input)
    print(f"Advent Of Code 2022 - {get_folder_name()}")
    result1 = sol1(input)
    print("First solution is: ", result1)
    result2 = sol2(input)
    print("Second solution is: ", result2)