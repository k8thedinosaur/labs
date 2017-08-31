# file = open("sample.txt", "r")
# contents = file.readlines()
# for line in contents:
#     print(line)
# print(contents)
# file.close()

# from pig import pig_latin


def read_file(file_path):
    with open(file_path, "r") as file:
        contents = file.readlines()
#         for line in contents:
#             print(line)
#     print(contents)

def write_file(file_path, new_lines):
    with open(file_path, "w") as file:
        for line in new_lines:
            file.write(line + "\n")
    # with open(file_path, "w") as file:
    #     times = int(input("How many lines would you like to add? "))
    #     ran = 0
    #     list_of_lines = []
    #     while ran < times:
    #         list_of_lines.append(input("What would you like to add? "))
    #         ran += 1
    #     for line in list_of_lines:
    #         file.write(line + "\n")

def append_to_file(file_path):
    with open(file_path, "a") as file:
        # for line in new_lines:
        #     file.write(line + "\n")
        times = int(input("How many lines would you like to add? "))
        ran = 0
        list_of_lines = []
        while ran < times:
            list_of_lines.append(input("What would you like to add? "))
            ran += 1
        for line in list_of_lines:
            file.write(line + "\n")

# def translate_to_pig_latin(orig_file, dest_file):
#     orig_lines_list = read_file(orig_file)
#     dest_file_lines = []
#     for line in orig_lines_list:
#         new_line = []
#         for word in line.split():
#             new_line.append(pig_latin(word))
#         dest_file_lines.append(" ".join(new_line))
#     write_file(dest_file, dest_file_lines)
#
# orig_file = "sample.txt"
# new_file = "translated_to_pig_latin.txt"
#
#
# translate_to_pig_latin("sample.txt", "translated_to_pig_latin.txt")

for line in read_file(new_file):
    print(line)
# # write_file("sample.txt")
# append_to_file("sample.txt")
# read_file("sample.txt")