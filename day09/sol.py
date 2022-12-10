def read_input(filename):
    with open(filename) as f:
        input = f.read().splitlines()
    return input

def get_folder_name():
    folders = __file__.split('/')
    return folders[-2]

class Rope:
    def __init__(self):
        self.head_pos = [0, 0]
        self.tail_pos = [0, 0]
        self.history = []
    def translate_dir(self, dir_str):
        if dir_str == "U":
            return (0, 1)
        elif dir_str == "D":
            return (0, -1)
        elif dir_str == "R":
            return (1, 0)
        elif dir_str == "L":
            return (-1, 0)
        else:
            print("pay attention: invalid move")
            return (0,0)
    def move(self, dir_str, steps = 1):
        dir = self.translate_dir(dir_str)
        for i in range(steps):
            self.head_pos = [self.head_pos[0] + dir[0], self.head_pos[1] + dir[1]]
            tail_distance = (self.head_pos[0]-self.tail_pos[0], self.head_pos[1]-self.tail_pos[1])
            if tail_distance[0] == 2:
                self.tail_pos = [self.head_pos[0] - 1, self.head_pos[1]]
            elif tail_distance[0] == -2:
                self.tail_pos = [self.head_pos[0] + 1, self.head_pos[1]]
            elif tail_distance[1] == 2:
                self.tail_pos = [self.head_pos[0], self.head_pos[1] - 1]
            elif tail_distance[1] == -2:
                self.tail_pos = [self.head_pos[0], self.head_pos[1] + 1]
            self.history.append({"head_pos": self.head_pos, "tail_pos": self.tail_pos})
    def get_tails_pos_count(self):
        tail_pos_history = [str(x["tail_pos"]) for x in self.history]
        tail_pos_set = set(tail_pos_history)
        return len(tail_pos_set)

def sol1(input):
    rope = Rope()
    for line in input:
        dir, steps = line.split()
        rope.move(dir, int(steps))
    # print(rope.history)
    return rope.get_tails_pos_count()

def sol2(input):
    pass

if __name__ == "__main__":
    input = read_input(f"{get_folder_name()}/input")
    print(f"Advent Of Code 2022 - {get_folder_name()}")
    result1 = sol1(input)
    print("First solution is: ", result1)
    result2 = sol2(input)
    print("Second solution is: ", result2)