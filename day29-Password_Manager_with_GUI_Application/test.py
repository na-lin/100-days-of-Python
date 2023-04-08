# with open("test.txt",mode='a') as file:
#     file.write("\nnew line")

#
# with open("data.txt") as file:
#     data = file.read()
#     if "SJDKF" in data:
#         print("exist")
#
# print(type(data))
# print(data)

# str = "fds | test@gmail.com | fdsf"
# str_list = str.split(" | ")
# print(str_list)
with open("test.txt") as file:
    lines = file.readlines()
    print(lines)
with open("test.txt",mode='w') as file:
    for line in lines:
        if 'E\n'!= line:
            file.write(line)



