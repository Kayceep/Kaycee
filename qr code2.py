import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)

qr.add_data('https://pythonabia.org.ng/')

img = qr.make_image(fill_colour='green', back_colour='white')
img.save("qrcode.jpg")