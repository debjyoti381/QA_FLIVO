import os
import streamlit as st

# Access secrets from environment variables
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

# Displaying environment variables
st.title("Environment Variables Loaded from GitHub Secrets")

st.subheader("Google Project Information")
st.write("CLIENT_ID:", client_id)
st.write("CLIENT_SECRET:", client_secret)  # Only for testing; remove in production for security

if client_id and client_secret:
    st.success("Secrets loaded successfully!")
else:
    st.error("Failed to load secrets. Check GitHub secrets configuration.")
