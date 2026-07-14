import qrcode

link = "https://www.instagram.com/mr_dathu_vicky__04/"

img = qrcode.make(link)
img.save("instagram_qr.png")

print("Instagram QR Code created successfully!")
