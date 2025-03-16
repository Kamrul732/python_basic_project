import qrcode

data = input("Enter your URL here: ").strip()
filename = input("Enter your file name: ").strip()

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color='black', back_color='white')
image.save(filename)
print(f'QR code saved as {filename}')