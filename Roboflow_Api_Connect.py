from inference_sdk import InferenceHTTPClient

CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="gOcrUpeKl5b5hHXZTpZT"
)

result = CLIENT.infer(your_image.jpg, model_id="leaf-disease-nsdsr/1")
