from ctypes import resize
import qrcode

data = 'Hello! Hi'

# Encoding data to
# qr codedefault code
# img = qrcode.make(data)
# img.save('O:/postProject/QRcode/QR_File/qrcode.png')

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color = 'red', back_color = 'white')
img.save('O:/postProject/QRcode/QR_File/qrcode2.png')

# decoding Qr code
from pyzbar.pyzbar import decode
from PIL import Image

qr_img = Image.open('O:/postProject/QRcode/QR_File/qrcode2.png')
result = decode(qr_img)
print(result)

