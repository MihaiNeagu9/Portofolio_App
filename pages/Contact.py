import streamlit as st

st.header("Contact Me")

with st.form(key="email_form"):
    st.text_input("Your email address:")
    st.text_area("Your message:")
    button = st.form_submit_button()
    if button:
        print("Pressed!")