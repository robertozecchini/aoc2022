def read_input(filename):
    with open(filename) as f:
        input = f.readlines()
    return input

def get_folder_name():
    folders = __file__.split('/')
    return folders[-2]

def sol1(input):
    total = 0
    for line in input:
        length = len(line)
        rucksack1 = line[:length//2]
        rucksack2 = line[length//2:]
        for char in rucksack1:
            if rucksack2.find(char) != -1:
                if char.islower():
                    val = 1 + ord(char) - ord("a")
                else:
                    val = 27 + ord(char) - ord("A")
                total += val
                # print(f"{rucksack1} {rucksack2} {char} {val} {total}")
                break
    return total

def sol2(input):
    total = 0
    tot_lines = len(input)
    for i in range(0, tot_lines, 3):
        rucksack1 = set(input[i][:-1])
        rucksack2 = set(input[i+1][:-1])
        rucksack3 = set(input[i+2][:-1])
        badge = rucksack1.intersection(rucksack2, rucksack3)
        if len(badge) != 1:
            print(f"Wrong badge detection {badge} {rucksack1} {rucksack2} {rucksack3}")
            break
        badge_char = badge.pop()
        if badge_char.islower():
            val = 1 + ord(badge_char) - ord("a")
        else:
            val = 27 + ord(badge_char) - ord("A")
        total += val
    return total

if __name__ == "__main__":
    input = read_input(f"{get_folder_name()}/input")
    print(f"Advent Of Code 2022 - {get_folder_name()}")
    result1 = sol1(input)
    print("First solution is: ", result1)
    result2 = sol2(input)
    print("Second solution is: ", result2)