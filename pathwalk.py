import cv2
from PIL import Image
import pytesseract
from pdf2image import convert_from_path
import os

pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'


def image_ocr(image_path, output_txt_file_name, All_text):
    image_text = pytesseract.image_to_string(
        image_path, lang='eng+ces', config='--psm 1')
    with open(output_txt_file_name, 'a', encoding='utf-8') as f:
        f.write(image_text)
    with open(All_text, 'a', encoding='utf-8') as f:
        f.write(image_text)


num = 0
year = 1970

year_being_recorded = 'txt_files/' + str(year) + '_article.txt'
cumulative_text = 'txt_files/cumulative.txt'

for foldername, subfolders, filenames in os.walk('articles'):
    for file in filenames:
        if file.endswith('.pdf'):
            article_path = str(foldername) + '/' + str(file)
            pages = convert_from_path(article_path, 500)
            for page in pages:
                name = 'jpegs/a_file_' + str(num) + '.jpeg'
                page.save(name, 'JPEG')
                image_ocr(name, year_being_recorded, cumulative_text)
                num = num + 1
