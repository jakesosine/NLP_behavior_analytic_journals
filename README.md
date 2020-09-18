# JABA Preprocessing and NLP
### Introduction

This project uses optical character recognition to gather written text from the Journal of Applied Behavior Analysis
[tesseract-ocr information](https://github.com/tesseract-ocr/tesseract/wiki)

### Installation
1. Install tesseract to your system
2. Locate and add the path to pytesseract from your system to 
3. Install the required python packages or create a virtual environment and install from requirements.txt

### Description of files and folders
* articles folder is where you will copy and paste articles that will be 
* jpegs - This folder will save each page of a pdf that has been processed. 
* txt_files - this is where the ```.txt``` files will be saved. 
* ```.gitignore``` - file indicates which files will not be uploaded to github.
* ```ocr_space_api.py``` - this is the original interaction using [OCR SPACE API](https://ocr.space/OCRAPI) with a free API key. Pricing models vary based on volume.
* ``OCR_article_to_text.py``` - Use for slow extraction from PDF's in research articles
### How it works
* ....

### Recommended format of pdf files in library
```
articles
├── year1
│   ├── article1.pdf
│   ├── article2.pdf
│   └── article3.pdf
├── year2
│   ├── article1.pdf
│   ├── article2.pdf
│   └── article3.pdf
── year3
│   ├── article1.pdf
│   ├── article2.pdf
│   └── article3.pdf
```
