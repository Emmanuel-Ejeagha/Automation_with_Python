# this script resizes the size of multiple images
import cv2
import os

def calculate_size(scale_percentage, width, height):
    new_width = int(width * scale_percentage / 100)
    new_height = int(height * scale_percentage / 100)
    print("New Dimensions:", new_width, new_height)
    return (new_width, new_height)


def resize(img_path, scale_percentage, resized_path):
    image = cv2.imread(img_path)
    if image is None:
        print(f"Error: Unable to load image from {img_path}")
        return
    height, width = image.shape[:2]  # Extract height and width
    new_dim = calculate_size(scale_percentage, width, height)
    resized_img = cv2.resize(image, new_dim)
    cv2.imwrite(resized_path, resized_img)
    print(f"Resized image saved as {resized_path}")

images = os.listdir('imageProcessing/img')
for image in images:
    resize(f'imageProcessing/img/{image}', 10, f'resizeImg/resized-{image}')


# imageProcessing/img/012 2.jpeg