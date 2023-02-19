import os
from PIL import Image
import pyocr

cur_dir = "tesseract.exe"

print("exists(): " + str(os.path.exists(cur_dir)))
 
print("isdir(): " + str(os.path.isdir(cur_dir)))
 
print("isfile(): " + str(os.path.isfile(cur_dir)))