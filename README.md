
# Python Script for Capturing VitalSource Book Pages

  

This Python script automates the process of capturing screenshots of pages in VitalSource Bookshelf applications (.vbk) and compiles them into a single PDF file. It uses `pyautogui` for GUI automation and `Pillow` for image handling.

  

## Prerequisites

  

Before running the script, ensure you have Python installed on your system along with the following packages:

  

-  `pyautogui`

-  `Pillow`

  

Install these packages using pip:

  

pip install pyautogui pillow

  

## Configuration

  

You need to configure the coordinates for the page capture area and the "Next Page" button based on your screen setup and the VitalSource Bookshelf application's layout.

  

### Capture Area Coordinates

  

Set the coordinates for the area of the screen where the page content is displayed:

  

-  **Top-left corner:** (90, 86)

-  **Width and Height:** 1500 x 888

  

Adjust these values in the script to match the area of the page you want to capture.

 
Alternatively, if you want to capture the entire screen without specifying coordinates:

  

- **Full Screen Capture:** Replace the `capture_page` function's content with `image = pyautogui.screenshot()`. This will capture the entire screen instead of a specific area.

### Next Page Button Coordinates

  

Set the coordinates for the "Next Page" button:

  

-  **X and Y:** 1643, 1015

  

Ensure these coordinates point to the "Next Page" button in your application.

  

## Usage

  

1.  **Open the VitalSource Bookshelf** application and navigate to the first page of the book you want to capture.

2.  **Run the script:**

```python app.py```

4.  **Enter the total number of pages** when prompted. The script will capture each page and compile them into a PDF named `output.pdf`.

## Script Breakdown

  

### `capture_page()`

  

Captures a predefined area of the screen and converts it to an RGB image. Adjust the coordinates and dimensions to match the page layout of your book.

  

### `go_to_next_page()`

  

Simulates a mouse click on the "Next Page" button. Set the coordinates to match the location of the "Next Page" button in your application.

  

### `main()`

  

The main function handles the capturing of all pages and saving them into a PDF. It manages page transitions and ensures that all pages are captured before creating the PDF.

  

## Troubleshooting

  

**Incorrect Coordinates:** If the screenshots do not capture the correct area, adjust the `x`, `y`, `width`, and `height` values in the `capture_page()` function.

  

**Timing Issues:** If the script pages too quickly or too slowly, adjust the sleep times in the `main()` function.