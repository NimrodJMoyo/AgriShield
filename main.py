from leaf_disease import infer_leaf_disease
from pests import infer_pests
from cell_towers import infer_cell_towers
from utils import load_image, save_result

def main():
    image_path = "your_image.jpg"  # I will load the image here, will change it to GUI later

    # Load image
    image = load_image(image_path)

    # Infer from the first dataset (Leaf Disease)
    leaf_disease_result = infer_leaf_disease(image_path)
    print("Leaf Disease Inference Result:", leaf_disease_result)
    save_result(leaf_disease_result, "leaf_disease_result.txt")

    # Infer from the second dataset (Pests)
    pests_result = infer_pests(image_path)
    print("Pests Inference Result:", pests_result)
    save_result(pests_result, "pests_result.txt")

    # Infer from the third dataset (Cell Towers)
    cell_towers_result = infer_cell_towers(image_path)
    print("Cell Towers Inference Result:", cell_towers_result)
    save_result(cell_towers_result, "cell_towers_result.txt")

if __name__ == "__main__":
    main()
