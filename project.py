import os
import shutil
import argparse
import pytesseract
from PIL import Image

def list_files(folder):
    for f in os.listdir(folder):
        if f.endswith(('.png', '.jpg', '.jpeg')):
            yield f

def extract_text(file_path, language):
    try:
        image = Image.open(file_path)
        return pytesseract.image_to_string(image, lang=language)
    except Exception as e:
        print(f'Error processing {file_path}: {e}')
        return ""

def search_string(folder, string, language, output):
    new_folder = os.path.join(output, string)
    os.makedirs(new_folder, exist_ok=True)

    string = string.lower() 

    for file_name in list_files(folder):
        file_path = os.path.join(folder, file_name)
        extracted_text = extract_text(file_path, language)
        if string in extracted_text.lower():  
            print(f'The string "{string}" was found in {file_path}')
            shutil.copy(file_path, new_folder)

def main():
    parser = argparse.ArgumentParser(description='Search for a string in images within a folder.')
    parser.add_argument('-l', '--language', required=True, help='Language of the string to search for')
    parser.add_argument('-s', '--string', required=True, help='String to search for.')
    parser.add_argument('-p', '--path', required=True, help='Path to the folder to search.')
    parser.add_argument('-o', '--output', required=True, help='Path to create the new folder.')
    args = parser.parse_args()

    search_string(args.path, args.string, args.language, args.output)

if __name__ == '__main__':
    main()