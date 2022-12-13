def read_input(filename):
    with open(filename) as f:
        input = f.read().splitlines()
    return input

def get_folder_name():
    folders = __file__.split('/')
    return folders[-2]

class Monkey:
    def __init__(self):
        self.items = []
        self.index = 0
        self.operation = []
        self.divisible = 1
        self.next_true = 0
        self.next_false = 0
        self.inspections_counter = 0
    def play_turn(self, monkeys, worried = False):
        for el in self.items:
            self.inspections_counter += 1
            if self.operation[0] == "old":
                x = el
            else:
                x = int(self.operation[0])
            if self.operation[2] == "old":
                y = el
            else:
                y = int(self.operation[2])
            if self.operation[1] == "+":
                val = x + y
            elif self.operation[1] == "*":
                val = x * y
            else:
                print(f"Invalid operation {self.operation}")
                val = 0
            if worried == False:
                val //= 3
            if val % self.divisible == 0:
                monkeys[self.next_true].items.append(val)
            else:
                monkeys[self.next_false].items.append(val)
        self.items = []


def parse_input(input):
    monkeys = []
    monkey = Monkey()
    for line in input:
        if line.startswith("Monkey "):
            monkey.index = int(line[len("Monkey "):].split(":")[0])
        elif line.startswith("  Starting items: "):
            monkey.items = [int(x) for x in line[len("  Starting items: "):].split(", ")]
        elif line.startswith("  Operation: new = "):
            monkey.operation = line[len("  Operation: new = "):].split()
        elif line.startswith("  Test: divisible by "):
            monkey.divisible = int(line[len("  Test: divisible by "):])
        elif line.startswith("    If true: throw to monkey "):
            monkey.next_true = int(line[len("    If true: throw to monkey "):])
        elif line.startswith("    If false: throw to monkey "):
            monkey.next_false = int(line[len("    If false: throw to monkey "):])
            monkeys.append(monkey)
            monkey = Monkey()
    return monkeys

def sol1(input):
    monkeys = parse_input(input)
    # for monkey in monkeys:
    #     print(monkey.index)
    for round in range (1, 20+1):
        for monkey in monkeys:
            monkey.play_turn(monkeys)
    active_scores = [monkey.inspections_counter for monkey in monkeys]
    active_scores.sort(reverse = True)
    # print(active_scores)
    return active_scores[0] * active_scores[1]


def sol2(input):
    monkeys = parse_input(input)
    # for monkey in monkeys:
    #     print(monkey.index)
    for round in range (1, 10000+1):
        for monkey in monkeys:
            monkey.play_turn(monkeys, worried = True)
    active_scores = [monkey.inspections_counter for monkey in monkeys]
    active_scores.sort(reverse = True)
    # print(active_scores)
    return active_scores[0] * active_scores[1]

if __name__ == "__main__":
    input = read_input(f"{get_folder_name()}/input")
    print(f"Advent Of Code 2022 - {get_folder_name()}")
    result1 = sol1(input)
    print("First solution is: ", result1)
    result2 = sol2(input)
    print("Second solution is: ", result2)