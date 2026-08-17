mport hashlib

# This is the same database dictionary from the sign-up step
user_database = {
    # Example of what the sign-up function saved:
    # "alice@example.com": "d6796c56df278631..."
}

def log_in(email, password):
    # Clean the email input just like we did in sign-up
    email = email.strip().lower()
    
    # 1. Check if the email exists in our database
    if email not in user_database:
        return "Error: Invalid email or password."
    
    # 2. Hash the entered password to see if it matches the stored hash
    # (Because you cannot un-scramble the stored password to read it)
    entered_password_hash = hashlib.sha256(password.encode()).hexdigest()
    stored_password_hash = user_database[email]
    
    # 3. Compare the two hashes
    if entered_password_hash == stored_password_hash:
        return "Success: Logged in successfully!"
    else:
        return "Error: Invalid email or password."

# --- Complete Example Workflow ---

# 1. Sign up Alice
# (This simulates the sign_up function adding data to the dictionary)
alice_password_hash = hashlib.sha256("SuperSecret123".encode()).hexdigest()
user_database["alice@example.com"] = alice_password_hash

# 2. Try to log in with the wrong password
print(log_in("alice@example.com", "WrongPassword")) 
# Output: Error: Invalid email or password.

# 3. Try to log in with the correct password
print(log_in("alice@example.com", "SuperSecret1