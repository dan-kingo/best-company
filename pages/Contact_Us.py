import streamlit as st
from send_email import send_email

st.title("Contact Us ")
options = ['Job Inquires', 'Project Proposal', "Other"]
with st.form(key="email_form"):
    user_email = st.text_input("Your Email Address", placeholder="your email")
    selected_option = st.selectbox("What topic do you want to discuss?", options)
    raw_message = st.text_area("Your Message", placeholder="type here...")
    message = f"""\
    Subject:{selected_option}

    From: {user_email} 
    {raw_message}
        """
    button = st.form_submit_button("Submit")

    if button:
        send_email(message)

        st.write("Email sent successfully!")
