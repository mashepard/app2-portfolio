import streamlit as st

st.header("Contact Mark Shepard")

with st.form(key="email_form"):
    user_email = st.text_input("Enter your email address: ")
    message = st.text_area("Your message: ")
    button = st.form_submit_button("Submit")
    if button:
        message = mesage + user_email