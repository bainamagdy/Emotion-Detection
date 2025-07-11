# Emotion Detection App

This project is a simple web application for detecting emotions from images and videos using [DeepFace](https://github.com/serengil/deepface) and [Streamlit](https://streamlit.io/).

## Features

- Detects emotions from uploaded images (JPG, JPEG, PNG)
- Detects emotions from uploaded videos (MP4, AVI, MOV)
- Displays the detected emotion for each image or video frame

## Requirements

- Python 3.10+
- [DeepFace](https://pypi.org/project/deepface/)
- [Streamlit](https://pypi.org/project/streamlit/)
- OpenCV
- NumPy
- Pillow

Install dependencies with:

```sh
pip install deepface streamlit opencv-python numpy pillow
```

## Usage

1. Run the Streamlit app:

    ```sh
    streamlit run app.py
    ```

2. Open the provided local URL in your browser.
3. Select "Image" or "Video" as input type.
4. Upload your file and view the detected emotion.

## File Structure

- `app.py` - Main Streamlit application
- `DeppFace.ipynb` - Notebook for experimenting with DeepFace
- `README.md` - Project documentation

## Notes

- For best results, use clear images or videos with visible faces.
- If you encounter errors, ensure all dependencies are installed and your input files are valid.

## License

This project is for educational purposes.