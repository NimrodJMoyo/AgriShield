from leaf_disease import infer_leaf_disease
from pests import infer_pests
from cell_towers import infer_cell_towers
from utils import load_image, create_html_report

def main():
    image_path = "your_image.jpg"  # Change this to the path of your image

    # Load image
    image = load_image(image_path)

    # Infer from the first dataset (Leaf Disease)
    leaf_disease_result = infer_leaf_disease(image_path)

    # Infer from the second dataset (Pests)
    pests_result = infer_pests(image_path)

    # Infer from the third dataset (Cell Towers)
    cell_towers_result = infer_cell_towers(image_path)

    # Generate the HTML report and save it
    report_file = create_html_report(leaf_disease_result, pests_result, cell_towers_result)
    
    print(f"Inference report generated and saved as {report_file}")

if __name__ == "__main__":
    main()
