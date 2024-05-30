# Text-on-images search

## Introduction
This project allows you to search for a specific string within image files in a specified folder. The images are processed using Tesseract OCR, and matching files are copied to a new directory.

## Installation
Tesseract OCR must be installed separately.

### Windows
Download the installer from the [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki) page and run it.

### macOS
Use Homebrew to install Tesseract:
```
brew install tesseract
```

### Linux
Use your package manager to install Tesseract. For example, on Ubuntu:
```
sudo apt-get install tesseract-ocr
```

### Prerequisites
- Python 3.x
- pip

### Install Python Dependencies
To install the necessary Python dependencies, run:
```
pip install -r requirements.txt
```

## Usage
### Command-Line Arguments
The program accepts the following command-line arguments:

* `-l` or `--language`: Required. The language of the string to search for. Specify the language code supported by Tesseract (e.g., eng for English, ita for Italian).
* `-s` or `--string`: Required. The string to search for within the images.
* `-p` or `--path`: Required. The path to the folder containing the images to search.
* `-o` or `--output`: Required. The path to create the new folder where matching images will be copied.

### Example Usage
To search for the string `vino` in images located in the folder `/venezia/bacari` using italian (`ita`) as the language, and to copy the matching images to the folder `bacarotour`, use the following command:

```
python project.py -l ita -s vino -p /venezia/bacari -o /bacarotour
```