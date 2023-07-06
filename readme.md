# Object Detection App

This is a Streamlit app for performing object detection on images and webcam streams using the YOLOv8 model.

The aim of this project is to perform object detection on images and webcam streams to classify them as either `device`, `live`, `photo`, or `spoof`.

## Usage

To use the app, follow these steps:

1. Clone the repository: 
```consol
git clone https://github.com/your-username/your-repo-name.git
```
2. Install the dependencies:

```consol
pip install -r requirements.txt
```
3. Run the app:
```consol
streamlit run app.py
```
4. Select an option from the radio button:

    - **Upload an image:** Upload an image from your local machine to perform object detection on.

    - **Use webcam:** Use your webcam to perform object detection on a live stream.

    - **Provide image URL:** Provide a URL of an image to perform object detection on.

5. Follow the instructions based on your selected option.


## Dependencies

The following dependencies are required to run the app:

- streamlit
- Pillow
- ultralytics
- opencv-python-headless
- requests
- streamlit-webrtc

These dependencies can be installed by running the following command:

```consol
pip install -r requirements.txt
```


## Model

The YOLOv8 model used for object detection can be found in the `models` directory. The `best_real_face_detection.pt` file is used for real face detection.

## License

This project is licensed under the terms of the MIT license.


Me suivre sur LinkedIn : www.linkedin.com/comm/mynetwork/discovery-see-all?usecase=PEOPLE_FOLLOWS&followMember=emad-darwich
