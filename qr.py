# import qrcode
# data = input("enter the data you want to encode: ")
# dest = input(
#     "enter the full path destination of where you want your qrcode to be saved: "
# )
# qr_name = input("enter the name to save the image: ")
# dest = dest.replace("\\", "/")
# dest = dest + "/" + qr_name + ".png"
# img = qrcode.make(data)
# img.save(dest)
# print("success! you can check the folder for qrcode")



import qrcode

list1 = input("enter the data you want to encode: ")
dest = input("enter the file path destination of where you want your qrcode saved: ")
qr_name = input ("enter the name to save the image: ")
list2 = input(fback_colour(["1 : green"], ["2 : blue"], ["3 : black"], ["4 : white"], ["5 : yellow"], ["6 :pink"]))
list3 = input("choose the back colour you want from the numbers: ")
list4 = input(ffill_colour(["white"], ["black"] ["purple"], ["yellow"], ["pink"], ["green"]))
dest = dest.replace("\\", "/")
dest = dest + "/" + qr_name + ".png"
img = qrcode.make(["list1"], ["list2"], ["list3"], ["list4"], ["list5"], ["list6"])
img.save(dest)
print("transaction successfully! check ur folder now")


