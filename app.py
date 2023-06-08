import os
import streamlit as st
import pyocr
from PIL import Image
import speech_recognition as sr


def main():

  st.markdown("## Image&Speech to Text")

  if st.selectbox("変換方法を選択", ["Image to Text", "Speech to Text"]) == "Image to Text":
    Image_to_Text()

  else:
    Speech_to_Text()



def Image_to_Text():
   
   path               = "/usr/share/tesseract-ocr"
   os.environ['PATH'] = os.environ['PATH'] + path
   tools              = pyocr.get_available_tools()
   tool               = tools[0]
   uploaded_file      = st.file_uploader("ファイルアップロード (.jpg)", type='jpg')
   option = st.selectbox("言語を選択", ["jpn", "eng"])
   
   if uploaded_file:
    
      if st.button("テキストに変換"):

        image   = Image.open(uploaded_file)
        builder = pyocr.builders.TextBuilder(tesseract_layout = 6)

        try:
          text = tool.image_to_string(image, lang = option, builder = builder)

        except:
          st.write("データサイズが無料枠を超過しています. ファイルサイズを小さくしてください")

        else:
          with st.expander("Image to Text"):
            st.write(text)



def Speech_to_Text():

  uploaded_file = st.file_uploader("ファイルアップロード (.wav)", type='wav')
  r             = sr.Recognizer()

  if uploaded_file:

    if st.button("テキストに変換"):
    
      with sr.AudioFile(uploaded_file) as source:
        audio = r.record(source)

      try:
        text = r.recognize_google(audio, language='ja-JP')

      except:
        st.write("データサイズが無料枠を超過しています. ファイルサイズを小さくしてください")

      else:
        with st.expander("Speech to Text"):
          st.write(text)



if __name__ == '__main__':
  main()
