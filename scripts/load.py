import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///data/air_quality.db"
)

df = pd.read_csv("air_quality_clean.csv")

df.to_sql(
    "air_quality",
    engine,
    if_exists="replace",
    index=False
)

print("Chargement terminé")
print(f"{len(df)} lignes importées")