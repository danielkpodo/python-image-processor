from PIL import Image
import sys
import os

# image_folder = "test_iamges/"
# output_folder = "new/"

image_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(image_folder):
    img = Image.open(f"{image_folder}{filename}")
    cleaned_img = os.path.splitext(filename)[0]
    img.save(f"{output_folder}{cleaned_img}.png", "png")
    print("All files converted")

# print(image_folder, output_folder)
