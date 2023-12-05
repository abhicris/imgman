import os
from PIL import Image

def is_image_empty(image_path):
    # Open the image
    image = Image.open(image_path)

    # Get the bounding box of the non-zero region
    bbox = image.getbbox()

    # Check if the image is empty
    return bbox is None

# Folder path containing the images
folder_path = 'imagefi/images'

# Counters for empty and non-empty images
empty_count = 0
non_empty_count = 0

# Iterate over files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is an image (optional)
    if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
        # Construct the full file path
        file_path = os.path.join(folder_path, filename)

        # Check if the image is empty
        if is_image_empty(file_path):
            empty_count += 1
        else:
            non_empty_count += 1

# Print the count of empty and non-empty images
print("Empty Images:", empty_count)
print("Non-Empty Images:", non_empty_count)
