from PIL import Image
import pytesseract
from pdf2image import convert_from_path

##########################################################################################
#                                                                                        #
#                             Tesseract Documentation Link                               #
#                    https://github.com/tesseract-ocr/tesseract/wiki                     #
#          run this command to install from homebrew = brew install tesseract            #
#                                                                                           #
#                                                                                        #
#                                                                                        #
#                                                                                        #
#                                                                                        #
##########################################################################################

# defining directory for tesseract
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'

# define a function that converts a pdf from an image path to an output text file


def image_ocr(image_path, output_txt_file_name):
    image_text = pytesseract.image_to_string(
        image_path, lang='eng+ces', config='--psm 1')
    with open(output_txt_file_name, 'a', encoding='utf-8') as f:
        f.write(image_text)


# Outlining path to pdf file
pages = convert_from_path('articles/test_article/test_article.pdf', 500)

num = 0
for page in pages:
    print(len(pages))
    name = 'jpegs/a_file_' + str(num) + '.jpeg'
    page.save(name, 'JPEG')
    jpegs_path = 'jpegs/a_file_' + str(num) + '.jpeg'
    image_ocr(jpegs_path, 'txt_files/sample_text/sample_article.txt')
    num = num + 1
