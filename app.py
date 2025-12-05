
import streamlit as st
import os
from src.ocr_engine import OCREngine
from src.text_extraction import extract_target_line
from src.utils import save_json

INPUT_DIR = "D:/ocrTask/ReverseWayBill"
OUTPUT_DIR = "results"

st.title("OCR Text Extraction")

uploaded_file = st.file_uploader("Upload a WayBill image", type=["jpg", "png", "jpeg"])

engine = OCREngine(use_gpu=False)


if uploaded_file:
    img_path = os.path.join(INPUT_DIR, uploaded_file.name)

    # Save file in system
    with open(img_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    #st.image(img_path, caption="Uploaded Image", use_column_width=True)
    st.image(img_path, caption="Uploaded Image", width="stretch")


    if st.button("Run OCR"):
        lines = engine.extract_text(img_path)
        target_line = extract_target_line(lines)

        if target_line:
            st.success(f"Extracted Target Text: {target_line}")
        else:
            st.error("Could not find pattern `_1_` in the image.")

        json_path = save_json(OUTPUT_DIR, uploaded_file.name, target_line)
        st.write("📄 JSON Saved at:", json_path)
