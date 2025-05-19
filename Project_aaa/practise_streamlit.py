import streamlit as st
import pandas as pd

# Sample data
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "City": ["New York", "London", "Paris", "Tokyo"]
}

# Convert dictionary to Pandas DataFrame
df = pd.DataFrame(data)

# Streamlit app
st.title("Simple Streamlit & Pandas App")

# Display DataFrame
st.write("Here is a sample dataset:")
st.dataframe(df)