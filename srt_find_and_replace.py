#.srt text finder and replacer

# Main script to run the function
input_folder = r"C:\Users\julia\Documents\Computer_Docs\Ladino_Lateral_Project\SRT_Editor\SRT_Input"
output_folder = r"C:\Users\julia\Documents\Computer_Docs\Ladino_Lateral_Project\SRT_Editor\SRT_Input"
search_text = "ll"  # Text to search for
replace_text = "y"  # Text to replace with

import os
import codecs

def replace_text_in_srt(input_folder, output_folder, search_text, replace_text):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created output folder: {output_folder}")
    else:
        print(f"Output folder already exists: {output_folder}")
    
    # Iterate through all the files in the input folder
    file_count = 0
    for filename in os.listdir(input_folder):
        input_file_path = os.path.join(input_folder, filename)
        
        if filename.endswith(".srt"):
            file_count += 1
            print(f"Processing file: {filename}")
            
            output_file_path = os.path.join(output_folder, filename)
            
            # Read the contents of the SRT file
            try:
                with codecs.open(input_file_path, 'r', 'utf-8') as file:
                    srt_data = file.read()
                print(f"Successfully read file: {filename}")
            except Exception as e:
                print(f"Error reading file {filename}: {e}")
                continue

            # Check if the search text is in the file
            if search_text in srt_data:
                print(f"Found '{search_text}' in {filename}, replacing with '{replace_text}'")
                modified_srt_data = srt_data.replace(search_text, replace_text)
            else:
                print(f"'{search_text}' not found in {filename}, no replacement needed.")
                modified_srt_data = srt_data

            # Write the modified content to the output file
            try:
                with codecs.open(output_file_path, 'w', 'utf-8') as file:
                    file.write(modified_srt_data)
                print(f"Successfully wrote modified file: {filename}")
            except Exception as e:
                print(f"Error writing file {filename}: {e}")
        
    if file_count == 0:
        print(f"No .srt files found in folder: {input_folder}")
    else:
        print(f"Processed {file_count} .srt files.")

# Call the function
print(f"Starting text replacement in folder: {input_folder}")
replace_text_in_srt(input_folder, output_folder, search_text, replace_text)
print("Text replacement complete.")
