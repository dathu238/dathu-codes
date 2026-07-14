import qrcode

data = input("Enter text or URL: ")

qr = qrcode.make(data)

qr.save("my_qrcode.png")

print("QR Code created successfully!")
