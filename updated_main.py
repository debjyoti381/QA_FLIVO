import os

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

print("Client ID:", client_id)
print("Client Secret:", client_secret)  # For testing; remove in production for security
