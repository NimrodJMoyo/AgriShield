# 🌱 **AgriShield** - AI Powered Agriculture Insights 🌾

Welcome to **AI-Powered Agriculture Insights**, a cutting-edge solution that leverages AI and Machine Learning models to detect **leaf diseases**, **pests**, and **cell towers** through image recognition. This project combines three powerful models to help farmers and agronomists make data-driven decisions, all in real-time.

## 🚀 Project Overview

This repository contains code for utilizing **Roboflow’s inference API** to analyze images and detect potential issues in agriculture, such as:
- **Leaf Diseases** (leaf-disease-nsdsr model)
- **Pests** (pests-2xlvx model)
- **Cell Towers** (cell-towers model)

Each image is processed and results are presented in a **cool, well-formatted HTML report**. This project is designed with modularity in mind, with each dataset API in separate Python files, all working together to create a seamless user experience.

---

## 📂 Project Structure

```bash
├── dataset_api_1.py          # Leaf Disease Detection using the API
├── dataset_api_2.py          # Pests Detection using the API
├── dataset_api_3.py          # Cell Towers Detection using the API
├── generate_report.py        # Generates the HTML report with all results
├── results/                  # Folder to store generated HTML reports
└── README.md                 # This awesome README file
```

## ⚙️ Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/NimrodJMoyo/AgriShield/
    cd AgriShield
    ```

2. **Install dependencies**:
    Ensure you have `inference_sdk` installed:
    ```bash
    pip install inference_sdk
    ```

3. **Add Your Images**:
    Replace the placeholder `your_image.jpg` in the script with the path to your image for each dataset.

---

## 💻 How to Run

Once everything is set up, you can run the detection process using the following steps:


2. **Run Main.py**: Generate the HTML report:

    Generate a consolidated HTML report with the results:
    ```bash
    python main.py
    ```

The results will be stored in the `results/` folder with a timestamp in the filename.

---

## 🖼️ Sample Report

Here’s an example of how the generated HTML report looks:

![Sample Report](sample_report_screenshot.png)

---

## 🧠 AI Models Used

- **Leaf Disease Detection**:
    - Model ID: `leaf-disease-nsdsr/1`
    - Purpose: Detect various diseases affecting plant leaves.

- **Pests Detection**:
    - Model ID: `pests-2xlvx/1`
    - Purpose: Identify pests that are harmful to crops.

- **Cell Towers Detection**:
    - Model ID: `cell-towers/1`
    - Purpose: TBA

---

## 🔒 Security & Privacy Considerations

We value data privacy and security. No personal information is stored, and images processed through the API are used solely for AI inference purposes.

---

## 🤝 Contribution

Contributions are welcome! Feel free to submit a pull request or open an issue if you have ideas on how to improve the project.

---

## 📅 Version History

- **v1.0**: Initial release with detection capabilities for leaf diseases, pests, and cell towers, and automated HTML report generation.

---

## 🛠️ Technologies Used

- **Python 3.8+**
- **Roboflow Inference API**
- **HTML / CSS** for the report formatting

---

## 📧 Contact

Project created and maintained by **Neural Nomads** - nimrodmoyoj@gmail.com.

If you have any questions or suggestions, feel free to reach out!

---

### 🌟 Don't forget to ⭐ this repository if you found it useful!

---
