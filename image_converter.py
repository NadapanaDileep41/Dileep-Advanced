from PIL import Image
import os

def convert_image(input_path, output_path, output_format):
    try:
        image = Image.open(input_path)
        image.save(output_path, format=output_format)
        print(f"Image converted successfully to {output_format.upper()} format.")
    except Exception as e:
        print(f"Error converting image: {e}")

def main():
    input_path = input("Enter the path of the image file: ")
    
    if not os.path.exists(input_path):
        print("Invalid path.")
        return
    
    output_format = input("Enter the desired output format (JPEG, PNG, BMP, GIF): ").upper()
    if output_format not in ['JPEG', 'PNG', 'BMP', 'GIF']:
        print("Invalid output format.")
        return

    output_path = input("Enter the path for the converted image file: ")

    convert_image(input_path, output_path, output_format)
if __name__ == "__main__":
    main()
