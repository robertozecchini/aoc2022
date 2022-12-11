def read_input(filename):
    with open(filename) as f:
        input = f.read().splitlines()
    return input

def get_folder_name():
    folders = __file__.split('/')
    return folders[-2]

class Rope:
    def __init__(self):
        self.knots = 10
        self.head_pos = [0, 0]
        self.tail_pos = [0, 0]
        self.tails_pos = []
        for i in range(self.knots):
            self.tails_pos.append([0, 0])
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
    def sign(self, i):
        if i > 0:
            return 1
        elif i < 0:
            return -1
        else:
            return 0
    def get_tail_position(self, head_pos, tail_pos):
        x_dist = head_pos[0] - tail_pos[0]
        y_dist = head_pos[1] - tail_pos[1]
        if abs(x_dist) == 2 or abs(y_dist) == 2:
            return [tail_pos[0] + self.sign(x_dist), tail_pos[1] + self.sign(y_dist)]
        else:
            return tail_pos
    def move(self, dir_str, steps = 1):
        dir = self.translate_dir(dir_str)
        for i in range(steps):
            self.head_pos = [self.head_pos[0] + dir[0], self.head_pos[1] + dir[1]]
            self.tails_pos[0] = self.head_pos
            for t in range(1, self.knots):
                self.tails_pos[t] = self.get_tail_position(self.tails_pos[t-1], self.tails_pos[t])
            self.tail_pos = self.tails_pos[1]
            status = {}
            status["head_pos"] = self.head_pos
            status["tail_pos"] = self.tail_pos
            for t in range(self.knots):
                status[f"tail{t}_pos"] = self.tails_pos[t]
            self.history.append(status)
    def get_tail_positions_count(self, tail_num = 1):
        tail_pos_history = [str(x[f"tail{tail_num}_pos"]) for x in self.history]
        tail_pos_set = set(tail_pos_history)
        return len(tail_pos_set)

def sol1(input):
    rope = Rope()
    for line in input:
        dir, steps = line.split()
        rope.move(dir, int(steps))
    return rope.get_tail_positions_count()

def sol2(input):
    rope = Rope()
    for line in input:
        dir, steps = line.split()
        rope.move(dir, int(steps))
    return rope.get_tail_positions_count(9)

if __name__ == "__main__":
    input = read_input(f"{get_folder_name()}/input")
    print(f"Advent Of Code 2022 - {get_folder_name()}")
    result1 = sol1(input)
    print("First solution is: ", result1)
    result2 = sol2(input)
    print("Second solution is: ", result2)