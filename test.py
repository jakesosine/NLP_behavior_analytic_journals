from PIL import Image
import pytesseract
from pdf2image import convert_from_path
import os
import cv2

pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'

y = 200
h = 5000
x = 0
w = 3440

y1 = 150
h1 = 5000
x1 = 0
w1 = 3440


def crop_page_1(image):
    image = cv2.imread(image)
    img = image[y1:y1 + image.shape[1],
                x1:x1 + image.shape[0]]  # Numpy Slicing
    return img


def crop_page_2_through_end(image):
    img = cv2.imread(image)
    crop_img = img[y:y + h,
                   x:x + w]  # Numpy Slicing
    return crop_img


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
            pages = convert_from_path(article_path, dpi=300)
            length_of_article = len(pages)
            print(length_of_article)
            page_number = 0
            for page in pages:
                if page_number == 0:
                    print('in if condition')
                    name = 'jpegs/file_' + str(saved_image_num) + '.jpeg'
                    page.save(name, 'JPEG')
                    img = crop_page_1(name)
                    page_number += 1
                    saved_image_num += 1
                    image_ocr(img, text_file + str(article_number) + '.txt')

                else:
                    print('in elif condition')
                    name_ = 'jpegs/file_' + str(saved_image_num) + '.jpeg'
                    page.save(name_, 'JPEG')
                    img1 = crop_page_2_through_end(name_)
                    saved_image_num += 1
                    page_number += 1
                    image_ocr(img1, text_file + str(article_number) + '.txt')

                    if page_number == length_of_article:
                        print('in else condition')
                        article_number += 1
                        print(page_number)
                        page_number = page_number - length_of_article
                        print(page_number)
