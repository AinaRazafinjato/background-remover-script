# Background Remover Script

A simple and efficient Python script to automatically remove the background from all images in a folder.

## 🚀 Features

- Automatic background removal from images
- Support for multiple formats: JPG, JPEG, PNG, JFIF, BMP, TIFF, WEBP
- Batch processing of all images in the folder
- Automatic saving with `_no_bg.png` suffix
- Command line interface with emojis for visual feedback

## 📋 Prerequisites

- Python 3.6+
- Required packages:
    ```bash
    pip install rembg pillow
    ```

## 💻 Installation

1. Clone this repository:
     ```bash
     git clone https://github.com/YOUR_USERNAME/REPO_NAME.git
     cd REPO_NAME
     ```

2. Install dependencies:
     ```bash
     pip install rembg pillow
     ```

## 🔧 Usage

1. Place the `background_remover.py` script in the folder containing your images
2. Run the script:
     ```bash
     python background_remover.py
     ```
3. Processed images will be saved with the `_no_bg.png` suffix

## 📁 File Structure

```
images-folder/
│
├── background_remover.py
├── image1.jpg
├── image2.png
└── ...
```

After processing:
```
images-folder/
│
├── background_remover.py
├── image1.jpg
├── image1_no_bg.png  ← New image without background
├── image2.png
├── image2_no_bg.png  ← New image without background
└── ...
```

## 🛠️ How it works

The script uses the `rembg` library which implements pre-trained AI models for background removal. It:

1. Scans the current folder for image files
2. Processes each image with the background removal model
3. Saves the result in PNG format with transparency

## 📝 Supported Formats

- JPG / JPEG
- PNG
- JFIF
- BMP
- TIFF
- WEBP

## ⚠️ Important Notes

- The script only processes images in the current folder (no subfolders)
- Output images are always in PNG format to preserve transparency
- Make sure you have enough disk space for processed images

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Improve documentation

## 📄 License

This project is under MIT license. See the [LICENSE](LICENSE) file for more details.

## 🙏 Acknowledgments

- [rembg](https://github.com/danielgatis/rembg) - For the background removal library
- [Pillow](https://python-pillow.org/) - For image processing