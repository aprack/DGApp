import pandas as pd

# Specify the file path
file_path = r"C:\Users\Drubert\Documents\pdga-approved-disc-golf-discs_2025-01-08T15-27-01.csv"

try:
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Display the first few rows
    print("\nPreview of the CSV file:")
    print(df.head())

    # Query the data
    column = input("\nEnter the column name to filter by: ")
    value = input(f"Enter the value to search for in '{column}': ")

    # Filter the DataFrame
    filtered = df[df[column].astype(str).str.contains(value, case=False, na=False)]
    print(f"\nResults:\n{filtered}")

except FileNotFoundError:
    print(f"Error: The file at '{file_path}' was not found.")
except KeyError:
    print(f"Error: The column name '{column}' does not exist in the CSV.")
except Exception as e:
    print(f"An error occurred: {e}")
