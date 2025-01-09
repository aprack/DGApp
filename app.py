import pandas as pd
import streamlit as st

# Load the CSV file
df = pd.read_csv(r"https://raw.githubusercontent.com/aprack/DGApp/refs/heads/main/dgdiscs.csv")

# Ensure the data types of relevant columns are numeric where needed
available_columns = ['Company', 'Disc', 'Speed', 'Glide', 'Turn', 'Fade']
for col in ['Speed', 'Glide', 'Turn', 'Fade']:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

st.title("Disc Search")

# Let users select multiple columns to filter by
selected_columns = st.multiselect("Choose columns to filter by:", available_columns)

# Dictionary to hold user input for each selected column
filter_values = {}

for column in selected_columns:
    if column in ['Speed', 'Glide', 'Turn', 'Fade']:
        # For numeric columns
        value = st.number_input(f"Enter the value to filter in {column}:", step=0.1, format="%.1f")
    else:
        # For text-based columns
        value = st.text_input(f"Enter the text to filter in {column}:")
    filter_values[column] = value

if st.button("Search"):
    # Start with the full DataFrame
    filtered_df = df
    
    # Apply filters based on user input
    for column, value in filter_values.items():
        if column in ['Speed', 'Glide', 'Turn', 'Fade']:
            # Numeric filter
            filtered_df = filtered_df[filtered_df[column] == value]
        else:
            # Text filter (case-insensitive)
            filtered_df = filtered_df[filtered_df[column].str.contains(str(value), case=False, na=False)]
    
    # Restrict the displayed columns to selected ones
    filtered_df = filtered_df[selected_columns]
    
    # Show results
    if filtered_df.empty:
        st.write("No results found for the given criteria.")
    else:
        st.write(filtered_df)
