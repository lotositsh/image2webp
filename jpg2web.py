# Import necessary libraries
import os
from PIL import Image

# Define a function to convert images to webp format
def convert_image(image_path):
    # Open image
    im = Image.open(image_path)

    # Convert image to RGB format
    im = im.convert('RGB')

    # Get image name and extension
    image_name, image_ext = os.path.splitext(image_path)

    # Save image in webp format
    im.save(f"{image_name}.webp", 'webp')

# Get all files in current directory
files = os.listdir()

# Filter out all image files
images = [file for file in files if file.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff'))]

# Convert each image to webp format
for image in images:
    convert_image(image)

# Print success message
print("All images converted to webp format successfully!")
