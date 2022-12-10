def read_input(filename):
    with open(filename) as f:
        input = f.read().splitlines()
    return input

def get_folder_name():
    folders = __file__.split('/')
    return folders[-2]

def get_wood(input):
    wood = []
    for line in input:
        row = [int(x) for x in list(line)]
        wood.append(row)
    return wood

def get_viewing_distance(wood, x, y, dir):
    total = 0
    x_len = len(wood[0])
    y_len = len(wood)
    if dir == "N":
        for i in range(y-1, -1, -1):
            if wood[i][x] >= wood[y][x]:
                total += 1
                break
            else:
                total += 1
    elif dir == "E":
        for i in range(x+1, x_len, 1):
            if wood[y][i] >= wood[y][x]:
                total += 1
                break
            else:
                total += 1
    elif dir == "S":
        for i in range(y+1, y_len, 1):
            if wood[i][x] >= wood[y][x]:
                total += 1
                break
            else:
                total += 1
    elif dir == "W":
        for i in range(x-1, -1, -1):
            if wood[y][i] >= wood[y][x]:
                total += 1
                break
            else:
                total += 1
    return total

def get_scenic_score(wood, x, y):
    score = 1
    for dir in ("N", "S", "W", "E"):
        score *= get_viewing_distance(wood, x, y, dir)
    return score

def sol1(input):
    wood = get_wood(input)
    # print(wood)
    visible_wood = []
    for row in wood:
        visible_wood.append([])
        for tree in row:
            visible_wood[-1].append(0)
    # print(visible_wood)
    for idx_row, row in enumerate(wood):
        last_visible = None
        for idx_el, el in enumerate(row):
            if last_visible == None or wood[idx_row][idx_el] > last_visible:
                last_visible = wood[idx_row][idx_el]
                visible_wood[idx_row][idx_el] = 1
    # print(visible_wood)
    for idx_row, row in enumerate(wood):
        last_visible = None
        for idx_el, el in reversed(list(enumerate(row))):
            if last_visible == None or wood[idx_row][idx_el] > last_visible:
                last_visible = wood[idx_row][idx_el]
                visible_wood[idx_row][idx_el] = 1
    # print(visible_wood)
    for idx_el, el in enumerate(wood[0]):
        last_visible = None
        for idx_row, row in enumerate(wood):
            if last_visible == None or wood[idx_row][idx_el] > last_visible:
                last_visible = wood[idx_row][idx_el]
                visible_wood[idx_row][idx_el] = 1
    # print(visible_wood)
    for idx_el, el in enumerate(wood[0]):
        last_visible = None
        for idx_row, row in reversed(list(enumerate(wood))):
            if last_visible == None or wood[idx_row][idx_el] > last_visible:
                last_visible = wood[idx_row][idx_el]
                visible_wood[idx_row][idx_el] = 1
    # print(visible_wood)
    total = 0
    for row in visible_wood:
        total += row.count(1)
    return total


def sol2(input):
    wood = get_wood(input)
    winning_score = 0
    for y, row in enumerate(wood):
        for x, el in enumerate(row):
            score = get_scenic_score(wood, x, y)
            if score > winning_score:
                winning_score = score
    return winning_score

if __name__ == "__main__":
    input = read_input(f"{get_folder_name()}/input")
    print(f"Advent Of Code 2022 - {get_folder_name()}")
    result1 = sol1(input)
    print("First solution is: ", result1)
    result2 = sol2(input)
    print("Second solution is: ", result2)