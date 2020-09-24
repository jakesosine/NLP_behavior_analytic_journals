from PIL import Image
import pytesseract
from pdf2image import convert_from_path
import os
import cv2

pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'

y = 350
h = 5000
x = 0
w = 3440
scale_percentage = 20


def image_ocr(image_path, output_txt_file_name):
    image_text = pytesseract.image_to_string(
        image_path, lang='eng+ces', config='--psm 1')
    with open(output_txt_file_name, 'a', encoding='utf-8') as f:
        f.write(image_text)


y1 = 230
h1 = 5000
x1 = 0
w1 = 3440


def crop_page_1(image_path):
    img = cv2.imread(image_path)
    img = cv2.medianBlur(img, 5)
    cv2.imshow('canny_edge_detection', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    crop_img = img[y1:y1 + img.shape[1], x1:x1 + img.shape[0]]  # Numpy Slicing
    return crop_img


img = (crop_page_1('jpegs/a_file_11.jpeg'))


def crop_and_resize_page_2_through_end(image_path):
    img = cv2.imread(image_path)
    print('Original Dimensions : ', img.shape)
    crop_img = img[y:y + img.shape[1], x:x + img.shape[0]]  # Numpy Slicing
    return crop_img


#img = crop_and_resize('jpegs/a_file_5.jpeg')
image_ocr(img, 'txt_files/' + 'article_test' + '.txt')
