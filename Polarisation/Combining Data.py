import pandas as pd
import glob

def combine_csv_files_polarisation():
    # Set the path to your Polarisation folder
    folder_path = r"C:\Users\gabri\OneDrive\Documents\University\Mphys\TriBoson\Polarisation"
    
    # Find all CSV files in the folder
    csv_files = glob.glob(f"{folder_path}\\Helicity_analysis_data_*.csv")
    
    # Check if files are found
    if not csv_files:
        print("No CSV files found in the Polarisation folder to combine!")
        return

    # Combine all CSV files into one DataFrame
    combined_df = pd.concat([pd.read_csv(f) for f in csv_files], ignore_index=True)

    # Save the combined DataFrame
    output_file = f"{folder_path}\\combined_helicity_data.csv"
    combined_df.to_csv(output_file, index=False)
    print(f"Combined data saved to {output_file}")

# Ensure the function is called only when the script is run directly
if __name__ == "__main__":
    combine_csv_files_polarisation()