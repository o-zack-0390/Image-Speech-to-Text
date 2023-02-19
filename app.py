import os
import streamlit as st
import pyocr
from PIL import Image


cur_dir = "tesseract.exe"

st.write("exists(): " + str(os.path.exists(cur_dir)))
 
st.write("isdir(): " + str(os.path.isdir(cur_dir)))
 
st.write("isfile(): " + str(os.path.isfile(cur_dir)))

tools = pyocr.get_available_tools()
tool = tools[0]

st.write(tool)

uploaded_file=st.file_uploader("ファイルアップロード", type='jpg')

if uploaded_file:
    
    if st.button("test start"):
      image=Image.open(uploaded_file)

      builder = pyocr.builders.TextBuilder(tesseract_layout=6)
      text = tool.image_to_string(img, lang="jpn", builder=builder)

      st.write(text)