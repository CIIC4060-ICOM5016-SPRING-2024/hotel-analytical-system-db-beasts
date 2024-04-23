import streamlit
from IPython.core.display_functions import clear_output
import ipywidgets as widgets
from IPython.display import display
import requests
import streamlit as st

# header_text = widgets.HTML(
#     "<h1 style='text-align: center; color: white; background-color: #333; width: 100%; margin: 0; padding: 15px "
#     "0;'>Hotel Analytics Systems by DB Beasts</h1>")
# display(header_text)

# """
# ------------------
# * LOGIN
# ------------------
# """


def Check_Login(username, password):
    # flask_url = "https://db-beasts-7827ce232282.herokuapp.com/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts
    # /login/voila"
    flask_url = "http://127.0.0.1:5000/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts/login/voila"
    credentials = {'username': username, 'password': password}
    response = requests.post(flask_url, json=credentials)
    return response


def Check_Employee(eid, fname, lastname):
    flask_url = "http://127.0.0.1:5000/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts/employee/voila"
    data = {'eid': eid, 'fname': fname, 'lname': lastname}
    response = requests.post(flask_url, json=data)
    return response


def Post_Login(eid, username, password):
    flask_url = "http://127.0.0.1:5000/ec2-54-152-144-84.compute-1.amazonaws.com/db-beasts/login"
    data = {'eid': eid, 'username': username, 'password': password}
    response = requests.post(flask_url, json=data)
    return response


# ** Switch between log in and sign in input credentials
def change_view1(button):
    with output:
        clear_output()
        if button.description == 'Sign Up':
            button.description = 'Log In'
            login_box.children = [employee_id, first_name, last_name, username, password, sign_up_button]
        else:
            button.description = 'Sign Up'
            login_box.children = [username, password, login_button]


def change_view2(button):
    with output:
        clear_output()
        login_box.children = [username, password, login_button]
        toggle_button.description = 'Sign Up'
        toggle_button.layout.visibility = 'visible'


# ** Login Credentials
def login():
    # ** Login Logic
    with output:
        response = Check_Login(username.value, password.value)
        if response.status_code == 200:  # Check if the request was successful
            clear_output()
            print(f"Login successful, Welcome!")
            login_box.children = [username, password, logout_button]
            toggle_button.layout.visibility = 'hidden'
        else:
            clear_output()
            print(f"Login failed. Please try again. username: {username.value}, password: {password.value}")


# ** Signup Credentials
def signup(button):
    # ** Signup Logic
    with output:
        employee = Check_Employee(employee_id.value, first_name.value, last_name.value)
        if employee.status_code == 200:
            post_login = Post_Login(employee_id.value, username.value, password.value)
            if post_login.status_code == 201:
                clear_output()
                print(f"Sign up successful, Welcome!")
                login_box.children = [username, password, logout_button]
                toggle_button.layout.visibility = 'hidden'
            elif post_login.status_code == 400:
                clear_output()
                print(f"Employee have account")
            else:
                clear_output()
                print(f"Username exist.")
        else:
            clear_output()
            print(f"Employee does not exist. {employee_id.value}, {first_name.value}, {last_name.value}")


# ** Login Widgets
username = streamlit.text_input("Username")
password = streamlit.text_input("Password")
login_button = st.button("Log In")
# login_button.on_click(login)
if login_button:
    login()


# ** Sigin Widgets
employee_id = streamlit.text_input('Employee ID')
first_name = streamlit.text_input('First Name')
last_name = streamlit.text_input('Last Name')
sign_up_button = st.button("Sign Up")
# sign_up_button.on_click(signup)

logout_button = st.button("Log Out")
# logout_button.on_click(change_view2)

# ** Initial State
login_box = widgets.VBox([username, password, login_button])

# ** Switch between log in and sign in credentials
toggle_button = widgets.Button("Sign Up")
toggle_button.on_click(change_view1)

output = widgets.Output()
display(output)

display(login_box)
display(toggle_button)
