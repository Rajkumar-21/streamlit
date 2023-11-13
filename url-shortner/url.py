# Import streamlit and requests libraries
import streamlit as st
import requests
import pyshorteners

# Create a title and a text input for the URL
st.title("URL Checker and Shortener")
url = st.text_input("Enter a URL to check and shorten:")

# Create a button to submit the URL
if st.button("Submit"):
    try:
        # Get the response from the URL
        response = requests.get(url)
        # Display the status code and the final URL
        st.write(f"Status code: {response.status_code}")
        st.write(f"Final URL: {response.url}")

        # Initialize the URL shortener
        s = pyshorteners.Shortener()

        # Shorten the URL using TinyURL
        short_url = s.tinyurl.short(url)
        st.write(f"Shortened URL: {short_url}")

    except Exception as e:
        st.error(f"Invalid URL or network error: {e}")
