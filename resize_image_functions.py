import re
import cv2
import pytesseract
from pytesseract import Output


y = 0
h = 2500
x = 0
w = 60000
global_dim = (640, 420)
scale_percentage = 20

# Crop and resize the photo Resize the photo an


def crop_and_resize(image_path):
    img = cv2.imread(image_path)
    print('Original Dimensions : ', img.shape)
    crop_img = img[y:y + h, x:x + w]  # Numpy Slicing
    imS = cv2.resize(crop_img, global_dim)
    print('Final Dimensions : ', imS.shape)
    cv2.imshow('cropped', imS)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


y1 = 0
h1 = 250
x1 = 0
w1 = 342


def resize_then_crop(image_path, scale_percentage):
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    print('Original Dimensions : ', img.shape)
    width = int(img.shape[1] * scale_percentage / 100)
    width = int(img.shape[1] * scale_percentage / 100)
    height = int(img.shape[0] * scale_percentage / 100)
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    print('Resized Dimensions : ', resized.shape)
    crop_img = resized[y1:y1 + h1, x1:x1 + w1]
    cv2.imshow("Resized_image", resized)
    cv2.imshow("cropped_image", crop_img)
    print('Resized Dimensions : ', crop_img.shape)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


y2 = 70
h2 = 992 - y2
x2 = 0
w2 = 992


def border_crop_resize(image_path, scale_percentage):
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    print('Original Dimensions : ', img.shape)
    width = int(img.shape[1] * scale_percentage / 100)
    width = int(img.shape[1] * scale_percentage / 100)
    height = int(img.shape[0] * scale_percentage / 100)
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    print('Resized Dimensions : ', resized.shape)
    crop_img = resized[y2:y2 + h2, x2:x2 + w2]
    cv2.imshow("Resized_image", resized)
    cv2.imshow("cropped_image", crop_img)
    print('Final Dimensions : ', crop_img.shape)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# crop_and_resize('a_file_0.jpeg')
#resize_then_crop('a_file_0.jpeg', 10)
#border_crop_resize('a_file_3.jpeg', 20)


def get_grayscale(image_path):
    image = cv2.imread(image_path)
    cv2.imshow('original_image', image)
    gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray_scale_image', gray_scale)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def canny_edge_detection(image_path):
    image = cv2.imread(image_path)
    cv2.imshow('original_image', image)
    canny = cv2.Canny(image, 100, 200)
    cv2.imshow('canny_edge_detection', canny)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def median_Blur(image_path):
    image = cv2.imread(image_path)
    cv2.imshow('original_image', image)
    median_Blur = cv2.medianBlur(image, 5)
    cv2.imshow('medianBlur', median_Blur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def thresh_bin(image_path):
    image = cv2.imread(image_path)
    cv2.imshow('original_image', image)
    thresh = cv2.threshold(image, 0, 255,
                           cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    cv2.imshow('thresh_bin', thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Takes a while


def bounding_boxes_letters(image_path):
    image = cv2.imread(image_path)
    h, w, c = image.shape
    boxes = pytesseract.image_to_boxes(image)
    for b in boxes.splitlines():
        b = b.split(' ')
        image = cv2.rectangle(image,
                              (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)
    return image


def bounding_boxes_to_words(image_path):
    img = cv2.imread(image_path)
    d = pytesseract.image_to_data(img, output_type=Output.DICT)
    n_boxes = len(d['text'])
    for i in range(n_boxes):
        if int(d['conf'][i]) > 60:
            (x, y, w, h) = (d['left'][i], d['top']
                            [i], d['width'][i], d['height'][i])
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return img


img = bounding_boxes_to_words('jpegs/a_file_1278.jpeg')
cv2.imshow('img_bounding_boxes_on_words', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#n_boxes = len(d['text'])

# bounding_boxes('jpegs/a_file_1278.jpeg')


# thresh_bin('jpegs/a_file_1278.jpeg')

# median_Blur('jpegs/a_file_1278.jpeg')
# canny_edge_detection('jpegs/a_file_1278.jpeg')

# get_grayscale('jpegs/a_file_1278.jpeg')
