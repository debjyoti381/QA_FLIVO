import os
import streamlit as st

# Access secrets from environment variables
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

# Display the secrets in Streamlit for testing (remove for production)
st.write("Client ID:", client_id)
st.write("Client Secret:", client_secret)  # Only for testing, remove for security in production
