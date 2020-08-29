import cv2
from PIL import Image
import pytesseract
from pdf2image import convert_from_path

pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'
pages = convert_from_path(
    'articles/jaba00083-0015.pdf', 500)


def image_ocr(image_path, output_txt_file_name):
    image_text = pytesseract.image_to_string(
        image_path, lang='eng+ces', config='--psm 1')
    with open(output_txt_file_name, 'a', encoding='utf-8') as f:
        f.write(image_text)


num = 0
for page in pages:

    name = 'jpegs/a_file_' + str(num) + '.jpeg'
    page.save(name, 'JPEG')
    jpegs_path = 'jpegs/a_file_' + str(num) + '.jpeg'
    image_ocr(jpegs_path, '1968_article.txt')
    num = num + 1


#img = cv2.imread('screenshot.png')
#cv2.imshow('img', img)
# cv2.waitKey(0)


#image_ocr('jpegs/file_8.jpeg', 'text.txt')

# print(pytesseract.image_to_string(Image.open('screenshot.png')))


'''

/usr/local/Cellar/tesseract/4.1.1/bin/tesseract
/usr/local/Cellar/tesseract/4.1.1/include/tesseract/ (19 files)
/usr/local/Cellar/tesseract/4.1.1/lib/libtesseract.4.dylib
/usr/local/Cellar/tesseract/4.1.1/lib/pkgconfig/tesseract.pc
/usr/local/Cellar/tesseract/4.1.1/lib/ (2 other files)
/usr/local/Cellar/tesseract/4.1.1/share/tessdata/ (35 files)
'''
