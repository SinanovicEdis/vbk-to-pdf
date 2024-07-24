import pyautogui
import time

def capture_page():
    """Capture the specific area of the screen where the page is displayed."""
    # Coordinates of the top-left corner and the width and height of the capture area
    x, y, width, height = 90, 86, 1500, 888  # Adjust these values based on your needs
    image = pyautogui.screenshot(region=(x, y, width, height))
    # Convert the image to RGB (required for saving to PDF)
    image = image.convert('RGB')
    return image

def go_to_next_page():
    """Simulate a mouse click on the 'Next Page' button."""
    # Coordinates of the 'Next Page' button; you need to set these manually
    next_page_button_x = 1643
    next_page_button_y = 1015
    pyautogui.click(next_page_button_x, next_page_button_y)

def main(total_pages):
    images = []
    for page_number in range(1, total_pages + 1):
        print(f"Capturing page {page_number}")
        img = capture_page()
        images.append(img)
        if page_number < total_pages:
            go_to_next_page()
            time.sleep(1)  # Adjust delay as necessary for page loading
            
    # Save all captured images as a PDF
    if images:
        images[0].save('output.pdf', save_all=True, append_images=images[1:])
        print("Saved all pages to output.pdf")

if __name__ == "__main__":
    total_pages = int(input("Enter the total number of pages: "))
    main(total_pages)