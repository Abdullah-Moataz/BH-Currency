# 🇧🇭 Bahraini Currency Detection Using YOLO11

An AI-powered object detection application that identifies and classifies Bahraini currency using **YOLO11** and **Streamlit**.

The system detects currency in images, draws bounding boxes around detected objects, and displays the predicted denomination with a confidence score.

### 🚀 Live Demo

**[Try the Bahraini Currency Detector](https://bh-currency-gb3rnelhuzdr7bfqnsteo5.streamlit.app/)**

## ✨ Features

- 📷 **Camera Support:** Capture currency images directly using your device's camera.
- 🖼️ **Image Upload:** Upload images in JPG, JPEG, or PNG format.
- 🎯 **Object Detection:** Detect and classify multiple currency objects in a single image.
- 📦 **Bounding Boxes:** Visualize detected currency with labeled bounding boxes.
- 📊 **Confidence Scores:** Display prediction confidence for each detected object.
- 🎚️ **Adjustable Threshold:** Control the minimum confidence required for detection.
- 🌐 **Web Deployment:** Accessible through Streamlit Community Cloud.

## 🧠 Model & Technology

| Component | Technology |
|---|---|
| Object Detection | YOLO11 Nano (YOLO11n) |
| Framework | Ultralytics |
| Programming Language | Python |
| Web Application | Streamlit |
| Image Processing | OpenCV, Pillow |
| Dataset | Roboflow |
| Training Environment | Google Colab |
| Deployment | Streamlit Community Cloud |

## 📂 Dataset

The model was trained using an annotated Bahraini currency dataset available on Roboflow.

**[Bahrain Currency Object Detector Dataset](https://universe.roboflow.com/alfadhul-almubarak/bahrain_currency_object_detector/dataset/3)**

The dataset contains seven currency classes.

| Dataset Split | Images |
|---|---:|
| Training | 4,668 |
| Validation | 296 |
| Testing | 260 |
| **Total** | **5,224** |

## 📊 Model Performance

The YOLO11n model was fine-tuned for **5 epochs** using images resized to 640 × 640 pixels.

### Test Set Results

| Evaluation Metric | Result |
|---|---:|
| Precision | 80.54% |
| Recall | 89.72% |
| mAP@50 | 92.12% |
| mAP@50–95 | 70.56% |

The model achieved a **92.12% mAP@50** on the test dataset, demonstrating promising object detection performance after a short training period.

### Confusion Matrix

The confusion matrix illustrates the model's classification performance, including correct detections, misclassifications, false positives, and missed objects.

![YOLO11 Confusion Matrix](images/confusion_matrix.png)

*Note: The confusion matrix should be interpreted alongside precision, recall, and mAP because this is an object detection task.*

## ⚙️ Installation

**1. Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/bh-currency.git
cd bh-currency
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Run the Streamlit application**

```bash
streamlit run BD_currency.py
```

## 📱 How to Use

1. Open the [Live Application](https://bh-currency-gb3rnelhuzdr7bfqnsteo5.streamlit.app/).
2. Select **Camera** or **Upload Image**.
3. Capture or upload an image containing Bahraini currency.
4. Adjust the confidence threshold if necessary.
5. View the detected currency, bounding boxes, and confidence scores.

## 📁 Project Structure

```text
bh-currency/
├── BD_currency.py
├── best.pt
├── requirements.txt
├── packages.txt
├── README.md
└── images/
    └── confusion_matrix.png
```

## 🔮 Future Improvements

- Train the model for additional epochs.
- Improve performance on underrepresented currency classes.
- Expand the dataset with different lighting conditions and backgrounds.
- Implement real-time video detection.
- Improve the user interface and mobile experience.

## 📚 Acknowledgments

- [Ultralytics](https://www.ultralytics.com/) — YOLO11 object detection framework.
- [Roboflow](https://roboflow.com/) — Annotated currency dataset.
- [Streamlit](https://streamlit.io/) — Web application framework.

---

**Built with Python, YOLO11, and Streamlit 🇧🇭**
