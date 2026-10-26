import pandas as pd

df = pd.read_csv("air_quality_raw.csv")

# Suppression des lignes vides
df = df.dropna()

# Conversion de la date
df["time"] = pd.to_datetime(df["time"])

# Suppression des doublons
df = df.drop_duplicates()

df.to_csv("air_quality_clean.csv", index=False)

print("Transformation terminée")
print(df.head())