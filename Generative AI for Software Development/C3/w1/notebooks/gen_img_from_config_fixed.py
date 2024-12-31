import requests
import json
import os

# Load the configuration from the external file
with open('config2.json', 'r') as config_file:
    config = json.load(config_file)

# Extract the API key and URL from the config
api_key = config['api_key']
url = config['url']

# Update headers with the authorization token
headers = config['headers']
headers['Authorization'] = f"Bearer {api_key}"

# Extract the payload from the config
payload = config['payload']

# Send a POST request to the OpenAI API
response = requests.post(url, headers=headers, json=payload)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response JSON
    data = response.json()

    # Extract the URLs of the generated images
    for i, image_data in enumerate(data['data']):
        image_url = image_data['url']
        print(f"Image {i + 1} URL: {image_url}")

        # Download the image and save it locally
        image_response = requests.get(image_url)
        if image_response.status_code == 200:
            filename = f"{config['filename']}{i + 1}.png"
            with open(filename, 'wb') as image_file:
                image_file.write(image_response.content)
            print(f"Image {i + 1} saved as {filename}")
        else:
            print(f"Failed to download image {i + 1}")
else:
    print(f"Failed to generate image: {response.status_code}")
    print(response.text)