from PIL import Image

def is_image_empty(image_path):
    # Open the image
    image = Image.open(image_path)

    # Get the bounding box of the non-zero region
    bbox = image.getbbox()

    # Check if the image is empty
    return bbox is None

# Example usage
image_path = 'replace with your image path'
result = is_image_empty(image_path)
print('Is the image empty?', result)
