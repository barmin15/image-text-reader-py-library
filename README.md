# OCR Image Text Extraction

This project demonstrates the use of Optical Character Recognition (OCR) to extract text from images using Python. The project leverages the `pytesseract` library for OCR and the `Pillow` library for image processing.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

- Python 3.x
- Tesseract-OCR

## Installation

1. Install the required Python libraries:

    ```bash
    pip install pytesseract Pillow
    ```

2. Install Tesseract-OCR:
    - **Windows:** Download and install from [here](https://github.com/UB-Mannheim/tesseract/wiki).
    - **macOS:** Use Homebrew to install:

      ```bash
      brew install tesseract
      ```

    - **Linux:** Use your package manager, for example:

      ```bash
      sudo apt-get install tesseract-ocr
      ```

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/ocr-image-text-extraction.git
    cd ocr-image-text-extraction
    ```

2. Update the path to Tesseract-OCR executable in the script:

    ```python
    pytesseract.pytesseract.tesseract_cmd = r'/path/to/tesseract.exe' # Update this path for your computer
    ```

3. Update the image path in the script:

    ```python
    image_path = 'path_to_your_image.jpg' # Update this path for your image
    ```

4. Run the script:

    ```bash
    python ocr_script.py
    ```

## Code Explanation

- **Preprocessing Function:**

    ```python
    def preprocess_image(image_path):
        image = Image.open(image_path).convert('L')
        image = image.filter(ImageFilter.SHARPEN)
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(2)
        return image
    ```

    This function opens the image, converts it to grayscale, sharpens it, and enhances the contrast to improve OCR accuracy.

- **OCR Function:**

    ```python
    def ocr_image(image_path):
        image = preprocess_image(image_path)
        text = pytesseract.image_to_string(image, lang='eng')
        return text
    ```

    This function processes the image and then extracts the text using `pytesseract`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License

This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for more details.

