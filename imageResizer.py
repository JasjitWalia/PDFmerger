import cv2
import os

image_path = "C:\\Users\\jasji\\OneDrive\\Pictures\\Saved Pictures\\car1.jpg"
output_path = "C:\\Users\\jasji\\OneDrive\\Pictures\\Saved Pictures\\resized_car1.jpg"
scale_percent = 200

if not os.path.isfile(image_path):
    print(f"Error: {image_path} does not exist or is not a file")
else:
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Failed to load image from {image_path}")
    else:
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized_image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
        cv2.imwrite(output_path, resized_image)
        print(f"Image saved to {output_path}")

