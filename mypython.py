# import calendar

# # prompt user to enter a year
# year = int(input(" enter a year: "))

# # print the calendar for the entered year
# print(calendar.calendar(year))



# import calendar

# # prompt user to enter a year
# year = int(input("enter a year: "))

# # prompt user to enter a month (by name or number)
# month_input = input("enter a month(name or number, e.g., january or 1): ")

# # convert month name to month number
# month_names = ["January","February","March","April","May","June","July","August","September",
# "October","November","December"]
# if month_input.isdigit():
#     month = int(month_input)
# else:
#     month = month_names.index(month_input.capitalize()) + 1

# # validate month input
# if month < 1 or month > 12:
#     print("invalid month. pls enter a number between 1 and 12 or a valid month name.")
# else:
#     # print the calendar for a entered month and year
#     print(calendar.month(year, month))




# import calendar
# # prompt user to enter a year 
# year = int(input("enter a year:"))

# # prompt user to enter the start and end months (by name or number)
# month_names = ["January","February","March","April","May","June","July","August","September","October",
# "November","December"]

# start_month_input = input("enter start the first month(name or number, e.g., january or 1):")
# end_month_input = input("enter the end month(name or number, e.g., december or 12):")

# # convert month names to month numbers
# if start_month_input.isdigit():
#     start_month = int(start_month_input)
# else:
#     start_month = month_names.index(start_month_input.capitalize()) + 1

# if end_month_input.isdigit():
#     end_month = int(end_month_input)
# else:
#     end_month = month_names.index(end_month_input. capitalize()) + 1

# # validate month input
# if start_month < 1 or start_month > 12 or end_month < 1 or end_month > 12:
#     print("invalid month. please enter a name between 1 and 12 or a valid month name.")
# elif start_month > end_month:
#     print("invalid range. start month should be before end month.")
# else:
#     # print the calendars for the specified range of months
#     for month in range(start_month, end_month + 1):
#       print(calendar.month(year, month))
#       print("\n")


# assignment 2
# import calendar

# def print_calendar():
#     year = int(input("enter a year: "))
#     month_input = input("enter the month (name or number): ")

#     # convert month input to integer if it's a number 
#     if month_input.isdigit():
#         month = int(month_input)
#     else:
#         month = list(calendar.month_name).index(month_input.capitalize())

#     #print the calendar
#     print(f"the calendar for the month of {calendar.month_name[month]} is:")
#     print(calendar.month(year, month))
     
#     print_calendar()


# import os

# def renamer():
#     path = input("enter the path you wish to rename: ")
#     path = path.replace("\\", "/")
#     path = path + "/"
#     i = 0
#     for filename in os.listdir(path):
#         my_source = path + filename
#         my_dest = "IMG" + str(i) + ".jpg"
#         my_dest = path + my_dest
#         os.rename(my_source, my_dest)
#         i += 1
#         print("success! you can now check your folder")

# renamer()


# def print_fibonacci(n):
#     fib_sequence = [0, 1]
#     while len(fib_sequence) < n:
#        fib_sequence.append(fib_sequence[-1] + fib_sequence[-21])
#     print(fib_sequence[:n])


# # prompy user to enter the number of fibonacci numbers
# n = int(input("enter the number of fibonacci number: "))

# # call the funtion to print the fibonacci sequence
# print_fibonacci(n)


# create_dict

# import time 

# def create_lists():
#     list1 = []
#     list2 = []

#     while true:
#         input_value = input("enter an input for list 1: ")
#         list1.append(input_value)
#         if input("Are you through with list 1? (yes/no):")==
# "yes":
#            break
#     while true:
#         input_value = input("enter an input for list 2:? ")
#         list2.append(input_value)
#         if input("Are you through with list 2? (yes/no):") ==
# "yes":
#            break
#     return list1, list2

# def check_lenghts(list1, list2):
#     if len(list1)! = len(list2):
#         print("lenght of the list don't match.")   
#         return false 
#     else:
#         print("lengths match. proceeding...") 
#         time.sleep(1)
#         print(",")
#         time.sleep(1)
#         print(",")
#         time.sleep(1)
#         print(",")
#         return True


# def create_dict():
#     list1, list2 = create_list()
#     if check_lenghts(list1, list2):
#         dictionary = create_dictionary(list1, list2)
#         print(dictionary)

# create_dict()


#fibonacci(n)

# def fibonacci(n, a=0, b=1, fibo=[0, 1]):
#     if len(fibo) == n:
#         return fibo
#     fibo.append(a + b)
#     return fibonacci(n, b, a + b, fibo)

# def main():
#     n = int(input("enter the number of fibonacci numbers to generate:"))
#     f = fibonacci(n)
#     print("fibonacci sequence up to", n, "numbers:")
#     for i in n:
#         print(i)
# #if_name_ == "_main_"
# main()




# def_square()







# def draw_square(size):
#     for i in range(size):
#         for j in range(size):
#             print("* ", end="")
#         print()


# size = int(input("enter square size: "))
# draw_square(size)








# def draw_rectangle(lenght, width):
#     for i in range(lenght):
#         for j in range(width):
#             print("* ", end="")
#         print()

# lenght = int(input("enter rectangle lenght: "))
# width = int(input("enter rectangle width):"))
# draw_rectangle(lenght, width)






# def draw_triangle(size):
#     for i in range(size):
#         for j in range(i):
#             print("* ", end="")
#         print()

# size = int(input("enter triangle size: "))
# draw_triangle(size)


# def_diamond()

# def draw_diamond(size):
#     # upper half
#     for i in range(size):
#         print(" " *(size - i - 1) + "* " * (2*i + 1))
#     # lower half
#     for i in range(size-2, -1, -1):
#         print(" " * (size - i - 1) + "* " * (2*i + 1))

# size = int(input("enter diamond size: "))
# draw_diamond(size)
 





# def draw_diamond(size):
#     # upper half
#     for i in range(size):
#         print(" " *(size - i - 1) + "* " * (2*i + 1))
#     # lower half 
#     for i in range(size-2, -1, -1):
#         print(" " * (size - i - 1) + "* " * (2*i + 1))

# size = int(input("enter diamond size: "))
# draw_diamond(size)



# import random
# import string

# def generate_password(length):
#     characters = string.ascii_letters + string.digits + string.punctuation
#     password = "".join(random.choice(characters) for _ in range(length))
#     return password

# def main():
#     """prompt user for password length and number of passwords."""
#     password_length = int(input("enter password length: "))
#     num_passwords = int(input("enter number of passwords: "))

#     print("/nGenerated passwords: ")
#     for _ in range(num_passwords):
#         print(generate_password(password_length))

# # if _name_ == "_main_":
# main()

# def right_aligned_triangle(n):
#     for i in range(1, n + 1):
#         # print space
#      for j in range(n - i):
#         print(' ', end="")  # two space for better allignment
#         #print asterisks
#     for k in range(i):
#          print("*", end="")
#     print()

# my_num = int(input("enter the number of rows: "))
# right_aligned_triangle(my_num)

rows = 5   
for i in range(rows):
    for j in range(i+1):
        print("* ", end=" ")
    print()