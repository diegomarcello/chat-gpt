import random
from PIL import Image, ImageDraw, ImageFont


def generate_random_color():
    return random.randint(0, 255)

# Define image size and background color
width, height = 400, 300
bg_color = (generate_random_color(), generate_random_color(), generate_random_color())

# Define text and font
text = "Hello, World!"

font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 28, encoding="unic")


# font = ImageFont.truetype('arial.ttf', 36)

# Create a new image with the specified size and background color
image = Image.new('RGB', (width, height), bg_color)

# Draw the text on the image
draw = ImageDraw.Draw(image)
text_width, text_height = draw.textsize(text, font)
x = (width - text_width) / 2
y = (height - text_height) / 2
draw.text((x, y), text, fill=(0, 0, 0), font=font)

# Save the image to a file
image.save('hello_world.png')
