# 📦 OCR Text Extraction System

A Streamlit-based OCR Application for Extracting Text from Shipping Labels / Waybills.

## 📘 Project Overview

This project is an OCR-based text extraction system designed to read shipping label / waybill images and automatically extract the target text pattern (Example: `_1_` line).

It is built to handle:

- Real-world label images  
- Skewed or noisy text  
- Blurry images (via preprocessing)  
- Automatic text detection using EasyOCR  
- A clean Streamlit UI to upload and process images  

This repository contains a complete end-to-end OCR pipeline, including preprocessing, OCR engine, pattern extraction, utilities, tests, and Streamlit UI.

---

## 📁 Folder Structure

```
project-root/
├── README.md                # Documentation (this file)
├── requirements.txt         # Python dependencies
├── app.py                   # Streamlit application
├── src/
│   ├── ocr_engine.py        # OCR engine using EasyOCR
│   ├── preprocessing.py     # Image enhancement & cleaning
│   ├── text_extraction.py   # Extracts target line/pattern
│   └── utils.py             # JSON saving, helpers
├── tests/                   # Test cases
├── notebooks/               # Jupyter notebooks for experiments
└── results/                 # Saved outputs/JSON/text
```

---

## 🛠️ Tech Stack & Libraries Used

| Component          | Library        | Purpose                      |
|-------------------|----------------|------------------------------|
| OCR Engine        | EasyOCR        | Extracts text from image     |
| Image Processing  | OpenCV         | Denoise, sharpen, grayscale  |
| UI App            | Streamlit      | Frontend for OCR processing  |
| JSON Handling     | Python json    | Save extracted results       |
| Testing           | pytest         | Validate functions           |

---

# ⚙️ Installation Guide (Step-By-Step)

## 1️⃣ Create Project Directory

Create folder:

```
D:\ocrTask
```

Copy all project files into this folder.

---

## 2️⃣ Create Python Virtual Environment

Open CMD inside the project folder:

```
python -m venv venv
```

---

## 3️⃣ Activate Virtual Environment

```
venv\Scripts\ctivate
```

Your terminal should now show:

```
(venv) D:\ocrTask>
```

---

## 4️⃣ Install All Required Libraries

Install dependencies:

```
pip install -r requirements.txt
```

If any library fails:

```
pip install easyocr
pip install opencv-python
pip install streamlit
pip install numpy
```

---

# ▶️ Running the Streamlit OCR Application

Run the app:

```
python -m streamlit run app.py
```

Streamlit will open at:

```
http://localhost:8501
```

---

# 🖼️ Using the Application (Step-by-Step)

### 1️⃣ Upload Image  
Select an image from:

```
D:\ocrTask\ReverseWayBill```

### 2️⃣ Preview Image  
Uploaded image will be displayed.

### 3️⃣ Run OCR  
Click:

```
Run OCR
```

### 4️⃣ View Output  
- Extracted text pattern will appear  
- JSON output saved inside:

```
results/
```

Example:

```
results/IMG_01.json
```

---

# 🧠 How the Project Works (Internal Flow)

## 🔍 1. preprocessing.py  
Cleans and enhances images:

- Grayscale  
- Noise removal  
- Sharpening  
- Improves blurry text recognition  

---

## 🔎 2. ocr_engine.py  
Handles OCR:

- Loads EasyOCR model  
- Extracts text lines  
- Returns results list  

---

## ✏️ 3. text_extraction.py  
Detects & extracts specific patterns like:

- `_1_`
- `CN_1_`
- `TRK_1_2024`

---

## 📁 4. utils.py  
Utility functions:

- Save JSON  
- File helpers  

---

## 🖥️ 5. app.py  
Controls UI:

- Upload image  
- Run OCR  
- Show results  
- Save output  

This is your main entry-point.

---

# ✔️ Example JSON Output

```
{
  "filename": "sample.jpg",
  "extracted_text": "_1_ CN12345"
}
```

---

# 🧪 Tests (Optional)

Test files go inside:

```
tests/
```

Run:

```
pytest
```

---

# 🎯 Final Notes

✔️ Works with blurry images due to strong preprocessing  
✔️ Simple & modular code structure  
✔️ Production-friendly OCR pipeline  
✔️ Easily expandable (barcode OCR, layout detection, etc.)

---


