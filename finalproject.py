import streamlit as st
import pandas as pd
import numpy as np

# Read CSV data
df = pd.read_csv("earthquake_1995-2023.csv")

# Define a set of valid country names that Plotly recognizes (customize as needed)
valid_countries = {
    "Vanuatu", "Argentina", "El Salvador", "Antigua and Barbuda", "Papua New Guinea",
    "Colombia", "Indonesia", "Russia", "Turkey", "United States of America", "Brazil",
    "Mexico", "Taiwan", "Philippines", "Peru", "New Zealand", "Afghanistan", "Ecuador",
    "Tajikistan", "Fiji", "Costa Rica", "Iran", "Guatemala", "Canada"
}

# Define a dictionary mapping keywords from the 'location' field to recognized countries
location_to_country = {
    "Sola": "Vanuatu",
    "Intipucá": "El Salvador",
    "Loncopué": "Argentina",
    "Sand Point": "United States of America",
    "Alaska Peninsula": "United States of America",
    "Antigua": "Antigua and Barbuda",
    "Tonga": "Tonga",
    "the Fiji Islands": "Fiji",
    "Panama-Colombia": "Panama",  # adjust as needed
    "Kermadec Islands": "New Zealand",
    "Teluk Dalam": "Indonesia",
    "Hihifo": "Tonga",
    "Codrington": "Antigua and Barbuda",
    "New Guinea": "Papua New Guinea",
    "San Antonio": "Argentina",
    "Jurm": "Afghanistan",
    "the Kamchatka Peninsula": "Russia",
    "Central Turkey": "Turkey",
    "Pulau Pulau Tanimbar": "Indonesia"
    # Add more mappings as necessary
}

def infer_country(row):
    # If the country field is missing or not in the valid list, infer from location.
    country = row.get("country")
    location = row.get("location", "")
    if pd.isna(country) or (country not in valid_countries):
        for keyword, mapped_country in location_to_country.items():
            if isinstance(location, str) and keyword.lower() in location.lower():
                return mapped_country
        # If no mapping is found, return "Unknown"
        return "Unknown"
    else:
        return country

# Apply the inference function to each row
df["country"] = df.apply(infer_country, axis=1)

# Display the unique country values after cleaning
st.write("Unique countries after cleaning:", df["country"].unique())
