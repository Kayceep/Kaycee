# def print_shapes():
#     shapes = {     

#         1: "hour glass",
#         2: "pyramid",
#         3: "left triangle",
#         4: "right triangle",
#         5: "inverted pyramid",
#         6: "double pyramid",
#         7: "inverted double pyramid",
#         8: "diamond"
#     }

#     print("available shapes: ")
#     for key, value in shapes.items():
#         print(f"{key}:  {shapes}")

    
#     choice = int(input("choose a shape (1-8): "))
#     rows = int(input("enter number of rows: "))


#     if choice == 1:
#         #shape 1
#         for i in range(rows):
#             print("* " * (i + 1))
#     elif choice == 2:
#         #shape 2
#         for i in range(rows):
#             print(" " * (rows - i - 1) + "* " * (i + 1))
#     elif choice == 3:
#         #shape 3
#         for i in range(rows):
#             print("* " * (i + 1))
#         for i in range(rows - 2, -1, -1):
#             print("* " * (i + 1))
#     elif choice == 4:
#         #shape 4
#         for i in range(rows):
#             print("* " * rows)
#     elif choice == 5:
#         #shape 5
#         for i in range(rows):
#             print(" " * i + "* " * (rows - i))
#     elif choice == 6:
#         #shape 6
#         for i in range(rows):
#             print(" " * (rows - i -1) + "* " * (2 * i + 1))
#         for i in range(rows - 2, -1, -1):
#             print(" " * (rows - i -1) + "* " * (2 * i + 1))
#     elif choice == 7:
#         #shape 7
#         for i in range(rows):
#             print("* " * (rows - i))
#     elif choice == 8:
#         #shape 8
#         for i in range(rows):
#             print(" " * i + "* " * (rows - i))
#         for i in range(rows -2, -1, -1):
#             print(" " * i + "* " * (rows - i))
#     else:
#         print("invalid choice")

# #     print("what is your name? ")
# #     name = input()
# #     print(f"hi {name}, welcome")

# print_shapes()

#Upper-Half
# for i in range(row, 0, -1):
#     for j in range(row-i):
#         print(" ", end="")
#     for j in range(1, 2*i):
#         print("*", end="")
#     print()

# # Lower-Half
# for i in range(2, row+1):
#     for j in range(row-i):
#         print(" ", end="")
#     for j in range(1, 2*i):
#         print("*", end="")
#     print()

# # open the file in read mode
# file = open('dummytext.txt', 'r')

# # read the entire content of the file 
# line = file.readline()

# # print the content
# print(line)

# # close the file
# file.close()


# import struct

# # define s floating-point number
# x = 23.50

# # pack the float into a binary format
# data = struct.pack('f', x)

# # open the file in binary write mode and write the packed data
# with open('test.bin', 'wb') as f:
#     f.write(data)

# import struct

# # open the file in binary read mode
# with open('test.bin', 'rb') as f:
#     # read the binary data from the file
#     data = f.read()

#     # unpack the binary data to retrieve the float
#     x = struct.unpack('f', data)[0]

#     # print the float value
#     print(x)

# open the file in the read-write mode
with open("dummytext.txt", "r+") as fo:
    # move the read/write pointer to the 10th byte point
    fo.seek(10, 0)

    # read 3 bytes from the current position
    data = fo.read(15)

    # print the read data
    print(data)