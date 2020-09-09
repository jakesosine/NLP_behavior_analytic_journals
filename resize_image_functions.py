import cv2


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


crop_and_resize('a_file_0.jpeg')
#resize_then_crop('a_file_0.jpeg', 10)
#border_crop_resize('a_file_3.jpeg', 20)
