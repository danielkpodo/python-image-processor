from PIL import Image, ImageFilter


def filter_image(image):
    img = Image.open(image)
    img.filter(ImageFilter.GaussianBlur)
    return img.save("filtered_images/blur.png", 'png')


image_path = "./test_images/profile.jpg"
filter_image(image_path)
