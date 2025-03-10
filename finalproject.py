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
    df["date_time"] = pd.to_datetime(df["date_time"], errors="coerce")
    df["year"] = df["date_time"].dt.year  # Extract year

st.markdown("---")

# --- 1. Animated Bubble Plot: Magnitude vs. Depth Over Time ---
st.subheader("1. Animated Bubble Plot: Magnitude vs. Depth Over Time")
st.markdown("""
**Chart Description:**  
- **X-axis:** Earthquake Magnitude  
- **Y-axis:** Depth (km)  
- **Bubble Size:** Signal Strength (sig)  
- **Bubble Color:** Modified Mercalli Intensity (mmi)  
- **Animation Slider:** Filters data by year  
""")

# Create an animated scatter plot
fig = px.scatter(
    df,
    x="magnitude",
    y="depth",
    size="sig",
    color="mmi",
    hover_data=["date_time", "location"],
    animation_frame="year",           
    animation_group="location",       
    range_x=[df["magnitude"].min(), df["magnitude"].max()],
    range_y=[df["depth"].min(), df["depth"].max()],
    title="Earthquake: Magnitude vs. Depth (Animated by Year)",
    template="plotly_white"
)

fig.update_layout(
    xaxis_title="Magnitude",
    yaxis_title="Depth (km)"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown(""" 
**Interpretation:**  
- Larger bubbles indicate earthquakes with higher signal strength.  
- Deeper colors represent stronger perceived shaking (higher MMI).  
- Use the slider to see how earthquake distribution changes from year to year.
""")

st.markdown("---")

# --- 2. Choropleth: Earthquake Distribution by Country (Log Scale) ---
st.subheader("2. Choropleth: Earthquake Distribution by Country (Log Scale)")
st.markdown("""
**Chart Description:**  
- Displays a global map of earthquake distribution by country.  
- **Color (Log Scale):** Represents the total number of earthquakes recorded in each country, transformed via `log(1 + x)`.  
- **Hover Data:** Shows the country name, original earthquake count, and average magnitude.  
""")

# Ensure 'country' column exists
if "country" not in df.columns:
    st.error("The dataset does not contain a 'country' column. Cannot create Choropleth map.")
else:
    df["country"] = df["country"].fillna("Unknown")
    df_country = df.groupby("country", as_index=False).agg(
        earthquake_count=("magnitude", "size"),
        avg_magnitude=("magnitude", "mean")
    )

    # Create a new column for the log-transformed earthquake counts
    df_country["log_count"] = np.log1p(df_country["earthquake_count"])

    # Use log_count for the color scale
    fig_choro = px.choropleth(
        df_country,
        locations="country",
        locationmode="country names",
        color="log_count",
        hover_name="country",
        hover_data={
            "earthquake_count": True,
            "avg_magnitude": True,
            "log_count": False
        },
        color_continuous_scale="Viridis",
        range_color=(df_country["log_count"].min(), df_country["log_count"].max()),
        scope="world",
        title="Global Earthquake Distribution by Country (Log Scale)"
    )

    # **Modify Layout to Increase Map Size**
    fig_choro.update_layout(
        geo=dict(
            showframe=False,
            showcoastlines=True,
            projection_type="natural earth"
        ),
        title_x=0.5,  # Center the title
        height=600,   # **Increase height**
        width=1200    # **Increase width**
    )

    st.plotly_chart(fig_choro, use_container_width=True)
    
st.markdown("""  
**Interpretation:**  
- Darker colored countries indicate a higher frequency of earthquakes.  
- Hovering over a country displays detailed statistics, including the average magnitude, which helps assess the overall seismic intensity.  
- Using a log transform helps differentiate regions with relatively low but nonzero earthquake counts, avoiding an overly uniform map.
""")

# **Add Author Name**
st.markdown("### Created by: Jiayi Zeng")
