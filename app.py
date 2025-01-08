import pandas as pd
import streamlit as st

# Load the CSV file
df = pd.read_csv(r"https://raw.githubusercontent.com/aprack/DGApp/refs/heads/main/dgdiscs.csv")

# Filter available columns
available_columns = ['Speed', 'Glide', 'Turn', 'Fade']

st.title("Disc Flight Number Search")

# Update the selectbox to only include the filtered columns
column = st.selectbox("Choose a column to filter:", available_columns)

# Take user input for the chosen column
value = st.number_input(f"Enter the value to filter in {column}:")

if st.button("Search"):
    # Filter the DataFrame based on the selected column and value
    results = df[df[column] == value]
    st.write(results)
