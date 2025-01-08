import pandas as pd
import streamlit as st

# Load the CSV file
df = pd.read_csv(r"https://raw.githubusercontent.com/aprack/DGApp/refs/heads/main/dgdiscs.csv")

# Filter available columns
available_columns = ['Speed', 'Glide', 'Turn', 'Fade']

st.title("Disc Flight Number Search")

# Let users select multiple columns to filter by
selected_columns = st.multiselect("Choose flight numbers to filter by:", available_columns)

# Dictionary to hold user input for each selected column
filter_values = {}

for column in selected_columns:
    value = st.number_input(f"Enter the value to filter in {column}:", format="%d")
    filter_values[column] = value

if st.button("Search"):
    # Start with the full DataFrame
    filtered_df = df
    
    # Apply filters based on user input
    for column, value in filter_values.items():
        filtered_df = filtered_df[filtered_df[column] == value]
    
    # Show results
    if filtered_df.empty:
        st.write("No results found for the given criteria.")
    else:
        st.write(filtered_df)
