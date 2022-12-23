def read_input(filename):
    with open(filename) as f:
        input = f.read().splitlines()
    return input

def get_folder_name():
    folders = __file__.split('/')
    return folders[-2]

def sol1(input):
    enc_file = [int(x) for x in input]
    working_file = enc_file[:]
    file_len = len(enc_file)
    idx_list = list(range(file_len))
    unique_count = len(set(enc_file))
    # print(unique_count)
    for idx in range(file_len):
        # index = working_file.index(num)
        index = idx_list.index(idx)
        num = working_file[index]
        new_index = (index + num) % (file_len - 1)
        working_file.pop(index)
        working_file.insert(new_index, num)
        idx_list.pop(index)
        idx_list.insert(new_index, idx)
        # print(working_file)
    idx0 = working_file.index(0)
    i1000 = (idx0 + 1000) % file_len
    i2000 = (idx0 + 2000) % file_len
    i3000 = (idx0 + 3000) % file_len
    print(i1000, i2000, i3000)
    # print(working_file)
    return working_file[i1000] + working_file[i2000] + working_file[i3000]

def sol2(input):
    pass

if __name__ == "__main__":
    input = read_input(f"{get_folder_name()}/input")
    print(f"Advent Of Code 2022 - {get_folder_name()}")
    result1 = sol1(input)
    print("First solution is: ", result1)
    result2 = sol2(input)
    print("Second solution is: ", result2)