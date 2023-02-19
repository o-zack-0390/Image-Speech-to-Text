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