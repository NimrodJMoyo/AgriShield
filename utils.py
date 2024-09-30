import os
from PIL import Image
import requests
from datetime import datetime

def load_image(image_path):
    """Loads an image from a file or URL."""
    if image_path.startswith('http'):
        response = requests.get(image_path)
        img = Image.open(BytesIO(response.content))
    else:
        img = Image.open(image_path)
    return img

def get_current_timestamp():
    """Returns the current timestamp formatted as YYYYMMDD_HHMMSS."""
    return datetime.now().strftime('%Y%m%d_%H%M%S')

def generate_thumbnail(image_path, thumb_size=(150, 150)):
    """Generate a thumbnail of the image."""
    img = Image.open(image_path)
    img.thumbnail(thumb_size)
    
    thumbnail_path = os.path.splitext(image_path)[0] + "_thumbnail.jpg"
    img.save(thumbnail_path, "JPEG")
    return thumbnail_path

def create_html_report(results):
    """Creates an HTML report formatted with the results of the API inferences for all images."""
    timestamp = get_current_timestamp()
    
    # Start building HTML content
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Inference Report - {timestamp} - ITU Hackathons</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
            }}
            .container {{
                width: 80%;
                margin: auto;
                background-color: white;
                padding: 20px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }}
            h1 {{
                text-align: center;
                color: #333;
            }}
            .section {{
                margin-bottom: 20px;
                border-bottom: 1px solid #ddd;
                padding-bottom: 10px;
            }}
            .section h2 {{
                color: #2c3e50;
            }}
            .section pre {{
                background-color: #f7f7f7;
                padding: 10px;
                border-radius: 5px;
                overflow-x: auto;
            }}
            .thumbnail {{
                width: 150px;
                height: 150px;
                object-fit: cover;
                margin-right: 10px;
                display: inline-block;
            }}
            footer {{
                text-align: center;
                padding: 10px;
                background-color: #333;
                color: white;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>AI Inference Report - {timestamp}</h1>
    """

    # Iterate over the results dictionary and create HTML content for each image
    for img_data in results:
        image_name = img_data['image_name']
        thumbnail_path = img_data['thumbnail_path']
        leaf_result = img_data['leaf_result']
        pests_result = img_data['pests_result']
        cell_towers_result = img_data['cell_towers_result']

        html_content += f"""
        <div class="section">
            <h2>Image: {image_name}</h2>
            <img class="thumbnail" src="{thumbnail_path}" alt="{image_name} thumbnail"/>
            <h3>Leaf Disease Detection</h3>
            <pre>{leaf_result}</pre>
            
            <h3>Pests Detection</h3>
            <pre>{pests_result}</pre>
            
            <h3>Cell Towers Detection</h3>
            <pre>{cell_towers_result}</pre>
        </div>
        """

    # Close the HTML content
    html_content += f"""
        </div>
        <footer>
            <p>Generated on {timestamp} by Neural Nomads</p>
        </footer>
    </body>
    </html>
    """

    # Create results directory if it doesn't exist
    if not os.path.exists("results"):
        os.makedirs("results")
    
    # Create the file name with timestamp
    file_name = f"results/inference_report_{timestamp}.html"
    
    # Write the HTML content to the file
    with open(file_name, 'w') as f:
        f.write(html_content)

    return file_name
