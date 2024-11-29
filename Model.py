import cv2
import json
from ultralytics import YOLO
# import GPTNaming

# Load the model
model = YOLO("yolo11n.pt")  # Pre-trained YOLO11n model

# Open the video file
input_video_path = '/Volumes/T7/TEMPCOMVIS/Project YOLO/vidvrd-videos-part2/ILSVRC2015_train_00473001.mp4'
cap = cv2.VideoCapture(input_video_path)

# Get video properties
fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define codec and create a VideoWriter object
output_video_path = "output_video.mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

# Set the interval for JSON extraction (e.g., save detections every 3 seconds)
interval_seconds = 3  # Adjust the interval in seconds
frame_interval = int(fps * interval_seconds)  # Number of frames to skip for JSON extraction

# Initialize a list to store detection information
detections = []

# Process the video frame by frame
frame_count = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # Exit the loop if no more frames are available

    # Perform inference on each frame
    results = model(frame)  # YOLO inference

    # Extract detection information only at the specified interval
    if frame_count % frame_interval == 0:
        frame_detections = []
        for detection in results[0].boxes:
            bbox = detection.xyxy.tolist()[0]  # [x_min, y_min, x_max, y_max]
            confidence = float(detection.conf.tolist()[0])  # Confidence score
            class_id = int(detection.cls.tolist()[0])  # Class ID
            class_name = model.names[class_id]  # Class name

            frame_detections.append({
                "confidence": confidence,
                "class_id": class_id,
                "class_name": class_name
            })

        # Add the frame's detection information to the main list
        detections.append({
            "frame": frame_count,
            "fps_time": frame_count / fps,  # Convert frame number to time (in seconds)
            "detections": frame_detections
        })

    # Display the results on the frame
    results_frame = results[0].plot()
    out.write(results_frame)  # Write the frame to the output video

    # Display the frame (optional)
    cv2.imshow("YOLO Inference", results_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit early
        break

    frame_count += 1

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()

# Save detection information to a JSON file
json_output_path = "detections.json"
with open(json_output_path, "w") as json_file:
    json.dump(detections, json_file, indent=4)

print(f"Output video saved as {output_video_path}")
print(f"Detections saved as {json_output_path}")

# GPTNaming()
