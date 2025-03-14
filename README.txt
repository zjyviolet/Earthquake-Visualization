# Earthquake Data Visualization

## Overview
This project presents an **interactive earthquake data visualization dashboard** using **Streamlit** and **Plotly Express**. It enables users to explore seismic activity trends from **1995 to 2023** through **dynamic and geospatial visualizations**.

## Features
1. **Animated Bubble Plot**  
   - Visualizes the **magnitude-depth** relationship of earthquakes over time.  
   - Uses **bubble size** to represent **signal strength (sig)** and **color** to indicate **Modified Mercalli Intensity (mmi)**.  
   - A **year slider** allows for interactive time-based exploration.  

2. **Choropleth Map**  
   - Displays **earthquake occurrences at the country level**.  
   - Uses a **log-transformed scale** to balance frequency distribution.  
   - Interactive **hover tooltips** provide statistics on earthquake count and average magnitude per country.  

## Dataset  
- **Source**: [Kaggle Earthquake Dataset](https://www.kaggle.com/datasets/warcoder/earthquake-dataset)  
- **File Used**: `earthquake_1995-2023.csv`  
- The dataset includes **magnitude, depth, signal strength (sig), mmi, date/time, and location** for global earthquakes.  

## Installation & Setup  
### 1. Clone the Repository  
```bash
git clone https://github.com/yourusername/earthquake-visualization.git
cd earthquake-visualization
```

### 2. Create a Virtual Environment  
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies  
```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application  
```bash
streamlit run app.py
