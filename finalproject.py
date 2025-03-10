import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

# Set page configuration
st.set_page_config(page_title="Earthquake Data Visualization", page_icon=":bar_chart:", layout="wide")

st.title("Earthquake Data Visualization")
# Display the dataset source at the top
st.markdown("### **Source of Data:** [Kaggle Earthquake Dataset](https://www.kaggle.com/datasets/warcoder/earthquake-dataset)")

st.markdown("""
This dashboard visualizes global earthquake data from 1995 to 2023, including magnitude, depth, signal strength (sig), Modified Mercalli Intensity (mmi), date/time, and location.  
Below you will find **two** interactive visualizations that provide different perspectives on earthquake characteristics and their distribution:
1. **Animated Bubble Plot:** Displays the relationship between earthquake magnitude and depth, with a year slider.
2. **Choropleth Map:** Shows the global distribution of earthquakes by country.
""")

# Read CSV data
df = pd.read_csv("earthquake_1995-2023.csv")

# Check for required columns in the dataset
required_columns = ["magnitude", "depth", "sig", "mmi", "date_time", "location"]
missing_cols = [col for col in required_columns if col not in df.columns]
if missing_cols:
    st.error(f"The dataset is missing the following required columns: {missing_cols}")
    st.stop()
else:
    # Convert columns to numeric
    df["magnitude"] = pd.to_numeric(df["magnitude"], errors="coerce")
    df["depth"] = pd.to_numeric(df["depth"], errors="coerce")
    df["sig"] = pd.to_numeric(df["sig"], errors="coerce")
    df["mmi"] = pd.to_numeric(df["mmi"], errors="coerce")
    
    # Convert date_time to datetime and create a 'year' column for animation
    df["date_time"] = pd.to_datetime(df
