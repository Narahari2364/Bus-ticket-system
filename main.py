from file_handler import load_ticket_data, get_unique_categories, load_ticket_objects

def display_menu():
    """Display main menu options"""
    print("\n" + "="*40)
    print("   BUS TICKET PURCHASE SYSTEM")
    print("="*40)
    print("1. View Ticket Categories")
    print("2. Search Top-ups")
    print("3. Purchase Ticket")
    print("4. View My Purchases")
    print("5. Exit")
    print("="*40)

def view_categories_v2(categories):
    """Display categories using Category objects"""
    if not categories:
        print("No categories available.")
        return
    
    print("\n" + "="*40)
    print("   AVAILABLE TICKET CATEGORIES")
    print("="*40)
    
    cat_list = list(categories.values())
    
    for i, category in enumerate(cat_list, 1):
        print(f"{i}. {category}")  # Uses __str__ method
    
    print("="*40)
    
    try:
        choice = input("\nEnter category number for details (or Enter to return): ")
        
        if choice.strip():
            index = int(choice) - 1
            
            if 0 <= index < len(cat_list):
                cat_list[index].display_info()  # Uses display_info method
            else:
                print("Invalid number!")
                
    except ValueError:
        print("Please enter a valid number!")

def main():
    """Main program loop"""
    # Load ticket data as objects organized by category
    categories = load_ticket_objects('data/bus_tickets.csv')
    
    if not categories:
        print("Cannot run without ticket data. Exiting.")
        return
    
    while True:
        display_menu()
        
        try:
            choice = input("\nEnter your choice (1-5): ")
            
            if choice == "1":
                view_categories_v2(categories)
            elif choice == "2":
                print("Search top-ups - Coming soon!")
            elif choice == "3":
                print("Purchase - Coming soon!")
            elif choice == "4":
                print("View purchases - Coming soon!")
            elif choice == "5":
                print("Thank you for using Bus Ticket System!")
                break
            else:
                print("Invalid choice! Please enter 1-5.")
                
        except KeyboardInterrupt:
            print("\nProgram interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
