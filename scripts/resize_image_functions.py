import re
import cv2
import pytesseract
from pytesseract import Output

# Crop and resize the photo Resize the photo so that all of the headers are out of the frame
def crop_and_resize(image_path, y=100, h=5000, x=0, w=3440):
    img = cv2.imread(image_path)
    print('Original Dimensions : ', img.shape)
    crop_img = img[y:y + h, x:x + w]  # Numpy Slicing
    imS = cv2.resize(crop_img, global_dim)
    print('Final Dimensions : ', imS.shape)
    cv2.imshow('cropped', imS)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return imS

def crop_and_resize_title_page(image_path, scale_percentage,y=100, h=5000, x=0, w=3440):
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    print('Original Dimensions : ', img.shape)
    width = int(img.shape[1] * scale_percentage / 100)
    width = int(img.shape[1] * scale_percentage / 100)
    height = int(img.shape[0] * scale_percentage / 100)
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    print('Resized Dimensions : ', resized.shape)
    crop_img = resized[y:y + h, x:x + w]
    cv2.imshow("Resized_image", resized)
    cv2.imshow("cropped_image", crop_img)
    print('Resized Dimensions : ', crop_img.shape)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def border_crop_resize(image_path, scale_percentage,y=100, h=5000, x=0, w=3440):
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    print('Original Dimensions : ', img.shape)
    width = int(img.shape[1] * scale_percentage / 100)
    width = int(img.shape[1] * scale_percentage / 100)
    height = int(img.shape[0] * scale_percentage / 100)
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    print('Resized Dimensions : ', resized.shape)
    crop_img = resized[y:y + h, x:x + w]
    cv2.imshow("Resized_image", resized)
    cv2.imshow("cropped_image", crop_img)
    print('Final Dimensions : ', crop_img.shape)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



def get_grayscale(image_path):
    return cv2.cvtColor(image_path, cv2.COLOR_BGR2GRAY)


def canny_edge_detection(image_path):
    image = cv2.imread(image_path)
    cv2.imshow('original_image', image)
    canny = cv2.Canny(image, 100, 200)
    cv2.imshow('canny_edge_detection', canny)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def medianblur(image_path):
    return cv2.medianBlur(image_path, 5)


def thresh_bin(image_path):
    image = cv2.imread(image_path)
    cv2.imshow('original_image', image)
    thresh = cv2.threshold(image, 0, 255,
                           cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    cv2.imshow('thresh_bin', thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return thresh

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
            (x, y, w, h) = (d['left'][i], d['top'][i],
                            d['width'][i], d['height'][i])
            img = cv2.rectangle(
                img, (x, y), (x + w, y + h), (255, 255, 0), 2)
    return img


if __name__ == '__main__':
    canny = get_grayscale('jpegs/a_file_0.jpeg')
    cv2.imshow('img_bounding_boxes_on_words', canny)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

