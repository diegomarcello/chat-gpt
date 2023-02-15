import torch
import torchvision
import cv2

# Load the pre-trained model
model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
model.eval()

# Load the image
image_path = "image.jpg"
image = cv2.imread(image_path)

# Convert the image to a tensor
image_tensor = torchvision.transforms.functional.to_tensor(image)

# Make a prediction
prediction = model([image_tensor])[0]

# Get the predicted bounding boxes, labels and scores
boxes = prediction['boxes'].tolist()
labels = prediction['labels'].tolist()
scores = prediction['scores'].tolist()

# Print the results
for i in range(len(scores)):
    print(f"Object {i+1}: {labels[i]} (score: {scores[i]})")
    print(f"Bounding box: {boxes[i]}")
