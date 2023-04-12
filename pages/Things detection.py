import requests
import streamlit as st
from PIL import Image
from ultralytics import YOLO
import cv2
from io import BytesIO
from streamlit_webrtc import (
    ClientSettings,
    VideoTransformerBase,
    WebRtcMode,
    webrtc_streamer,
)


# Initialize the YOLOv5 model
model = YOLO("models/yolov8s.pt")


# Define the Streamlit app
def main():
    st.title("Object Detection App")

    # Create a radio button to choose between uploading an image, using the webcam or providing an image URL
    choice = st.radio("Select an option", ("Upload an image", "Use webcam", "Provide image URL"))

    if choice == "Upload an image":
        # Create a file uploader widget
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

        # If a file is uploaded
        if uploaded_file is not None:
            # Load the image from the uploaded file
            img = Image.open(uploaded_file)

            results = model(source=img)
            res_plotted = results[0].plot()
            cv2.imwrite('images/test_image_output.jpg', res_plotted)
            
            col1, col2 = st.columns(2)

            col1.image(img, caption="Uploaded Image", use_column_width=True)
            # Display the uploaded image
            col2.image('images/test_image_output.jpg', caption="Predected Image", use_column_width=True)

    elif choice == "Use webcam":
        # Define the WebRTC client settings
        client_settings = ClientSettings(
            rtc_configuration={
                "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
            },
            media_stream_constraints={
                "video": True,
                "audio": False,
            },
        )

        # Define the WebRTC video transformer
        class ObjectDetector(VideoTransformerBase):
            def transform(self, frame):
                # Convert the frame to an image
                img = Image.fromarray(frame.to_ndarray())

                results = model(source=img)
                res_plotted = results[0].plot()
                output_frame = cv2.cvtColor(res_plotted, cv2.COLOR_BGR2RGB)

                # Return the annotated frame
                return output_frame

        # Start the WebRTC streamer
        webrtc_streamer(
            key="object-detection",
            mode=WebRtcMode.SENDRECV,
            client_settings=client_settings,
            video_transformer_factory=ObjectDetector,
        )

    elif choice == "Provide image URL":
        # Get the image URL from the user
        image_url = st.text_input("Enter the image URL:")

        # If the user has entered an image URL
        if image_url != "":
            try:
                # Download the image from the URL
                response = requests.get(image_url)
                img = Image.open(BytesIO(response.content))

                results = model(source=img)
                res_plotted = results[0].plot()
                cv2.imwrite('images/test_image_output.jpg', res_plotted)
                
                col1, col2 = st.columns(2)
                col1.image(img, caption="Downloaded Image" , use_column_width=True)
                # Display the downloaded image
                col2.image('images/test_image_output.jpg', caption="predected Image", use_column_width=True)
            except:
                st.error("Error: Invalid image URL or unable to download the image.")


if __name__ == '__main__':
    main()
