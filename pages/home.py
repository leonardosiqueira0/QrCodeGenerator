import streamlit as st
from controller.qrcode import create_qr_code, download_qr_code
import io

def app():
    st.set_page_config(
        page_title="QR Code Generator",
        layout="wide",
        initial_sidebar_state="collapsed",
        menu_items={
            "Get Help": None,
            "Report a bug": None,
            "About": None,
        }
    )

    st.title("QR Code Generator")
    st.write("Welcome to the QR Code Generator!")
    st.write("This application allows you to create QR codes easily.")
    
    input_col, qr_col = st.columns(2, gap="large")
    with input_col:
        st.header("Input")
        data = st.text_input("Enter the data to encode:")
        image = st.file_uploader("Upload a logo image:", type=["png", "jpg", "jpeg"], accept_multiple_files=False)
    with qr_col:
        st.header("QR Code")
        if not data:
            st.warning("Please enter some data to generate a QR code.")
        if data:
            qr_code = create_qr_code(data, image)
            buf = io.BytesIO()
            qr_code.save(buf, format="PNG")
            buf.seek(0)
            st.image(buf)
            download_qr_code(buf)