
import streamlit as st
from ultralytics import YOLO
from PIL import Image

st.set_page_config(page_title="Bahraini Currency Detector", page_icon="🇧🇭")

st.title("🇧🇭 Bahraini Currency Detector")
st.write("Detect Bahraini banknotes and coins using YOLO11.")

@st.cache_resource
def load_model():
    return YOLO("best.pt")

model = load_model()

confidence = st.slider("Confidence threshold", 0.1, 1.0, 0.25, 0.05)

option = st.radio("Choose input method:", ["Upload Image","Camera"])

if option == "Camera":
    uploaded_file = st.camera_input("Take a photo of your currency")
else:
    uploaded_file = st.file_uploader(
        "Upload a currency image",
        type=["jpg", "jpeg", "png"]
    )

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")

    results = model.predict(
        source=image,
        conf=confidence
    )

    annotated_image = results[0].plot()

    st.image(
        annotated_image,
        caption="Detected Currency",
        channels="BGR",
        use_container_width=True
    )

    detections = results[0].boxes

    if len(detections) == 0:
        st.warning("No currency detected.")
    else:
        st.success(f"Detected {len(detections)} currency object(s)")

        for box in detections:
            class_id = int(box.cls[0])
            class_name = model.names[class_id]
            score = float(box.conf[0])

            st.write(f"**{class_name}** — Confidence: {score:.1%}")
