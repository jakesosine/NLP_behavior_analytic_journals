from PIL import Image
import pytesseract
from pdf2image import convert_from_path
import os


pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'


def image_ocr(image_path, output_txt_file_name):
    image_text = pytesseract.image_to_string(
        image_path, lang='eng+ces', config='--psm 1')
    with open(output_txt_file_name, 'a', encoding='utf-8') as f:
        f.write(image_text)


article_number = 0
saved_image_num = 0
text_file = 'txt_files/' + 'article'


for root, dirs, files in os.walk('articles'):
    for file_ in files:
        if file_.endswith('.pdf'):
            article_path = str(root) + '/' + str(file_)
            pages = convert_from_path(article_path, 500)
            length_of_article = len(pages)
            page_number = 0
            for page in pages:
                name = 'jpegs/a_file_' + str(saved_image_num) + '.jpeg'
                page.save(name, 'JPEG')
                p += 1
                saved_image_num += 1
                image_ocr(name, text_file + str(article_number) + '.txt')
                if page_number == length_of_article:
                    article_number += 1
