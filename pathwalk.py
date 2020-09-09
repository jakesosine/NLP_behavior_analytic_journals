from PIL import Image
import pytesseract
from pdf2image import convert_from_path
import os

# pytesseract location in homebrew.
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'

# Optical Character Recognition Function
def image_ocr(image_path, output_txt_file_name, All_text):
    image_text = pytesseract.image_to_string(
        image_path, lang='eng+ces', config='--psm 1')
    with open(output_txt_file_name, 'a', encoding='utf-8') as f:
        f.write(image_text)
    with open(All_text, 'a', encoding='utf-8') as f:
        f.write(image_text)


num = 0 # Number for Jpeg File
year = 1974 # Year being recorded for cumulative text


#Path to file for year being recorded
year_being_recorded = 'txt_files/' + str(year) + '_article.txt'
#Path to file for cumulative text
cumulative_text = 'txt_files/cumulative.txt'


#Pathwalk through the directory and retrive all folders, subfulders, and fnames in directory articles
for foldername, subfolders, filenames in os.walk('articles'):
    for file in filenames: # Only considers filenames
        if file.endswith('.pdf'): # outlines that it should end with PDF
            article_path = str(foldername) + '/' + str(file) #Joins article path
            pages = convert_from_path(article_path, 500) #Converts pdf to Python image library format (known as pillow)
            for page in pages: # Loop through each page
                name = 'jpegs/a_file_' + str(num) + '.jpeg' # provide name for saving
                page.save(name, 'JPEG') # save file for records
                image_ocr(name, year_being_recorded, cumulative_text) #Optical character recognition function
                num = num + 1 #add 1 for JPEG filename
