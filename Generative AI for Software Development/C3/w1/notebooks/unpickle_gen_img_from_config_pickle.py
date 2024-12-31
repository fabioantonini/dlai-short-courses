import pickle
import shutil
import json

def unpickle_data(pickle_file_path):
    """Unpickle data from a pickle file."""
    with open(pickle_file_path, 'rb') as pkl_file:
        data = pickle.load(pkl_file)
    return data

def save_unpickled_images(image_filenames):
    """Save images with a new suffix."""
    for original_filename in image_filenames:
        # Create a new filename with the 'unpkl' suffix
        new_filename = original_filename.replace('.png', '_unpkl.png')
        # Copy the original image to the new file
        shutil.copy(original_filename, new_filename)
        print(f"Image saved as {new_filename}")

if __name__ == "__main__":
    # Unpickle the data
    data = unpickle_data('generated_images.pkl')

    # Print the configuration
    config = data['config']
    print("Configuration:")
    print(json.dumps(config, indent=4))

    # Print the prompt used to generate the images
    prompt = config['payload']['prompt']
    print(f"\nPrompt: {prompt}")

    # Extract and save the images
    image_filenames = data['images']
    save_unpickled_images(image_filenames)