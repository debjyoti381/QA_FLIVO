import os
import streamlit as st

# Access the secrets from environment variables
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

# Display the secrets (for testing purposes only)
st.write("Client ID:", client_id)
st.write("Client Secret:", client_secret)  # Remove this line for production
