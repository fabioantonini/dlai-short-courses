import pickle

# Define a Python dictionary to serialize
data = {
    'name': 'Alice',
    'age': 30,
    'skills': ['Python', 'Machine Learning', 'Data Analysis'],
    'is_active': True
}

# Serialize the dictionary to a file
with open('data.pkl', 'wb') as file:  # Open the file in binary write mode
    pickle.dump(data, file)
    print("Data has been serialized and written to 'data.pkl'.")

# Deserialize the dictionary from the file
with open('data.pkl', 'rb') as file:  # Open the file in binary read mode
    loaded_data = pickle.load(file)
    print("Data has been deserialized from 'data.pkl'.")

# Print the deserialized data
print("Deserialized Data:")
print(loaded_data)

# Verify that the original and loaded data are the same
assert data == loaded_data, "The original and loaded data do not match!"