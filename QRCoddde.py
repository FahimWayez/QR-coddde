import qrcode 
from PIL import Image
import matplotlib.pyplot as plt

data = input("Enter the data to encode: ")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)
qr_code = qr.make_image(fill_color="black", back_color="white")

qr_code.save("generated_qr_code.png")

plt.imshow(qr_code)
plt.axis('off')
plt.show()