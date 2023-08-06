import qrcode,random,os

qr=qrcode.QRCode(version=5,box_size=10,border=1)
inp = input("Please enter data which you want to convert to QR-Code:  ")
qr.add_data(inp)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white")
r= random.randint(0,10000)
img.save(f"qrc{r}.jpeg")
os.startfile(f"qrc{r}.jpeg")