"""
Image to ASCII Art Converter
Converts a photo into ASCII art matching the rebuild.py format.
Output: 100 chars wide x 55 lines tall, using characters: @%#*+=-
"""

from PIL import Image, ImageEnhance, ImageFilter
import sys
import os

# ASCII characters from darkest to lightest
ASCII_CHARS = "@%#*+=-"

def image_to_ascii(image_path, width=100, height=55, contrast=1.5, brightness=1.0, invert=False):
    """Convert an image to ASCII art."""
    
    # Open and process image
    img = Image.open(image_path)
    
    # Convert to grayscale
    img = img.convert('L')
    
    # Enhance contrast for better detail
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(contrast)
    
    # Enhance brightness
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(brightness)
    
    # Apply slight sharpening for better edges
    img = img.filter(ImageFilter.SHARPEN)
    
    # Resize image - ASCII chars are ~2x taller than wide, so adjust height
    img = img.resize((width, height))
    
    # Get pixel data
    pixels = list(img.getdata())
    
    # Map pixels to ASCII characters
    ascii_lines = []
    for i in range(height):
        line = ""
        for j in range(width):
            pixel = pixels[i * width + j]
            
            if invert:
                pixel = 255 - pixel
            
            # Map pixel value (0-255) to ASCII character index
            char_index = int(pixel / 256 * len(ASCII_CHARS))
            char_index = min(char_index, len(ASCII_CHARS) - 1)
            line += ASCII_CHARS[char_index]
        
        ascii_lines.append(line)
    
    return "\n".join(ascii_lines)


def update_rebuild_py(ascii_art, rebuild_path="rebuild.py"):
    """Update the ascii_art variable in rebuild.py with new ASCII art."""
    
    with open(rebuild_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the ascii_art variable and replace it
    start_marker = 'ascii_art = """'
    end_marker = '"""'
    
    start_idx = content.find(start_marker)
    if start_idx == -1:
        print("ERROR: Could not find 'ascii_art = \"\"\"' in rebuild.py")
        return False
    
    # Find the closing """
    search_from = start_idx + len(start_marker)
    end_idx = content.find(end_marker, search_from)
    if end_idx == -1:
        print("ERROR: Could not find closing '\"\"\"' in rebuild.py")
        return False
    
    # Replace the content between the markers
    new_content = content[:start_idx + len(start_marker)] + ascii_art + content[end_idx:]
    
    with open(rebuild_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("Successfully updated rebuild.py with new ASCII art!")
    return True


def main():
    # Configuration
    image_path = "photo.jpg"  # Change this to your image filename
    width = 100
    height = 55
    contrast = 1.6        # Increase for more detail (1.0 = normal)
    brightness = 1.0       # Adjust brightness (1.0 = normal)
    invert = False         # Set True if image appears inverted
    auto_update = False    # Auto-update rebuild.py without asking
    
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
    if len(sys.argv) > 2 and sys.argv[2] == "--auto":
        auto_update = True
    
    if not os.path.exists(image_path):
        print(f"ERROR: Image file '{image_path}' not found!")
        print("Usage: python image_to_ascii.py [image_path] [--auto]")
        sys.exit(1)
    
    print(f"Converting '{image_path}' to ASCII art...")
    print(f"   Dimensions: {width}x{height}")
    print(f"   Contrast: {contrast}, Brightness: {brightness}")
    print()
    
    # Generate ASCII art
    ascii_art = image_to_ascii(
        image_path, 
        width=width, 
        height=height, 
        contrast=contrast, 
        brightness=brightness,
        invert=invert
    )
    
    # Preview
    print("=" * 100)
    print("PREVIEW:")
    print("=" * 100)
    print(ascii_art)
    print("=" * 100)
    print()
    
    # Save to file
    with open("ascii_output.txt", "w", encoding="utf-8") as f:
        f.write(ascii_art)
    print("ASCII art saved to ascii_output.txt")
    
    # Update rebuild.py
    if auto_update:
        update_rebuild_py(ascii_art)
    else:
        response = input("\nUpdate rebuild.py with this ASCII art? (y/n): ").strip().lower()
        if response == 'y':
            update_rebuild_py(ascii_art)
        else:
            print("Skipped. You can manually copy from ascii_output.txt")


if __name__ == "__main__":
    main()
