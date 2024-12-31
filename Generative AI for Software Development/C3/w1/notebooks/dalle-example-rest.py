import requests
import json

def load_config(file_path):
    """Load configuration from a JSON file."""
    with open(file_path, 'r') as file:
        return json.load(file)

def generate_image(config):
    """Generate an image using the OpenAI API."""
    url = "https://api.openai.com/v1/images/generations"

    headers = {
        "Authorization": f"Bearer {config['api_key']}",
        "Content-Type": "application/json"
    }

    data = {
        "prompt": config['prompt'],
        "n": config.get('n', 1),
        "size": config.get('size', '1024x1024')
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        images = response.json().get('data', [])
        for i, image in enumerate(images):
            print(f"Image {i + 1}: {image['url']}")
    else:
        print(f"Failed to generate image: {response.status_code}")
        print(response.json())

if __name__ == "__main__":
    # Load configuration
    config = load_config('config.json')

    # Generate image
    generate_image(config)