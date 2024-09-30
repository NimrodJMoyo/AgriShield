from PIL import Image
import requests

def load_image(image_path):
    """Loads an image from a file or URL."""
    if image_path.startswith('http'):
        response = requests.get(image_path)
        img = Image.open(BytesIO(response.content))
    else:
        img = Image.open(image_path)
    return img

def save_result(result, output_path):
    """Saves the result returned by the API."""
    with open(output_path, 'w') as f:
        f.write(str(result))
