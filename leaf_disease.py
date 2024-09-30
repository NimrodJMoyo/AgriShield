from inference_sdk import InferenceHTTPClient

def infer_leaf_disease(image_path):
    CLIENT = InferenceHTTPClient(
        api_url="https://detect.roboflow.com",
        api_key="gOcrUpeKl5b5hHXZTpZT"
    )
    result = CLIENT.infer(image_path, model_id="leaf-disease-nsdsr/1")
    return result
