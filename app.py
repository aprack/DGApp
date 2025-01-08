import pandas as pd
import streamlit as st

# Load the CSV file
df = pd.read_csv(r"https://raw.githubusercontent.com/aprack/DGApp/refs/heads/main/dgdiscs.csv")

st.title("Disc Flight Number Search")
column = st.selectbox("Choose a column to filter:",df.loc[:,['Speed', 'Glide', 'Turn', 'Fade']))
value = st.number_input(f"Enter the value to filter in {column}:")

if st.button("Search"):
    results = df[df[column] == value]
    st.write(results)
