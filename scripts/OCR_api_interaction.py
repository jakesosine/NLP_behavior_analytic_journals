import cv2
import requests
import io
import json
import os
# API found free at https://ocr.space/
# No affiliation to ocr.space

api_value = 'key'  # Enter your own API Key


img = cv2.imread('screenshot2.png')

# defining image height and width by using img.shape
height, width, _ = img.shape

# Cutting image
roi = img[0:height, 400:width]

# OCR API
url_api = 'https://api.ocr.space/parse/image'
# Outlining the compressed image and then converting it to bytes using IO package
_, compressedimage = cv2.imencode('.jpg', img, [1, 90])
file_bytes = io.BytesIO(compressedimage)

# Sending post request to API
results = requests.post(url_api,
                        files={'screenshot.png': file_bytes},
                        data={'apikey': api_Value})


result = results.content.decode()
result = json.loads(result)

parsed_results = result.get('ParsedResults')[0]
text_detected = parsed_results.get('ParsedText')

with open('data1.txt', 'a+') as file:
    file.write(text_detected)

cv2.imshow('roi', roi)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
