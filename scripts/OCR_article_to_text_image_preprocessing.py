from PIL import Image
import pytesseract
from pdf2image import convert_from_path
import os
import cv2
# This is the path to tesseract on the device
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'

# Cropping values
y = 200 # This is the value for cropping off the header for page 2-end.
h = 5000 # This encompassess the whole document
x = 0
w = 3440
# Cropping values for first page of the document
y1 = 150
h1 = 5000
x1 = 0
w1 = 3440

#Cropping page 1 function
def crop_page_1(image):
    image = cv2.imread(image)
    img = image[y1:y1 + image.shape[1],
                x1:x1 + image.shape[0]]  # Numpy Slicing
    return img

# Cropping page 2 through end function
def crop_page_2_through_end(image):
    img = cv2.imread(image)
    crop_img = img[y:y + h,
                   x:x + w]  # Numpy Slicing
    return crop_img

# Optical Character Recognition function
def image_ocr(image_path, output_txt_file_name):
    image_text = pytesseract.image_to_string(
        image_path, lang='eng+ces', config='--psm 1')
    with open(output_txt_file_name, 'a', encoding='utf-8') as f:
        f.write(image_text)


article_number = 0 # Starting article value
saved_image_num = 0 # Starting saved image value
text_file = '../txt_files/' + 'article'

# Identifying different files in the directory
for root, dirs, files in os.walk('../articles'):
    for file_ in files:
        if file_.endswith('.pdf'):#Identifying files that end with .pdf
            article_path = str(root) + '/' + str(file_) # Outlining the article path
            pages = convert_from_path(article_path, dpi=300) #Converting to pages Pypdf with 300 dpi
            length_of_article = len(pages)# Length of each article in pages
            print("Length of first article: " + str(length_of_article)) #Check for pages
            page_number = 0# starting page number
            for page in pages: # Looping through pages
                if page_number == 0: #If page is the first page, then use the page one resize function
                    print('Resizing first page and converting to text') # General visual check to establish if the function is working
                    name = '../jpegs/file_' + str(saved_image_num) + '.jpeg'# produce a path for the page
                    page.save(name, 'JPEG') # Save the page as a JPEG
                    img = crop_page_1(name) #Crop the Jpeg image
                    page_number += 1 #Add 1 to page number to track the pages
                    saved_image_num += 1 # Increase saved image number to name next jpeg
                    image_ocr(img, text_file + str(article_number) + '.txt') # Ocr on the image

                else:
                    print('Resizing and converting next page to text')
                    name_ = '../jpegs/file_' + str(saved_image_num) + '.jpeg'
                    page.save(name_, 'JPEG')
                    img1 = crop_page_2_through_end(name_) #Different image cropping
                    saved_image_num += 1
                    page_number += 1
                    image_ocr(img1, text_file + str(article_number) + '.txt')

                    if page_number == length_of_article:#Outlines to change the text file so that over aggregating does not occur
                        print(
                            'Page numbers and length of article matched, changing .txt file for next article')
                        article_number += 1
                        print("Total page numbers recognized: " + str(page_number))
                        page_number = page_number - length_of_article
                        print("Reseting page number to : " + str(page_number))
