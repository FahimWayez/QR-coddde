#install pip in your computer if not already installed, and then run the following code in the command prompt
#pip install qrcode[pil]

import qrcode 
from PIL import Image
import re

data = input("Enter the data to encode: ")
sanitizedData = re.sub(r'[\\/:*?"<>|]', '_', data)

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)
qrCode = qr.make_image(fill_color="black", back_color="white")

filename = f"{sanitizedData}.png"
qrCode.save(filename)