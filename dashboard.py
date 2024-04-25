import streamlit as st

# Create a title for the login page
st.title("Login Page")

# Create fields for user input
username = st.text_input("Username")  # Requires a label
password = st.text_input("Password", type="password")  # Requires a label; type="password" hides the text

# Button for login
login_button = st.button("Login")

choice1 = st.number_input('Enter First number')  #Accepts a number input
choice2 = st.number_input('Enter Second number')
choice3 = st.number_input('Enter Third number')
