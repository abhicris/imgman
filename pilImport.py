from PIL import Image

def is_image_empty(image_path):
    # Open the image
    image = Image.open(image_path)

    # Get the minimum and maximum pixel values
    min_pixel, max_pixel = image.getextrema()

    # Check if the image is empty
    return min_pixel == max_pixel

# Example usage
image_path = 'images/Tesla/Tesla_04.png'
result = is_image_empty(image_path)
print('Is the image empty?', result)
