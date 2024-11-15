import os

def deploy():
    # Fetch the secret from environment variable
    secret_key = os.getenv("MY_SECRET_KEY")
    if secret_key:
        print(f"Deploying with secret key: {secret_key}")
        # Add your deployment logic here (e.g., API calls, file setup, etc.)
    else:
        print("Secret key not found. Ensure MY_SECRET_KEY is set in GitHub Secrets.")

if __name__ == "__main__":
    print("Starting deployment...")
    deploy()
