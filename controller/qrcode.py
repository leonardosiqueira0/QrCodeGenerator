import qrcode
from PIL import Image
import io
import streamlit as st


def create_qr_code(data, logo_image=None):
    qr = qrcode.QRCode(
        version = 4,
        error_correction = qrcode.constants.ERROR_CORRECT_H,
        box_size = 10,
        border = 4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    if logo_image:
        logo = Image.open(logo_image).convert("RGBA")
        logo = logo.resize((int(img.size[0] * 0.2), int(img.size[0] * 0.2)))
        bg = Image.new("RGBA", logo.size, (255, 255, 255, 255))
        logo = Image.alpha_composite(bg, logo).convert("RGB")
        img.paste(logo, (img.size[0] // 2 - 50, img.size[1] // 2 - 50))
       
    return img

def download_qr_code(buf):
    st.download_button(
        label="Download QR Code",
        data=buf,
        file_name="qrcode.png",
        mime="image/png"
    )