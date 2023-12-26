from PIL import Image, ImageDraw, ImageFont
import datetime

# Image dimensions
width = 1500
height = 2000

# Create a black image
image = Image.new('RGB', (width, height), color='black')

# Load the font (replace 'YourFont.ttf' with the path to your font file)
font_path = ['bereal-cover/inter/Inter-Bold.ttf', "bereal-cover/inter/Inter-SemiBoldItalic.otf"]
font_size = [250, 160]
font = [ImageFont.truetype(font_path[0], font_size[0]),ImageFont.truetype(font_path[1], font_size[1]) ]

# Get current year and username
current_year = datetime.datetime.now().year
username =  input('Enter your username:')
# Text to be written
text = [f"BeReal\nRecap\n{current_year}", f"@{username}"]

# Initialize drawing context
draw = ImageDraw.Draw(image)

# Calculate text position
text_x = width // 2  # Center text horizontally
text_y = [height *1.15// 3, 2.55*height // 3]  # Position text at 1/3 of the image height

# Write text on the image
for i in range(2):
    draw.text((text_x, text_y[i]), text[i], fill='white', font=font[i], anchor='mm', align='center',spacing=40)

# Save the image
image.save('bereal-cover/cover.png')

# # Show a preview of the generated image
# image.show()
