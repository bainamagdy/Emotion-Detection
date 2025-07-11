import streamlit as st 
from deepface import DeepFace
import cv2 
import numpy as np 
from PIL import Image 
import tempfile

# --- Page Config & Style ---
st.set_page_config(page_title="Emotion Detection App", page_icon="😊", layout="centered")
st.markdown("""
    <style>
        .main { background-color: #f0f2f6; }
        .stButton>button { background-color: #4CAF50; color: white; }
        .stFileUploader { border: 1px solid #4CAF50; }
        .stRadio > div { flex-direction: row; }
    </style>
""", unsafe_allow_html=True)

st.title("😊 Emotion Detection App")
st.write("Detect emotions from your images or videos using DeepFace.")

# --- Emotion Analysis Function ---
def analyzeEmotion(img_vid):
    try:
        analyze = DeepFace.analyze(img_vid, actions=["emotion"], enforce_detection=False)
        return analyze[0]['emotion']
    except Exception as e:
        st.error("Error in analyzing the image or video. Please check the input format.")
        return None

# --- GUI ---
option = st.radio("Select Input Type", ("Image", "Video"), horizontal=True)

# --- Main Logic ---
if option == "Image":
    st.subheader("Upload an Image")
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        img_arr = np.array(img)
        st.image(img, caption="Uploaded Image", use_column_width=True)
        with st.spinner("Analyzing emotion..."):
            analyze_result = analyzeEmotion(img_arr)
        if analyze_result:
            detect_emotion = max(analyze_result, key=analyze_result.get)
            st.success(f"**Detected Emotion:** {detect_emotion}")
            st.json(analyze_result)
        else:
            st.error("Could not detect emotion from the image.")

elif option == "Video":
    st.subheader("Upload a Video")
    uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "avi", "mov"])
    if uploaded_file is not None:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_file.read())
        tfile.close()
        video_path = tfile.name
        cap = cv2.VideoCapture(video_path)
        frame_count = 0
        frame_rate = 30  # Analyze every 30th frame
        stframe = st.empty()
        detected_emotions = []
        with st.spinner("Processing video..."):
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                frame_count += 1
                if frame_count % frame_rate == 0:
                    img_arr = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    stframe.image(img_arr, caption=f"Frame {frame_count}")
                    analyze_result = analyzeEmotion(img_arr)
                    if analyze_result:
                        detect_emotion = max(analyze_result, key=analyze_result.get)
                        detected_emotions.append(detect_emotion)
                        st.write(f"Detected Emotion: {detect_emotion}")
                    else:
                        st.write("No emotion detected in this frame.")
            cap.release()
        if detected_emotions:
            st.success("Video processing completed.")
            st.write("**Summary of detected emotions:**")
            st.write(detected_emotions)
        else:
            st.error("No emotions detected in the video.")




