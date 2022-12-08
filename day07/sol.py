def read_input(filename):
    with open(filename) as f:
        input = f.read().splitlines()
    return input

def get_folder_name():
    folders = __file__.split('/')
    return folders[-2]

def add_dir_to_path(path, dir):
    if path == "/":
        path += dir
    else:
        path += "/" + dir
    return path

def get_directories(input):
    dirs = {"/":0}
    path = ""
    for line in input:
        args = line.split()
        if line.startswith("$ cd "):
            if args[2] == "/":
                path = "/"
            elif args[2] == "..":
                if path == "/":
                    print("invalid cmd '" + line + "' when path='" + path + "'")
                else:
                    path = "/".join(path.split("/")[:-1])
            else:
                path = add_dir_to_path(path, args[2])
        elif line.startswith("dir"):
            dirs[add_dir_to_path(path, args[1])] = 0
        elif args[0].isnumeric():
            dirs_list = path.split("/")
            d_path = ""
            for d in dirs_list[:]:
                d_path = add_dir_to_path(d_path, d)
                dirs[d_path] += int(args[0])
    return dirs

def sol1(input):
    dirs = get_directories(input)
    # print(dirs)
    total = 0
    for path, size in dirs.items():
        if size < 100000:
            total += size
    return total

def sol2(input):
    pass

if __name__ == "__main__":
    input = read_input(f"{get_folder_name()}/input")
    print(f"Advent Of Code 2022 - {get_folder_name()}")
    result1 = sol1(input)
    print("First solution is: ", result1)
    result2 = sol2(input)
    print("Second solution is: ", result2)