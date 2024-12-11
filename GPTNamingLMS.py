import requests
import json
import os
import shutil

# Local LLM API details
API_URL = "http://127.0.0.1:1234/v1/chat/completions"

# Path to the JSON file containing detection data
detection_data_path = 'detections.json'

# Load detection data
try:
    with open(detection_data_path, 'r') as f:
        detection_data = json.load(f)
except FileNotFoundError:
    detection_data = {}

# Path to the original video
original_video_path = "output_video.mp4"

# Directory to save renamed videos
output_directory = "renamed_videos"
os.makedirs(output_directory, exist_ok=True)

# Crafted prompt to force JSON output
messages = [
    {
        "role": "system",
        "content": """You are an AI assistant specialized in generating precise JSON output. 
        You MUST follow these strict rules:
        1. ONLY respond with a valid JSON object
        2. The JSON MUST have exactly this structure: {"video_name": "string"}
        3. The video_name should be a concise, descriptive name based on the most prominent objects detected
        4. DO NOT include any additional text, explanation, or commentary
        5. Ensure the JSON is properly formatted
        6. If no clear objects are detected, do NOT generate a name
        7. Use lowercase, underscore-separated words
        8. Maximum length of video_name is 30 characters"""
    },
    {
        "role": "user",
        "content": f"Analyze these detection results and generate a precise video name in JSON format: {json.dumps(detection_data)}"
    }
]

# Payload for the API request
payload = {
    "messages": messages,
    "temperature": 0.3,
    "max_tokens": 50,
}

try:
    # Send the request to local LLM
    response = requests.post(
        API_URL,
        headers={"Content-Type": "application/json"},
        json=payload
    )

    # Process LLM's response
    if response.status_code == 200:
        response_data = response.json()

        # Extract the content from the response
        full_response = response_data['choices'][0]['message']['content']

        # Attempt to parse the video name
        try:
            video_name_data = json.loads(full_response)
            video_name = video_name_data.get("video_name", None)
        except json.JSONDecodeError:
            # If direct parsing fails, try extracting the content inside quotes
            import re

            match = re.search(r'"video_name"\s*:\s*"([^"]*)"', full_response)
            video_name = match.group(1) if match else None

        # If no valid name found, copy the original video without renaming
        if not video_name:
            print("No valid name generated. Copying original video.")
            shutil.copy2(original_video_path,
                         os.path.join(output_directory, os.path.basename(original_video_path)))
            print(f"Video copied as: {os.path.join(output_directory, os.path.basename(original_video_path))}")
        else:
            # Rename and move the video
            renamed_video_path = os.path.join(output_directory, f"{video_name}.mp4")
            shutil.copy2(original_video_path, renamed_video_path)
            print(f"Video renamed and saved as: {renamed_video_path}")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

except requests.exceptions.ConnectionError:
    print("Error: Could not connect to the local LLM. Ensure LM Studio is running on 127.0.0.1:1234")
except Exception as e:
    print(f"An unexpected error occurred: {e}")