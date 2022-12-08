def read_input(filename):
    with open(filename) as f:
        input = f.read().splitlines()
    return input

def get_folder_name():
    folders = __file__.split('/')
    return folders[-2]

def search_start_of_packet(datastream):
    for i in range(4, len(datastream)):
        if len(set(datastream[i-4:i])) == 4:
            return i
    return 0

def sol1(input):
    sol = []
    for line in input:
        sol.append(search_start_of_packet(line))
    return sol

def sol2(input):
    pass

if __name__ == "__main__":
    input = read_input(f"{get_folder_name()}/input")
    print(f"Advent Of Code 2022 - {get_folder_name()}")
    result1 = sol1(input)
    print("First solution is: ", result1)
    result2 = sol2(input)
    print("Second solution is: ", result2)