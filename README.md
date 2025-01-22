# Video Frame Processing Tool

This is a web-based video processing tool that can add frame counters to videos and supports customizable text position and color.

## Features

- Support for multiple video formats (MP4, AVI, MOV)
- Drag and drop video file upload
- Customizable text position (top-left, top-right, bottom-left, bottom-right)
- Customizable text color
- Automatic frame counter addition

## Tech Stack

- Python 3.x
- Flask 2.0.1
- OpenCV 4.5.3
- NumPy 1.21.2

## Installation

1. Clone the project to your local machine

2. Install dependencies
```bash
pip install -r requirements.txt
```

## Usage

1. Start the server
```bash
python app.py
```

2. Visit `http://localhost:5000` in your browser

3. Using the interface
   - Click or drag to upload video file
   - Select text display position
   - Choose text color
   - Click "Process Video" button
   - Wait for processing to complete and the processed video will download automatically

## Notes

- Supported video formats: .mp4, .avi, .mov
- Upload file size limit: 16MB
- Processed video will be automatically downloaded as processed_video.mp4

## Directory Structure

```
.
├── app.py          # Main application
├── requirements.txt # Dependencies list
├── templates/      # HTML templates
│   └── index.html  # Main page
└── uploads/        # Temporary storage for uploaded files
```

## Development Notes

- Video processing core functionality is implemented in the `process_video` function
- Flask framework handles file upload and download
- OpenCV is used for video processing and frame operations
- Frontend uses native JavaScript for drag and drop file upload