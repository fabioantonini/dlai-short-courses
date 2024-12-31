import openai
import json
import os

def load_config(file_path):
    """Load configuration from a JSON file."""
    with open(file_path, 'r') as file:
        return json.load(file)

def generate_image(config):
    """Generate an image using DALL-E API."""
    # Set up OpenAI API key
    openai.api_key = config['api_key']

    # Call the DALL-E API
    try:
        response = openai.Image.create(
            prompt=config['prompt'],
            n=config.get('n', 1),  # Number of images to generate
            size=config.get('size', '1024x1024')  # Image size
        )

        # Print the URL of the generated image(s)
        for i, image in enumerate(response['data']):
            print(f"Image {i + 1}: {image['url']}")

    except openai.error.OpenAIError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Load configuration
    config = load_config('config.json')

    # Generate image
    generate_image(config)