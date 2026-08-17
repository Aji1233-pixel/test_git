def show_welcome_page(email):
    """
    File 3: Welcome Screen Function
    Displays a personalized dashboard for the logged-in user.
    """
    # 1. Cleanly extract the name from the email (e.g., 'sam@email.com' -> 'Sam')
    raw_name = email.split('@')[0]
    username = raw_name.capitalize()
    
    # 2. Display the UI
    print("\n" + "=" * 35)
    print(f"🎉  WELCOME TO YOUR DASHBOARD, {username}!  🎉")
    print("=" * 35)
    print("1. View Profile Details")
    print("2. Log Out")
    print("=" * 35)
    
    # 3. Handle user input
    choice = input("Select an option (1-2): ").strip()
    
    if choice == "1":
        print(f"\n👤 [Profile Data]")
        print(f"Registered Email: {email}")
        input("\nPress Enter to return to menu...")
        return show_welcome_page(email)  # Keep the loop open
        
    elif choice == "2":
        print("\nLogging you out safely... Goodbye!")
        return "Logged Out"  # Tells File 4 that the session is ended
        
    else:
        print("\n❌ Invalid choice! Please enter 1 or 2.")
        return show_welcome_page(email)  # Reloads menu for incorrect choice
