import streamlit as st 
from deepface import DeepFace
import cv2 
import numpy as np 
from  PIL import  Image 
import tempfile



## FUNC 

def analyzeEmation(img_vid):
    try:
       analyze =  DeepFace.analyze(img_vid, actions=["emotion"],enforce_detection=False)
       return analyze[0]['emotion']
    except ValueError  as e:
        st.error("Error in analyzing the image or video. Please check the input format.")
        return None


##GUI 

option =st.selectbox("Select Input Type",("Image","Video"))






##MAIN FUNC
if option == "Image":
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None :
        img = Image.open(uploaded_file)
        img_arr = np.array(img)
        st.image(img, caption="Uploaded Image")
        analyze_result = analyzeEmation(img_arr)
        if analyze_result:
            detect_emotion  = max(analyze_result, key=analyze_result.get)
            st.write(f"Detected Emotion: {detect_emotion}")
        else:       
            st.error("Could not detect emotion from the image.")


if option == "Video":
    uploaded_file = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])
    if uploaded_file is not None:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_file.read())
        tfile.close()
        video_path = tfile.name
        cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        frame_count =0 
        frame_rate= 100
        ret,frame =cap.read() 
        if not ret :
            break
        frame_count += 1
        if frame_count % frame_rate == 0:
            img_arr = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            st.image(img_arr, caption="Video Frame")
            analyze_result = analyzeEmation(img_arr)
            if analyze_result:
                detect_emotion = max(analyze_result, key=analyze_result.get)
                st.write(f"Detected Emotion: {detect_emotion}")
            else:
                st.error("Could not detect emotion from the video frame.")
    cap.release()
    st.success("Video processing completed.")




