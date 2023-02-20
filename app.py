import os
import streamlit as st
import pyocr
from PIL import Image
import speech_recognition as sr


def main():

  st.markdown("## Image&Speech to Text")

  if st.selectbox("変換方法を選択", [ "Image to Text", "Speech to Text"]) == "Image to Text":
    Image_to_Text()

  else:
    Speech_to_Text()



def Image_to_Text():
   
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



def Speech_to_Text():

  uploaded_file = st.file_uploader("ファイルアップロード", type='wav')
  r             = sr.Recognizer()
  
  with sr.AudioFile(uploaded_file) as source:
    audio = r.record(source)
    
  with st.expander("Speech to Text"):
    st.write(r.recognize_google(audio, language='ja-JP'))



if __name__ == '__main__':
  main()
