from PIL import Image


def image_resizer(img, width, height):
    try:
        current_img = Image.open(img)
        current_img.thumbnail((width, height))
        return current_img.save("./filtered_images/thumbnail.png")
    except FileNotFoundError as err:
        return err


img_location = "./test_images/wallpapertip_wallpaper-work_1736843.jpg"
image_resizer(img_location, 400, 400)
