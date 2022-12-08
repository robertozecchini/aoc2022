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
    pass

if __name__ == "__main__":
    input = read_input(f"{get_folder_name()}/input")
    print(f"Advent Of Code 2022 - {get_folder_name()}")
    result1 = sol1(input)
    print("First solution is: ", result1)
    result2 = sol2(input)
    print("Second solution is: ", result2)