from PIL import Image


def count_pixels(uploaded_file, color: tuple):
    print("Looking for color = ", color)
    img = Image.open(uploaded_file)
    color_dict = {color: count for count, color in img.getcolors()}
    try:
        pixel_count = color_dict[color]
        print(f"{color} found: {pixel_count}")
        return pixel_count
    except KeyError:
        pixel_count = -1
    return pixel_count
