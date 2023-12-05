from PIL import Image
import os
# Load the PNG file
png_file_path = 'filepath.png'
if not os.path.exists(png_file_path):
    raise FileNotFoundError(f"The file '{png_file_path}' does not exist.")

try:
    image = Image.open(png_file_path)
except Exception as e:
    raise RuntimeError(f"An error occurred while opening the PNG file: {e}")

# Define the grid dimensions
rows = 2  # Number of rows
cols = 2  # Number of columns

# Calculate the width and height of each slice
slice_width = image.width // cols
slice_height = image.height // rows

# Function to divide the image into smaller slices
def divide_image(image, rows, cols):
    slices = []
    for row in range(rows):
        for col in range(cols):
            # Calculate the slice boundaries
            left = col * slice_width
            upper = row * slice_height
            right = (col + 1) * slice_width
            lower = (row + 1) * slice_height

            # Crop the image to extract the slice
            slice_image = image.crop((left, upper, right, lower))
            slices.append(slice_image)

    return slices

# Divide the image into slices
image_slices = divide_image(image, rows, cols)

# Create a directory to save the slices (if it doesn't already exist)
output_directory = '/extracted'
os.makedirs(output_directory, exist_ok=True)

# Save each slice as a separate file
for i, slice_image in enumerate(image_slices):
    slice_file_path = os.path.join(output_directory, f"Slice_{i}.png")
    slice_image.save(slice_file_path)
