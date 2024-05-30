# Smart Surveillance System

This project is a Smart Surveillance System designed for real-time video stream analysis, including human face recognition, object recognition, and behavior analysis. The system uses machine learning models and computer vision techniques to detect and analyze suspicious behaviors or events and identify specific individuals using facial recognition technology.

## Features

- **Real-time Video Stream Analysis**: Analyze video streams in real-time.
- **Human Face Recognition**: Recognize human faces in the video stream.
- **Object Recognition**: Detect specific objects in the video stream.
- **Behavior Analysis**: Analyze suspicious or predefined behaviors.

## Technologies Used

- **Backend**: Flask, OpenCV, TensorFlow/Keras
- **Frontend**: React, Material-UI
- **Models**: Pre-trained models for face detection, object detection, and behavior analysis


## Setup Instructions

### Prerequisites

- Python 3.x
- Node.js and npm

### Backend Setup

1. **Clone the repository**:

    ```sh
    git clone https://github.com/yourusername/smart_surveillance_system.git
    cd smart_surveillance_system/backend
    ```

2. **Create and activate a virtual environment**:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the required Python packages**:

    ```sh
    pip install -r requirements.txt
    ```

4. **Download the pre-trained models**:
    - Download the face detection model [haarcascade_frontalface_default.xml](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml) and place it in the `backend/models` directory.
    - Create the object detection and behavior analysis models by running:

    ```sh
    python create_object_model.py
    python create_behavior_model.py
    ```

5. **Run the Flask application**:

    ```sh
    python app.py
    ```

### Frontend Setup

1. **Navigate to the frontend directory**:

    ```sh
    cd ../frontend
    ```

2. **Install the required npm packages**:

    ```sh
    npm install
    ```

3. **Start the React application**:

    ```sh
    npm start
    ```

### Accessing the Application

- **Backend**: The Flask backend will be running on `http://127.0.0.1:5000`.
- **Frontend**: The React frontend will be running on `http://localhost:3000`.

Open your browser and navigate to the respective URLs to access the application and see the live video feed with analysis.

## Customizing the Application

You can customize the application by modifying the frontend and backend code. For example, you can change the video source by updating the `cv2.VideoCapture` path in `app.py`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the developers of [OpenCV](https://opencv.org/) and [TensorFlow](https://www.tensorflow.org/) for their amazing libraries.
- Material-UI for the beautiful UI components.
