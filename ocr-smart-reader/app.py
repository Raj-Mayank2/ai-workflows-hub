import streamlit as st
from ocr import extract_text
from utils.file_loader import save_uploaded_file

st.set_page_config(
    page_title="Smart OCR Reader",
    layout="centered"
)

st.title("📄 Smart OCR Reader")
st.subheader("Typed + Handwritten • Free • CPU-Friendly")

uploaded_file = st.file_uploader(
    "Upload an image (PNG / JPG)",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file:
    file_path = save_uploaded_file(uploaded_file)

    with st.spinner("Running smart OCR..."):
        text = extract_text(file_path)

    st.success("OCR completed")

    st.text_area(
        "Extracted Text",
        value=text,
        height=350
    )
