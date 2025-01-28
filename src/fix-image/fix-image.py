from PIL import Image

def make_background_transparent(image_path, output_path):
    # Open the image
    image = Image.open(image_path).convert("RGBA")
    
    # Get the pixel data
    data = image.getdata()
    
    # Create a new list to hold the modified pixel data
    new_data = []
    
    for pixel in data:
        # If the pixel is white (or close to white), make it transparent
        if pixel[0] > 180 and pixel[1] > 180 and pixel[2] > 180:  # Adjust tolerance as needed
            new_data.append((255, 255, 255, 0))  # Transparent
        else:
            new_data.append(pixel)  # Keep the pixel as it is
    
    # Update the image with the new data
    image.putdata(new_data)
    
    # Save the output
    image.save(output_path, "PNG")
    print(f"Image saved with transparent background at {output_path}")

# Example usage
make_background_transparent("python-logo.png", "output_image.png")
