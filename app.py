import pandas as pd
import streamlit as st

# Load the CSV file
df = pd.read_csv(r"https://raw.githubusercontent.com/aprack/DGApp/refs/heads/main/pdga-approved-disc-golf-discs_2025-01-08T15-27-01.csv")

st.title("CSV Query App")
column = st.selectbox("Choose a column to filter:", df.columns)
value = st.text_input(f"Enter the value to filter in {column}:")

if st.button("Search"):
    results = df[df[column] == value]
    st.write(results)
