def read_input(filename):
    with open(filename) as f:
        input = f.read().splitlines()
    return input

def get_folder_name():
    folders = __file__.split('/')
    return folders[-2]

def search_start_of_packet(datastream, marker_len = 4):
    for i in range(marker_len, len(datastream)):
        if len(set(datastream[i-marker_len:i])) == marker_len:
            return i
    return 0

def sol1(input):
    sol = []
    for line in input:
        sol.append(search_start_of_packet(line))
    return sol

def sol2(input):
    sol = []
    for line in input:
        sol.append(search_start_of_packet(line, 14))
    return sol

if __name__ == "__main__":
    input = read_input(f"{get_folder_name()}/input")
    print(f"Advent Of Code 2022 - {get_folder_name()}")
    result1 = sol1(input)
    print("First solution is: ", result1)
    result2 = sol2(input)
    print("Second solution is: ", result2)