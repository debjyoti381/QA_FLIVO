import os

def debug_secrets():
    print("Checking for secrets...")
    for key in ["MY_SECRET_KEY", "ANOTHER_SECRET"]:
        value = os.getenv(key, "NOT FOUND")
        print(f"{key}: {value[:5]}...")  # Show only the first few characters for security

if __name__ == "__main__":
    print("Starting debug...")
    debug_secrets()
