def read_input(filename):
    with open(filename) as f:
        input = f.readlines()
    return input

scores1 = {
    "A X": 4,
    "B X": 1,
    "C X": 7,
    "A Y": 8,
    "B Y": 5,
    "C Y": 2,
    "A Z": 3,
    "B Z": 9,
    "C Z": 6,
}

scores2 = {
    "A X": 3,
    "B X": 1,
    "C X": 2,
    "A Y": 4,
    "B Y": 5,
    "C Y": 6,
    "A Z": 8,
    "B Z": 9,
    "C Z": 7,
}

def calculate_strategy (input, scores):
    total = 0
    for line in input:
        val = scores.get(line[:3], 0)
        total += val
        if val == 0:
            print("Found invalid line ", line[:3])
    return total

def sol1(input):
    return calculate_strategy(input, scores1)

def sol2(input):
    return calculate_strategy(input, scores2)

if __name__ == "__main__":
    input = read_input("day02/input")
    result1 = sol1(input)
    print("First solution is: ", result1)
    result2 = sol2(input)
    print("Second solution is: ", result2)