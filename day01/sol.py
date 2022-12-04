def read_elves_calories(input):
    elves = []
    elves.append(0)
    for line in input:
        if line == "\n":
            elves.append(0)
        else:
            elves[-1] += int(line)
    return elves

def sol1(input):
    elves = read_elves_calories(input)
    return max(elves)

def sol2(input):
    elves = read_elves_calories(input)
    elves.sort()
    return sum(elves[-3:])

if __name__ == "__main__":
    filename = "day01/input"
    with open(filename) as f:
        input = f.readlines()
    result1 = sol1(input)
    print("First solution is: ", result1)
    result2 = sol2(input)
    print("Second solution is: ", result2)