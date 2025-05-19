import streamlit as st
import pandas as pd
import pydeck as pdk

# Data (latitude, longitude, plastic_in_tons)
data = {
    "lat": [28.19, -31.45, 34.56, -5.35, 12.07],
    "lon": [-121.71, -64.12, 139.68, 105.43, -61.28],
    "plastic_tons": [200, 450, 800, 150, 300],
    "location": [
        "North Pacific",
        "South Atlantic",
        "Western Pacific",
        "Indian Ocean",
        "Caribbean Sea"
    ]
}

df = pd.DataFrame(data)

# App structure
st.title("Ocean Pollution Map")
st.write("Hover over a map point to see pollution details.")

# Define the PyDeck layer with interactive capabilities
layer = pdk.Layer(
    "ScatterplotLayer",
    df,
    get_position=["lon", "lat"],
    get_radius=50000,
    get_fill_color=[255, 0, 0],
    pickable=True,  # Enables interactivity
)

# Set up the initial view
view_state = pdk.ViewState(latitude=df["lat"].mean(), longitude=df["lon"].mean(), zoom=2)

# Add a tooltip to display pollution info when hovering/clicking
deck = pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    tooltip={"text": "{location}: {plastic_tons} tons of plastic pollution"}
)

# Render the map with interactivity
st.pydeck_chart(deck)

# User coordinate input
col1, col2 = st.columns(2)
with col1:
    lat = st.number_input("Enter latitude", min_value=-90.0, max_value=90.0, value=0.0)
with col2:
    lon = st.number_input("Enter longitude", min_value=-180.0, max_value=180.0, value=0.0)

# Find closest pollution point based on input coordinates
if st.button("Show Pollution Data"):
    closest = df.iloc[((df['lat'] - lat)**2 + (df['lon'] - lon)**2).idxmin()]

    st.subheader(f"Pollution Report for {closest['location']}:")
    st.metric("Plastic Pollution", f"{closest['plastic_tons']} tons")
    st.write(f"Coordinates: {closest['lat']:.2f}°N, {closest['lon']:.2f}°E")
    st.image("https://cdn.pixabay.com/photo/2020/04/17/19/48/pollution-5056223_960_720.jpg", width=300)