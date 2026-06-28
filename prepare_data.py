import pandas as pd

# Load dataset
df = pd.read_csv("dataset/styles.csv", on_bad_lines="skip")

# Keep only rows that have an image
df = df[df["id"].apply(lambda x: True)]

# Keep only the required columns
df = df[["id", "subCategory"]]

print(df.head())
print("Total Records:", len(df))
print("Unique Categories:", df["subCategory"].nunique())