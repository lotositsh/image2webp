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

    # Display progress message
    print(f"Converted: {image_path}")


# Define a function to recursively find image files in directory and subdirectories
def find_images(directory):
    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff')
    images = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(image_extensions):
                images.append(os.path.join(root, file))
    return images

# Prompt for the folder path containing the drawings
image_directory = input("Enter the folder path containing the drawings: \n")

# Find all image files in the specified folder and its subfolders
images = find_images(image_directory)

# Convert each image to webp format and prompt for confirmation to delete the original image files
total_images = len(images)
converted_images = 0
for image in images:
    convert_image(image)
    converted_images += 1
    print(f"Progress: {converted_images}/{total_images} images converted")

# Prompt for confirmation to delete the original image files
delete_original = input("Should I delete the original files? (yes/no): ")
if delete_original.lower() == "yes":
    for image in images:
        os.remove(image)

# Print completion message
print("All images converted to webp format successfully!")