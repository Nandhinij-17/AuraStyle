from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import os

app = Flask(__name__)

# Load trained model
model = tf.keras.models.load_model("fashion_model.keras")

# Class names
class_names = [
    'Accessories', 'Apparel Set', 'Bags','Bath and Body',
    'Beauty Accessories', 'Belts', 'Bottomwear', 'Cufflinks',
    'Dress', 'Eyes', 'Eyewear', 'Flip Flops', 'Fragrance',
    'Free Gifts', 'Gloves', 'Hair', 'Headwear',
    'Home Furnishing', 'Innerwear', 'Jewellery', 'Lips',
    'Loungewear and Nightwear', 'Makeup', 'Mufflers',
    'Nails', 'Perfumes', 'Sandal', 'Saree', 'Scarves',
    'Shoe Accessories', 'Shoes', 'Skin', 'Skin Care',
    'Socks', 'Sports Accessories', 'Sports Equipment',
    'Stoles', 'Ties', 'Topwear', 'Umbrellas',
    'Vouchers', 'Wallets', 'Watches',
    'Water Bottle', 'Wristbands'
]

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Recommended products
products = {
    "Topwear": [
        {"name": "Blue T-Shirt", "image": "images/tshirt.jpg", "price": "₹699"},
        {"name": "Grey Hoodie", "image": "images/hoodie.jpg", "price": "₹1499"}
    ],

    "Shoes": [
        {"name": "Running Shoes", "image": "images/shoes.jpg", "price": "₹2499"}
    ],

    "Watches": [
        {"name": "Sports Watch", "image": "images/watch.jpg", "price": "₹1999"}
    ],

    "Bags": [
        {"name": "Laptop Bag", "image": "images/laptopbag.jpg", "price": "₹999"},
        {"name": "Hand Bag", "image": "images/handbag.jpg", "price": "₹1299"}
    ],

    "Bottomwear": [
        {"name": "Blue Jeans", "image": "images/jeans.jpg", "price": "₹1299"}
    ]
}

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    confidence = None
    image_path = None
    top_predictions = []
    recommendations = []

    if request.method == "POST":

        file = request.files["image"]

        if file:

            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)

            image_path = filepath

            img = image.load_img(filepath, target_size=(224, 224))
            img_array = image.img_to_array(img)/255.0
            img_array = np.expand_dims(img_array, axis=0)

            pred = model.predict(img_array)

            predicted_index = np.argmax(pred)

            prediction = class_names[predicted_index]

            confidence = round(float(np.max(pred))*100,2)

            top_indices = np.argsort(pred[0])[-3:][::-1]

            for i in top_indices:

                top_predictions.append({
                    "name": class_names[i],
                    "score": round(float(pred[0][i])*100,2)
                })

            recommendations = products.get(prediction, [])

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        image_path=image_path,
        top_predictions=top_predictions,
        recommendations=recommendations
    )

if __name__ == "__main__":
    app.run(debug=True)