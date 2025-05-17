
#Real Time Fire And Smoke Detection

This project detects **fire** and **smoke** in a video using computer vision techniques with OpenCV in Python. It highlights fire and smoke in real time and displays the processed frames.




## Features

- 🔥 **Real-Time Fire Detection**
  - Uses HSV color filtering and contour analysis to identify fire regions.
  - Draws bounding boxes and labels detected fire areas in red.

- 💨 **Smoke Detection with Motion Analysis**
  - Combines motion detection (frame differencing) with HSV masking.
  - Detects slow-moving, gray/white smoke clouds.
  - Bounding boxes are drawn in gray with the label "Smoke".

- 📹 **Video Frame Buffering**
  - Maintains a frame buffer using `deque` to track changes over time.
  - Enhances detection stability by analyzing motion over multiple frames.
## Installation



### 1. Clone the Repository





### 2. Create a Virtual Environment (Optional but Recommended)


### 3. Install Dependencies

### 4. Run the Script

## Usage/Examples

## ▶️ Usage & Example

### 🔧 Basic Usage

Run the detection script using a video file:


To specify your own video file:

Replace path/to/your/video.mp4 with the actual path to your video file.


## License

[MIT](https://choosealicense.com/licenses/mit/)


## Acknowledgements

- [OpenCV](https://opencv.org/) – Powerful open-source computer vision library used for image processing and video analysis.
- [NumPy](https://numpy.org/) – Fundamental package for numerical computing in Python.
- [Python](https://www.python.org/) – Easy-to-use programming language ideal for rapid development of computer vision applications.
## Feedback

If you have any feedback, please reach out to us at For questions or improvements, feel free to reach out:

📩 Email: harishlm2005@gmail.com

🌐 GitHub: https://github.com/harishlm05

