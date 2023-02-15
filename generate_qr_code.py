# pip install qrcode

import qrcode

qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Clique aqui agora!')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("qr_code.png")
