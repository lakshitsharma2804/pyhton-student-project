import qrcode
text = input("Enter Text Or Link: ")
qr = qrcode.QRCode()
qr.add_data(text)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
filename = input("Enter File Name: ")
if filename == "":
    filename = "QRCode"
if not filename.endswith(".png"):
    filename = filename + ".png"
img.save(filename)
print("QR Code Generated Successfully!")
