def read_input(filename):
    with open(filename) as f:
        input = f.read().splitlines()
    return input

def get_folder_name():
    folders = __file__.split('/')
    return folders[-2]

def get_sections_edges(assignment):
    sections = assignment.split(",")
    s11 = int(sections[0].split("-")[0])
    s12 = int(sections[0].split("-")[1])
    s21 = int(sections[1].split("-")[0])
    s22 = int(sections[1].split("-")[1])
    return s11, s12, s21, s22

def sol1(input):
    total = 0
    for line in input:
        s11, s12, s21, s22 = get_sections_edges(line)
        if (s11 >= s21 and s11 <= s22 and s12 >= s21 and s12 <= s22) or (s21 >= s11 and s21 <= s12 and s22 >= s11 and s22 <= s12):
            total += 1
    return total

def sol2(input):
    total = 0
    for line in input:
        s11, s12, s21, s22 = get_sections_edges(line)
        if (s11 >= s21 and s11 <= s22) or (s12 >= s21 and s12 <= s22) or (s21 >= s11 and s21 <= s12) or (s22 >= s11 and s22 <= s12):
            total += 1
    return total

if __name__ == "__main__":
    input = read_input(f"{get_folder_name()}/input")
    print(f"Advent Of Code 2022 - {get_folder_name()}")
    result1 = sol1(input)
    print("First solution is: ", result1)
    result2 = sol2(input)
    print("Second solution is: ", result2)