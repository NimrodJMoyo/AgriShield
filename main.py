import os
from leaf_disease import infer_leaf_disease
from pests import infer_pests
from cell_towers import infer_cell_towers
from utils import load_image, create_html_report, generate_thumbnail

def process_images_in_folder(folder_path):
    
    results = []
    
    # Get all image files in the folder
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        
        # Generate thumbnail for the image
        thumbnail_path = generate_thumbnail(image_path)
        
        # Run inference on the image for all models
        leaf_disease_result = infer_leaf_disease(image_path)
        pests_result = infer_pests(image_path)
        cell_towers_result = infer_cell_towers(image_path)
        
        # Collect results for this image
        results.append({
            'image_name': image_file,
            'thumbnail_path': thumbnail_path,
            'leaf_result': leaf_disease_result,
            'pests_result': pests_result,
            'cell_towers_result': cell_towers_result
        })
        print results
    return results

def main():
    folder_path = "Samples"  # The folder where images are stored

    # Process all images in the folder and collect results
    results = process_images_in_folder(folder_path)

    # Generate the HTML report and save it
    report_file = create_html_report(results)
    
    print(f"Inference report generated and saved as {report_file}")

if __name__ == "__main__":
    main()
