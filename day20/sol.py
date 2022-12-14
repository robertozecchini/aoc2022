def read_input(filename):
    with open(filename) as f:
        input = f.read().splitlines()
    return input

def get_folder_name():
    folders = __file__.split('/')
    return folders[-2]

def mix(enc_file, n):
    working_file = enc_file[:]
    file_len = len(enc_file)
    idx_list = list(range(file_len))
    unique_count = len(set(enc_file))
    for i in range(n):
        for idx in range(file_len):
            # index = working_file.index(num)
            index = idx_list.index(idx)
            num = working_file[index]
            new_index = (index + num) % (file_len - 1)
            working_file.pop(index)
            working_file.insert(new_index, num)
            idx_list.pop(index)
            idx_list.insert(new_index, idx)
    return working_file

def get_grove(l):
    idx0 = l.index(0)
    file_len = len(l)
    i1000 = (idx0 + 1000) % file_len
    i2000 = (idx0 + 2000) % file_len
    i3000 = (idx0 + 3000) % file_len
    # print(i1000, i2000, i3000)
    # print(working_file)
    return l[i1000], l[i2000], l[i3000]

def sol1(input):
    enc_file = [int(x) for x in input]
    mixed_file = mix(enc_file, 1)
    grove_coordinates = get_grove(mixed_file)
    return sum(grove_coordinates)

def sol2(input):
    enc_key = 811589153
    enc_file = [int(x)*enc_key for x in input]
    mixed_file = mix(enc_file, 10)
    grove_coordinates = get_grove(mixed_file)
    return sum(grove_coordinates)

if __name__ == "__main__":
    input = read_input(f"{get_folder_name()}/input")
    print(f"Advent Of Code 2022 - {get_folder_name()}")
    result1 = sol1(input)
    print("First solution is: ", result1)
    result2 = sol2(input)
    print("Second solution is: ", result2)