from inference_sdk import InferenceHTTPClient

def infer_cell_towers(image_path):
    CLIENT = InferenceHTTPClient(
        api_url="https://detect.roboflow.com",
        api_key="eKK3oVUEFpdvYVIyng0b"
    )
    result = CLIENT.infer(image_path, model_id="cell-towers/1")
    return result
