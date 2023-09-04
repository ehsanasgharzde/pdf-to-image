# PDF to Image Converter

This Python script converts PDF files into image files, providing a convenient way to extract images from PDF documents.

## Files

The program consists of the following files:

1. `main.py`: The main script responsible for PDF to image conversion.
2. `poppler/`: A directory containing the Poppler utility binaries needed for PDF conversion.

## How to Use

1. Ensure you have Python installed on your system.

2. Place the PDF files you want to convert into the same directory as `main.py`.

3. Make sure you have the `poppler` directory containing Poppler's utility binaries. Poppler is required for PDF to image conversion.

4. Run the program by executing `main.py`.

5. The program will prompt you to enter the DPI (dots per inch) for image conversion. This determines the image quality and resolution.

6. The program will convert each PDF file in the directory into a separate PNG image file.

7. You can find the resulting PNG images in the "images" directory. Each image will be numbered sequentially.

8. You can customize the program further by modifying the input and output directories, image format, or other parameters as needed.

## Dependencies

The program relies on Python for script execution and the Poppler utility for PDF to image conversion. Make sure you have both installed on your system.

## Notes

- This program is intended for extracting images from PDFs for various purposes, such as document analysis or image processing.
- You can adapt and extend this code for more advanced PDF processing tasks, such as OCR (Optical Character Recognition) or document parsing.
- The program assumes that the input PDF files are in the same directory as `main.py`. You can modify the script to handle different input and output directories.
- Ensure that the `poppler` directory contains the necessary Poppler utility binaries for your operating system.
