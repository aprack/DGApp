import pandas as pd
import streamlit as st

# Load the CSV file
df = pd.read_csv(r"https://github.com/aprack/DGApp/blob/bc46c1892a18a8e4a7a76b00b906688b35b9f753/pdga-approved-disc-golf-discs_2025-01-08T15-27-01.csv")

st.title("CSV Query App")
column = st.selectbox("Choose a column to filter:", df.columns)
value = st.text_input(f"Enter the value to filter in {column}:")

if st.button("Search"):
    results = df[df[column] == value]
    st.write(results)
