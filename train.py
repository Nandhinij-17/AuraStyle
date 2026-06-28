import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import os

# Load dataset
df = pd.read_csv("dataset/styles.csv", on_bad_lines="skip")

# Display first 5 rows
print(df.head())

# Select first product
image_id = str(df.iloc[0]["id"])
image_path = os.path.join("dataset", "images", image_id + ".jpg")

print("Image Path:", image_path)

# Show image
img = Image.open(image_path)
plt.imshow(img)
plt.axis("off")
plt.title(df.iloc[0]["productDisplayName"])
plt.show()