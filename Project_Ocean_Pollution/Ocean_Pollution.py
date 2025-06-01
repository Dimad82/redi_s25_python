import streamlit as st
import pandas as pd
import pydeck as pdk
import logging

# Set up logging
logging.basicConfig(
    filename="pollution_app.log",  # Save logs in a file
    level=logging.INFO,  # Log INFO-level events and higher
    format="%(asctime)s - %(levelname)s - %(message)s",  # Log format
)

class OceanMap: # shows map of the oceans

# Data for oceans (latitude, longitude, plastic_in_tons)
    def __init__(self):
        logging.info("Initializing PollutionMap class")  # Log when the class

        self.oceans = {
            "lat": [0, 0, 90, -60, -10],
            "lon": [-160, -30, 0, -150, 80],
            "plastic_tons": [223, 461, 802, 149, 299],
            "location": [
                "Pacific",
                "Atlantic",
                "Arctic",
                "Antarctic",
                "Indian Ocean"
            ]
        }

        try:
            # Converts dictionary into DataFrame for the use with PyDeck and Streamlit.
            self.df = pd.DataFrame(self.oceans) 
            logging.info("Data successfully loaded into DataFrame")
        except Exception as e:
            logging.error(f"Error loading data: {e}")
            st.error(f"Error loading data: {e}")
            st.stop()  # Stop execution if data is invalid.

    # Function to display pollution map.
    def show_ocean_map(self): # Shows ocean map using PyDeck.
        st.title("Ocean Pollution Map")
        st.write("One million or more marine animals die in the ocean each year due to plastic pollution.")
        st.write("Hover over a map point to see pollution details.")

        try:
            layer = pdk.Layer(
                "ScatterplotLayer",  # Scatterplot is used for creating red dots
                self.df,
                get_position=["lon", "lat"],  # Map dots from DataFrame
                get_radius=50000,  # It shows the radius of red dots that users should click. But they're very small.
                get_fill_color=[255, 0, 0],  # It gives the color to dots in red
                pickable=True,  # Helps to hover over red dots
            )

            # Sets the view of the map
            # Latitude and longitude (moved to the left for 15 degrees)
            # and zoom 0.2 so that whole map can be displayed.
            view_state = pdk.ViewState(latitude=self.df["lat"].mean(), longitude=-15, zoom=0.2)

            # Shows text when hovering over the dots
            deck = pdk.Deck(
                layers=[layer],
                initial_view_state=view_state,
                tooltip={"text": "{location}: {plastic_tons} tons of plastic pollution"}
            )

            # Renders the map in Streamlit web application
            st.pydeck_chart(deck)
            logging.info("Pollution map displayed successfully")
        except Exception as e:
            logging.error(f"Error displaying pollution map: {e}")
            st.error(f"Error displaying pollution map: {e}")

class RecycleQuestionnaire: # Everything is together with class to look better for questionnaire.
    def __init__(self): # Starts the questionnaire session.
        logging.info("Initializing RecyclingQuestion class")  # Log when initialized
        if "recycling_response" not in st.session_state:
            st.session_state.recycling_response = None

    def ask_recycle_questionnaire(self): #Displays recycling question and stores response. Button
        try:
            st.button("Do you recycle?", key="recycle_btn")

            # Store the answer, otherwise it shows always "Yes" and when "No" is clicked is permanently gone.
            if "recycling_response" not in st.session_state:
                st.session_state.recycling_response = None
        
            # Allow the user to select an option from dropdown menu
            user_response = st.selectbox("Choose an option:", ["Select", "Yes", "No"])

            # Saves the user's choice in st.session_state
            if user_response != "Select":
                st.session_state.recycling_response = user_response  

            # Display message after selection
            if st.session_state.recycling_response == "Yes":
                st.success("Excellent! Keep reducing waste and protecting our oceans! 🍃♻️🏞️💚🌱")
                logging.info("User selected 'Yes' for recycling question")
            elif st.session_state.recycling_response == "No":
                logging.warning("User selected 'No' for recycling question")
                st.warning("Don't be like that. Start now! Look how much garbage is in the oceans. 🤌🏻🌍🌡️🥵")

        except Exception as e:
            logging.error(f"Error processing recycling question: {e}")
            st.error(f"Error processing recycling question: {e}")

# Main function that calls two functions
def main():
    try:
        logging.info("Starting Pollution Oceans App")  # Log app start
        ocean_map = OceanMap() # Instantiate ocean pollution map
        ocean_map.show_ocean_map()

        recycle_questionnaire = RecycleQuestionnaire() # Instantiate recycling question
        recycle_questionnaire.ask_recycle_questionnaire()
    except Exception as e:
        logging.critical(f"Unexpected error in application: {e}")  # Log sever
        st.error(f"Unexpected error in application: {e}")

if __name__ == "__main__":
    main()