import cv2
#import requests
import io
import json
import os
import PyPDF2

for folderName, subfolders, filenames in os.walk('articles/'):
    print(f'The folder is {folderName})
    print(f'The subfolders in {folderName} are {subfolders}')
    print(f'The subfolders in {folderName} are {filenames}')

    for file in filenames:
        if file.endswith('.png'):
            pdfFile = open(file, 'rb')
            reader = PyPDF2.PdfFileReader(pdfFile)


#            img = cv2.imread(file)
 #           cv2.imshow('img', img)
  #          cv2.waitKey(0)
   #         cv2.destroyAllWindows()


#img = cv2.imread('screenshot2.png')

#height, width, _ = img.shape

# Cutting image
#roi = img[0:height, 400:width]

# ocr
#url_api = 'https://api.ocr.space/parse/image'

#_, compressedimage = cv2.imencode('.jpg', img, [1, 90])
#file_bytes = io.BytesIO(compressedimage)


# results = requests.post(url_api,
#                        files={'screenshot.png': file_bytes},
#                        data={'apikey': 'api_Value'})


#result = results.content.decode()
#result = json.loads(result)

#parsed_results = result.get('ParsedResults')[0]
#text_detected = parsed_results.get('ParsedText')

# with open('data1.txt', 'a+') as file:
#    file.write(text_detected)

#cv2.imshow('roi', roi)
#cv2.imshow('img', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
