def sol1(input):
    elves = []
    elves.append(0)
    for line in input:
        if line == "\n":
            elves.append(0)
        else:
            elves[-1] += int(line)
    return max(elves)

if __name__ == "__main__":
    filename = "day01/input"
    with open(filename) as f:
        input = f.readlines()
    result = sol1(input)
    print(result)