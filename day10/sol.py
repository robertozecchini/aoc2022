def read_input(filename):
    with open(filename) as f:
        input = f.read().splitlines()
    return input

def get_folder_name():
    folders = __file__.split('/')
    return folders[-2]

def sol1(input):
    cycle = 0
    x = 1
    val_to_add = 0
    cycles_to_consider = [20, 60, 100, 140, 180, 220]
    results = []
    for line in input:
        x += val_to_add
        val_to_add = 0
        args = line.split()
        if args[0] == "noop":
            cycle += 1
        elif args[0] == "addx":
            cycle += 2
            val_to_add = int(args[1])
        if cycle >= cycles_to_consider[0]:
            results.append(x*cycles_to_consider[0])
            # print(f"{cycles_to_consider[0]} {x} {x*cycles_to_consider[0]}")
            cycles_to_consider.pop(0)
            if len(cycles_to_consider) == 0:
                break
    return sum(results)

def sol2(input):
    pass

if __name__ == "__main__":
    input = read_input(f"{get_folder_name()}/input")
    print(f"Advent Of Code 2022 - {get_folder_name()}")
    result1 = sol1(input)
    print("First solution is: ", result1)
    result2 = sol2(input)
    print("Second solution is: ", result2)