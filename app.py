import os
import streamlit as st
import pyocr
from PIL import Image

path               = "/usr/share/tesseract-ocr"
os.environ['PATH'] = os.environ['PATH'] + path
tools              = pyocr.get_available_tools()
tool               = tools[0]
uploaded_file      = st.file_uploader("ファイルアップロード", type='jpg')

if uploaded_file:
    
    if st.button("テキストに変換"):

      image   = Image.open(uploaded_file)
      builder = pyocr.builders.TextBuilder(tesseract_layout = 6)
      text    = tool.image_to_string(image, lang = "jpn", builder = builder)

      with st.expander("Image to Text"):
        st.write(text)
