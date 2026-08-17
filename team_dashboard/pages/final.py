# Import the functions created by your team members
# (Assumes the file names match the function names exactly)
from sign_up import sign_up
from login import log_in
from welcome import show_welcome_page

# Shared database dictionary passed into the functions so they share data
user_database = {}

def main_menu():
    """
    Main system loop that coordinates all separate files.
    """
    while True:
        print("\n" + "=== MAIN ACCESS PORTAL ===")
        print("1. Create New Account (Sign Up)")
        print("2. Access Existing Account (Log In)")
        print("3. Exit System")
        print("==========================")
        
        choice = input("Please select an action (1-3): ").strip()
        
        if choice == "1":
            # 1. Run Member 1's Sign Up Logic
            print("\n--- Account Registration ---")
            email = input("Enter email: ")
            password = input("Enter password: ")
            
            # Call sign-up function and pass the database
            result = sign_up(email, password, user_database)
            print(result)
            
        elif choice == "2":
            # 2. Run Member 2's Log In Logic
            print("\n--- System Login ---")
            email = input("Enter email: ")
            password = input("Enter password: ")
            
            # Call login function. Expects True/False or the email back if successful
            login_success = log_in(email, password, user_database)
            
            if login_success:
                # 3. If login succeeds, trigger Member 3's Welcome Screen
                show_welcome_page(email)
            else:
                print("\n❌ Login failed. Please check your credentials.")
                
        elif choice == "3":
            print("\nShutting down system. Goodbye!")
            break
            
        else:
            print("\n❌ Invalid command. Please select 1, 2, or 3.")

# This ensures the menu only runs if this file is executed directly
if __name__ == "__main__":
    main_menu()