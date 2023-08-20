import streamlit as st
import time
from Send_email import send_email

st.title("Contact Me")
with st.form(key="Contact_form"):
    email=st.text_input("Email:",placeholder="Write your Email here.",key="email")
    message=st.text_area(label='Message:',placeholder="Type Your Message",height=100)
    button=st.form_submit_button("Submit")
    if button:
        send_email(message,email)
        placeholder=st.empty()
        placeholder.success("Submitted")
        time.sleep(2)
        placeholder.empty()