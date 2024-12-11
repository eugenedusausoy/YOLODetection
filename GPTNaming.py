import requests
import json
import os

# OpenAI API details
API_URL = "https://api.openai.com/v1/chat/completions"
MODEL_IDENTIFIER = "gpt-4-turbo"
API_KEY = ""  # Add your API key here

# Path to the JSON file containing detection data
detection_data = 'detections.json'

# Path to the original video
original_video_path = "output_video.mp4"  # Replace with your actual file
output_directory = "renamed_videos"  # Directory to save renamed videos

# Ensure that the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Message to send to ChatGPT
messages = [
    {
        "role": "system",
        "content": "You are an assistant tasked with renaming videos using detection data."
    },
    {
        "role": "user",
        "content": f"Here is the detection data collected from a video: {json.dumps(detection_data)}. Generate a name for this video based on what was detected in it."
                   f" Write the response in JSON format following this structure: {{\"video_name\": \"video name\"}}."
    }
]

# Payload for the API request
payload = {
    "model": MODEL_IDENTIFIER ,
    "messages": messages,
    "temperature": 0.7
}

try:
    # Send the request
    response = requests.post(
        API_URL,
        headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
        json=payload
    )

    # Process GPT's response
    if response.status_code == 200:
        response_data = response.json()
        reply = response_data["choices"][0]["message"]["content"]

        # Parse the JSON response to extract the video name
        video_name_data = json.loads(reply)
        video_name = video_name_data.get("video_name", "Unnamed_Video")

        # Rename and move the video
        renamed_video_path = os.path.join(output_directory, f"{video_name}.mp4")
        os.rename(original_video_path, renamed_video_path)

        print(f"Video renamed and saved as: {renamed_video_path}")

    else:
        print(f"Error: {response.status_code}")
        print(response.json())

except Exception as e:
    print(f"An error occurred: {e}")
