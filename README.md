# 👗 AuraStyle - AI Fashion Classification & Recommendation System

AuraStyle is an AI-powered fashion image classification web application that predicts the category of a fashion product from an uploaded image. The system is built using TensorFlow, Flask, HTML, CSS, and JavaScript, and provides confidence scores, top predictions, and product recommendations.

---

## 📌 Project Title

**AuraStyle: Multimodal E-Commerce Fashion & Text-to-Image Trend Matcher**

---

## 🚀 Features

- 📷 Upload fashion images
- 🤖 AI-based fashion category prediction
- 📊 Displays confidence score
- 🥇 Top 3 prediction results
- 🛍️ Product recommendation section
- 🌐 Flask web application
- 💻 Responsive user interface

---

## 🛠️ Technologies Used

- Python
- Flask
- TensorFlow / Keras
- NumPy
- Pillow (PIL)
- HTML5
- CSS3
- JavaScript
- Git & GitHub

---

## 📂 Project Structure

```
AuraStyle/
│
├── app.py
├── model_train.py
├── predict.py
├── prepare_data.py
├── prepare_dataset.py
├── train.py
├── fashion_model.keras
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   ├── images/
│   └── uploads/
│
└── dataset/
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Nandhinij-17/AuraStyle.git
```

### 2. Open the Project Folder

```bash
cd AuraStyle
```

### 3. Create a Virtual Environment (Optional)

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

Windows

```bash
.venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Flask Application

```bash
python app.py
```

### 7. Open in Browser

```
http://127.0.0.1:5000
```

---

## 🧠 AI Model

The application uses a Convolutional Neural Network (CNN) built with TensorFlow/Keras to classify fashion images into multiple categories.

The model predicts:

- Top predicted class
- Confidence score
- Top 3 probable categories

---

## 📊 Fashion Categories

The model classifies images into categories such as:

- Topwear
- Bottomwear
- Shoes
- Bags
- Watches
- Saree
- Dress
- Accessories
- Jewellery
- Socks
- Wallets
- Watches
- Sports Equipment
- Headwear
- And many more...

---

## 🖼️ How It Works

1. User uploads a fashion image.
2. Flask receives the image.
3. The image is preprocessed.
4. TensorFlow model predicts the fashion category.
5. Prediction and confidence score are displayed.
6. Recommended products are shown on the webpage.

---

## 📸 Screenshots

### Home Page

(Add screenshot here)

### Upload Image

(Add screenshot here)

### Prediction Result

(Add screenshot here)

---

## 📈 Future Enhancements

- Voice Search
- Text-to-Image Search
- CLIP Model Integration
- Similar Fashion Recommendation
- MongoDB Integration
- User Login System
- Shopping Cart
- Online Payment Gateway

---

## 🎯 Advantages

- Fast image prediction
- Easy-to-use interface
- AI-powered classification
- Responsive design
- Can be extended into a complete e-commerce platform

---

## 👩‍💻 Developed By

**Nandhini J**


## 📄 License

This project is developed for educational and academic purposes.

---

## ⭐ GitHub Repository

https://github.com/Nandhinij-17/AuraStyle
