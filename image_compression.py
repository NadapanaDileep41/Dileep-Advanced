from PIL import Image
import os

def compress_image(input_path, output_path, quality=85):
    try:
        image = Image.open(input_path)
        image.save(output_path, quality=quality)
        print(f"Image compressed successfully with quality {quality}.")
    except Exception as e:
        print(f"Error compressing image: {e}")

def main():
    input_path = input("Enter the path of the image file: ")
    
    if not os.path.exists(input_path):
        print("Invalid path.")
        return
    
    quality = int(input("Enter the compression quality (1-100): "))
    if quality < 1 or quality > 100:
        print("Invalid compression quality. Quality should be between 1 and 100.")
        return

    output_path = input("Enter the path for the compressed image file: ")

    compress_image(input_path, output_path, quality)

if __name__ == "__main__":
    main()
