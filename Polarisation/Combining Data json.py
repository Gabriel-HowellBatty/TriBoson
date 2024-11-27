import json
import glob
import os

# Define the path where JSON files are located
json_folder = os.path.abspath("../DataFiles")  # Path to JSON files
json_files = os.path.join(json_folder, "*.json")  # Match all JSON files in the folder

# Initialize a dictionary to store combined data
combined_data = {}

# Debug: Print the list of JSON files found
print("Looking for JSON files in:", json_folder)
print("Files found:", list(glob.glob(json_files)))

# Iterate over each JSON file in the directory
for file_name in glob.glob(json_files):
    with open(file_name, 'r') as file:
        data = json.load(file)
        # Extract energy level from the filename
        # Assuming the filename is something like "data_14.0.json"
        base_name = os.path.basename(file_name).replace(".json", "")  # Remove extension
        energy_level = base_name.split("_")[-1]  # Extract the part after the last underscore
        combined_data[energy_level] = data

# Define the output file path
output_directory = os.path.abspath(r"C:\Users\gabri\Documents\University\Year 4\Mphys\DataFiles")  # Adjust directory as needed
os.makedirs(output_directory, exist_ok=True)  # Create the directory if it doesn't exist
output_file = os.path.join(output_directory, "combined_data.json")

# Save the combined data into the file
with open(output_file, 'w') as file:
    json.dump(combined_data, file, indent=4)
    print("File written successfully.")

print(f"Combined data saved to {output_file}")
