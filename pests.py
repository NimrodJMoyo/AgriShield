from inference_sdk import InferenceHTTPClient

def infer_pests(image_path):
    CLIENT = InferenceHTTPClient(
        api_url="https://detect.roboflow.com",
        api_key="N01BkY5VfChlz3IyI08w"
    )
    result = CLIENT.infer(image_path, model_id="pests-2xlvx/1")
    return result
