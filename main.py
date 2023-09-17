from PIL import Image
import tkinter as tk
from tkinter import filedialog


def add_watermark(input_image_path, watermark_image_path, output_image_path, where):

    try:
        base_image = Image.open(input_image_path)
    except:
        print("Please, select a valid image.")
        return True

    try:
        watermark_image = Image.open(watermark_image_path)
    except:
        print("Please, select a valid image.")
        return True

    width, height = base_image.size
    watermark_width , watermark_height = watermark_image.size

    if width < watermark_width or height < watermark_height:
        print("The waterkmark selected is bigger than the image.")
        return True

    position = calculate_position(where, width, height, watermark_width, watermark_height)

    output_image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    output_image.paste(base_image, (0, 0))
    output_image.paste(watermark_image, position, mask=watermark_image)
    output_image.show()
    output_image.save(output_image_path)
    return False


def calculate_position(where, base_width, base_height, watermark_width, watermark_height):

    if where == "1":
        return 5, 5
    elif where == "2":
        return int((base_width - watermark_width) / 2), 5
    elif where == "3":
        return base_width - watermark_width - 5, 5
    elif where == "4":
        return 5, int((base_height- watermark_height) / 2)
    elif where == "5":
        return int((base_width - watermark_width) / 2), int((base_height- watermark_height) / 2)
    elif where == "6":
        return base_width - watermark_width - 5, int((base_height- watermark_height) / 2)
    elif where == "7":
        return 5, base_height - watermark_height - 5
    elif where == "8":
        return int((base_width - watermark_width) / 2), base_height - watermark_height - 5
    elif where == "9":
        return base_width - watermark_width - 5, base_height - watermark_height - 5
    else:
        return base_width - watermark_width - 5, base_height - watermark_height - 5


root = tk.Tk()
root.withdraw()

retry_on_error = True

while retry_on_error:
    print("Please, select the image you want to watermark.")
    image_to_watermark = filedialog.askopenfilename()

    print("Please, select the watermark.")
    watermark = filedialog.askopenfilename()

    print("""
    1   2   3
    4   5   6
    7   8   9
    """)
    pos_chosen = input("Where do you want the watermark? Type a number from 1 to 9 (default = 9). ")

    retry_on_error = add_watermark(image_to_watermark, watermark, "Result.png", pos_chosen)

