


import os
from psd_tools import PSDImage

# Define the grid dimensions
rows = 2  # Number of rows
cols = 2  # Number of columns

# Load the PSD file
psd_file_path = 'finalArtwork.psd'

if not os.path.exists(psd_file_path):
    raise FileNotFoundError(f"The file '{psd_file_path}' does not exist.")

try:
    psd = PSDImage.open(psd_file_path)
except Exception as e:
    raise RuntimeError(f"An error occurred while opening the PSD file: {e}")

# Function to slice the PSD file based on the grid
def slice_psd_with_grid(psd, rows, cols):
    # Calculate the width and height of each slice
    slice_width = psd.width // cols
    slice_height = psd.height // rows

    for row in range(rows):
        for col in range(cols):
            # Calculate the slice boundaries
            left = col * slice_width
            top = row * slice_height
            right = left + slice_width
            bottom = top + slice_height

            # Extract the slice as a new PSDImage object
            slice_layers = psd.layers[:]  # Create a shallow copy of layers
            for layer in slice_layers:
                layer.left -= left
                layer.top -= top
                layer.right -= left
                layer.bottom -= top

            slice_psd = PSDImage(psd.header, layers=slice_layers, use_preview=True)

            # Save the slice as a new PSD file (adjust file path as needed)
            slice_file_path = f'/finalimage/finalImageSliced/Slice_{row}_{col}.psd'
            slice_psd.save(slice_file_path)

# Call the function to slice the PSD file into equal parts based on the grid
slice_psd_with_grid(psd, rows, cols)

