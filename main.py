import streamlit as st
# import login

# Import necessary functions from web_functions
from web_functions import load_data

# Import pages
from Tabs import home, data, predict, visualise, community, consultation

# Dictionary for pages
Tabs = {
    "Home": home,
    "Data Info": data,
    "Prediction": predict,
    "Visualisation": visualise,
    "Community": community,
    "Consultation": consultation
}

# Create a sidebar
# Add title to sidebar
st.sidebar.title("Navigation")

# Loading the dataset.
df, X, y = load_data()

# Create radio option to select the page
page = st.sidebar.radio("Pages", list(Tabs.keys()))

# Call the app function of selected page to run
if page in ["Prediction", "Visualisation"]:
    Tabs[page].app(df, X, y)
elif (page == "Data Info"):
    Tabs[page].app(df)
else:
    Tabs[page].app()
