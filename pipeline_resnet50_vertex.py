from google.cloud import aiplatform
from google.cloud.aiplatform.gapic.schema import predict as predict_pb2
from google.protobuf.json_format import MessageToJson
import json
import numpy as np
import PIL.Image

# Set your project and location information
project_id = "your-project-id"
location = "us-central1"
api_endpoint = f"{location}-aiplatform.googleapis.com"
parent = f"projects/{project_id}/locations/{location}"
model_display_name = "resnet50"

# Authenticate with Vertex AI
aiplatform.init(project=project_id, location=location)

# Load the ResNet50 model
model = aiplatform.Model.list(filter=f"display_name={model_display_name}")[0]

# Set the input image file and label map file
input_image_file = "image.jpg"
label_map_file = "label_map.json"

# Load the input image
input_image = PIL.Image.open(input_image_file)
input_image_np = np.array(input_image)

# Load the label map
with open(label_map_file, "r") as f:
    label_map = json.load(f)

# Convert the input image to a tensor
input_tensor = np.expand_dims(input_image_np, axis=0)

# Set the prediction request parameters
instances_list = [{"input_1": input_tensor.tolist()}]
parameters = predict_pb2.PredictRequest.Parameters()
parameters.mutable_value().CopyFrom(json_format.ParseDict({"confidence_threshold": 0.5}, Value()))

# Send the prediction request to the model
response = model.predict(instances_list, parameters=parameters)

# Convert the prediction response to a JSON string
response_json = MessageToJson(response.predictions)

# Parse the prediction response JSON and print the results
response_dict = json.loads(response_json)
predicted_class_index = np.argmax(response_dict["output_1"][0])
predicted_class_label = label_map[str(predicted_class_index)]
predicted_class_confidence = np.max(response_dict["output_1"][0])
print(f"Predicted class: {predicted_class_label}")
print(f"Confidence: {predicted_class_confidence}")
