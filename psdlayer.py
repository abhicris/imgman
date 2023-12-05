import os
from psd_tools import PSDImage
from PIL import Image

# Load the PSD file
psd_file_path = 'finalArtworklayeredfilled.psd'
if not os.path.exists(psd_file_path):
    raise FileNotFoundError(f"The file '{psd_file_path}' does not exist.")

try:
    psd = PSDImage.open(psd_file_path)
except Exception as e:
    raise RuntimeError(f"An error occurred while opening the PSD file: {e}")

# Function to extract and save all layers as separate image files
def extract_all_layers(psd, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for index, layer in enumerate(psd):
        # Extract the layer as an RGBA image (with transparency preserved)
        layer_image = layer.compose()

        # Save the layer as a PNG file (you can change the format if needed)
        output_file_path = os.path.join(output_directory, f"Layer_{index}.png")
        layer_image.save(output_file_path)

# Usage: Replace '/path/to/output/directory' with the directory where you want to save the extracted layers.
output_directory = '/extract'
extract_all_layers(psd, output_directory)
