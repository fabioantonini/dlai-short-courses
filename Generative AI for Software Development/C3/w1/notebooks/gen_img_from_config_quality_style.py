import requests
import json
import os

def load_config(file_path):
    """Load configuration from a JSON file."""
    with open(file_path, 'r') as file:
        return json.load(file)

def validate_parameters(payload):
    """Validate style and quality parameters."""
    valid_styles = ['vivid', 'natural']
    valid_qualities = ['standard', 'hd']
    
    style = payload.get('style')
    quality = payload.get('quality')

    if style not in valid_styles:
        raise ValueError(f"Invalid style: {style}. Valid options are {valid_styles}.")
    
    if quality not in valid_qualities:
        raise ValueError(f"Invalid quality: {quality}. Valid options are {valid_qualities}.")

def generate_image(config):
    """Generate an image using the OpenAI API."""
    url = config['url']
    headers = config['headers']
    headers['Authorization'] = f"Bearer {config['api_key']}"
    payload = config['payload']
    
    # Validate parameters
    validate_parameters(payload)
    
    timeout = config.get('timeout', 10)  # Default to 10 seconds if not specified

    # Send a POST request to the OpenAI API
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=timeout)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the response JSON
            data = response.json()

            # Extract the URLs of the generated images
            for i, image_data in enumerate(data['data']):
                image_url = image_data['url']
                print(f"Image {i + 1} URL: {image_url}")

                # Download the image and save it locally
                try:
                    image_response = requests.get(image_url, timeout=timeout)
                    if image_response.status_code == 200:
                        filename = f"{config['filename']}{i + 1}.png"
                        with open(filename, 'wb') as image_file:
                            image_file.write(image_response.content)
                        print(f"Image {i + 1} saved as {filename}")
                    else:
                        print(f"Failed to download image {i + 1}")
                except requests.exceptions.Timeout:
                    print(f"Timeout occurred while downloading image {i + 1}")

        else:
            print(f"Failed to generate image: {response.status_code}")
            print(response.text)

    except requests.exceptions.Timeout:
        print("Timeout occurred while generating image")

if __name__ == "__main__":
    # Load configuration
    config = load_config('config2.json')

    # Generate image
    try:
        generate_image(config)
    except ValueError as e:
        print(f"Configuration error: {e}")