import os
import streamlit as st
import pyocr
from PIL import Image


cur_dir = "usr/share/tesseract-ocr"

#"/usr/share/tesseract-ocr"

if st.write("exists(): " + str(os.path.exists(cur_dir))) or st.write("isdir(): " + str(os.path.isdir(cur_dir))) or st.write("isfile(): " + str(os.path.isfile(cur_dir))):
  st.write(os.listdir(cur_dir))

tools = pyocr.get_available_tools()
tool = tools[0]

st.write(tool)

uploaded_file=st.file_uploader("ファイルアップロード", type='jpg')

if uploaded_file:
    
    if st.button("test start"):
      image=Image.open(uploaded_file)

      TESSERACT_PATH = "usr/share/tesseract-ocr"
      TESSDATA_PATH  = "usr/share/tesseract-ocr/4.00/tessdata"

      os.environ['PATH'] += os.pathsep + TESSERACT_PATH
      os.environ["TESSDATA_PREFIX"] = TESSDATA_PATH

      builder = pyocr.builders.TextBuilder(tesseract_layout=6)
      text = tool.image_to_string(image, lang="jpn", builder=builder)

      st.write(text)