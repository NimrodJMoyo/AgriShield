#A Nimrod Moyo Project
from PIL import Image
import requests
from datetime import datetime
import os

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

def create_html_report(leaf_result, pests_result, towers_result):
    """Creates an HTML report formatted with the results of the API inferences."""
    timestamp = get_current_timestamp()
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Inference Report - {timestamp}</title>
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
            
            <div class="section">
                <h2>Leaf Disease Detection</h2>
                <pre>{leaf_result}</pre>
            </div>
            
            <div class="section">
                <h2>Pests Detection</h2>
                <pre>{pests_result}</pre>
            </div>
            
            <div class="section">
                <h2>Cell Towers Detection</h2>
                <pre>{towers_result}</pre>
            </div>
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
