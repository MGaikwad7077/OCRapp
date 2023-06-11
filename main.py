import time
import schedule
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\hp\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
from PIL import Image

def extrat_data():
    img = Image.open('invoice2.png')
    text = tess.image_to_string(img)
    print(text)

usertime = input("Enter a time in the format of hours:minutes")
schedule.every().day.at(usertime).do(extrat_data)

while True:
    schedule.run_pending()
    time.sleep(1)























