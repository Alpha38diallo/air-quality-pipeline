import streamlit as st
import pandas as pd

st.title("Air Quality Dashboard")

try:
    df = pd.read_csv("air_quality_clean.csv")

    st.subheader("Aperçu des données")
    st.dataframe(df.head())

    if "pm10" in df.columns:
        st.subheader("Évolution du PM10")
        st.line_chart(df["pm10"])

except Exception as e:
    st.error(f"Erreur : {e}")