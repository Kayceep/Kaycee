import qrcode

data = input("enter the data you want to encode: ")
dest = input(
    "enter the full path destination of where you want your qrcode to be saved: "
)
qr_name = input("enter the name to save the image: ")
dest = dest.replace("\\", "/")
dest = dest + "/" + qr_name + ".png"
img = qrcode.make(data)
img.save(dest)
print("success! you can check the folder for qr code")
