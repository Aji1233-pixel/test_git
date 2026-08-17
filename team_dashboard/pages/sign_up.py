import hashlib
# A dictionary to simulate our database (Email -> Hashed Password)
user_database = {}

def sign_up(email, password):
    # Ensure fields are not empty
    if not email or not password:
        return "Error: Email and password cannot be empty."
    
    # Clean the email input
    email = email.strip().lower()
    
    # 1. Check if the user already exists
    if email in user_database:
        return "Error: An account with this email already exists."
    
    # 2. Secure the password (Never store plain-text passwords!)
    # We convert the password to bytes and create a secure SHA-256 hash
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    # 3. Save to our database
    user_database[email] = hashed_password
    return "Success: Account created successfully!"

# --- Example Usage ---
print(sign_up("alice@example.com", "SuperSecret123")) 
# Output: Success: Account created successfully!

print(sign_up("alice@example.com", "DifferentPassword")) 
# Output: Error: An account with this email already exists.
