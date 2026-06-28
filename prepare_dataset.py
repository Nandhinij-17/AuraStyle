import os
import shutil
import pandas as pd

# Read CSV
df = pd.read_csv("dataset/styles.csv", on_bad_lines="skip")

source_folder = "dataset/images"
destination_folder = "dataset/train"

# Create train folder
os.makedirs(destination_folder, exist_ok=True)

for _, row in df.iterrows():
    image_id = str(row["id"]) + ".jpg"
    category = str(row["subCategory"]).replace("/", "-")

    source = os.path.join(source_folder, image_id)
    category_folder = os.path.join(destination_folder, category)

    os.makedirs(category_folder, exist_ok=True)

    destination = os.path.join(category_folder, image_id)

    if os.path.exists(source):
        shutil.copy(source, destination)

print("Dataset organized successfully!")