import json
import glob

def combine_json_files(output_file, json_files):
    combined_data = {}

    for json_file in json_files:
        with open(json_file, 'r') as file:
            data = json.load(file)
            energy_level = json_file.split("_")[-1].split(".")[0]  # Extract energy level from filename
            combined_data[energy_level] = data  # Add data under energy level key

    # Save the combined data to a new JSON file
    with open(output_file, 'w') as file:
        json.dump(combined_data, file, indent=4)

    print(f"Combined data saved to {output_file}")

