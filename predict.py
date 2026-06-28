import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# -----------------------------
# Load the trained model
# -----------------------------
model = tf.keras.models.load_model("fashion_model.keras")

# -----------------------------
# Load class names automatically
# -----------------------------
datagen = ImageDataGenerator(rescale=1.0 / 255)

train_data = datagen.flow_from_directory(
    "dataset/train",
    target_size=(128, 128),
    batch_size=32,
    class_mode="categorical",
    shuffle=False
)

class_names = list(train_data.class_indices.keys())

print("Classes found:", class_names)
print("Number of classes:", len(class_names))

# -----------------------------
# Load the test image
# -----------------------------
# Change this path to any image you want to test
image_path = "dataset/images/1163.jpg"

img = image.load_img(image_path, target_size=(128, 128))
img_array = image.img_to_array(img)
img_array = img_array / 255.0
img_array = np.expand_dims(img_array, axis=0)

# -----------------------------
# Predict
# -----------------------------
prediction = model.predict(img_array)

predicted_index = np.argmax(prediction)
confidence = np.max(prediction)

print("\nPredicted Index :", predicted_index)
print("Predicted Class :", class_names[predicted_index])
print("Confidence      :", round(float(confidence) * 100, 2), "%")