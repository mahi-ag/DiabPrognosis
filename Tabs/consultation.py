import streamlit as st
import pandas as pd
import os

def app():
    # Title for the page with custom font and color
    st.markdown("<h1 style='text-align: center; color: #ff6347; font-family: Arial, sans-serif;'>Expert Consultation</h1>", unsafe_allow_html=True)

    # Sidebar with rounded corners and background color
    st.sidebar.title('User Information')
    st.sidebar.markdown("---")
    name = st.sidebar.text_input('Name', '')
    age = st.sidebar.number_input('Age', min_value=0, max_value=150, value=30)
    gender = st.sidebar.selectbox('Gender', ['Male', 'Female'])

    # Main content area with rounded corners and shadow
    st.subheader('Consultation Request')
    symptoms = st.text_area('Describe your symptoms:', height=200)
    additional_info = st.text_area('Any additional information or questions:', height=100)

    # Button styled with custom background color and rounded corners
    if st.button('Request Consultation'):
        st.success('Consultation request sent successfully!')
        # Save consultation data to CSV
        save_consultation_data(name, age, gender, symptoms, additional_info)


def save_consultation_data(name, age, gender, symptoms, additional_info):
    # Create DataFrame with consultation data
    consultation_data = pd.DataFrame({
        'Name': [name],
        'Age': [age],
        'Gender': [gender],
        'Symptoms': [symptoms],
        'Additional Info': [additional_info]
    })

    # Check if the file exists
    file_path = 'consult.csv'
    if os.path.isfile(file_path):
        # Append data to existing file
        consultation_data.to_csv(file_path, mode='a', header=False, index=False)
    else:
        # Create new file
        consultation_data.to_csv(file_path, index=False)
