from file_handler import load_ticket_data, get_unique_categories

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

def view_categories(ticket_data):
    """Display all available ticket categories"""
    categories = get_unique_categories(ticket_data)
    
    if not categories:
        print("No categories available.")
        return
    
    print("\n" + "="*40)
    print("   AVAILABLE TICKET CATEGORIES")
    print("="*40)
    
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")
    
    print("="*40)
    
    # Ask if user wants details
    try:
        choice = input("\nEnter category number for details (or press Enter to return): ")
        
        if choice.strip():  # If user entered something
            index = int(choice) - 1
            
            if 0 <= index < len(categories):
                view_category_details(ticket_data, categories[index])
            else:
                print("Invalid category number!")
                
    except ValueError:
        print("Please enter a valid number!")
    except Exception as e:
        print(f"Error: {e}")

def view_category_details(ticket_data, category_name):
    """Show all top-ups for a specific category"""
    print(f"\n--- Details for {category_name} ---")
    
    # Filter tickets for this category
    category_tickets = [t for t in ticket_data if t.get('Category') == category_name]
    
    if not category_tickets:
        print("No tickets found for this category.")
        return
    
    for ticket in category_tickets:
        print(f"\nTop-up Type: {ticket.get('TopUpType', 'N/A')}")
        print(f"Price: £{ticket.get('Price', 'N/A')}")
        print(f"Duration: {ticket.get('Duration', 'N/A')}")
        print("-" * 30)

def main():
    """Main program loop"""
    # Load ticket data at startup
    ticket_data = load_ticket_data('data/bus_tickets.csv')
    
    if not ticket_data:
        print("Cannot run without ticket data. Exiting.")
        return
    
    while True:
        display_menu()
        
        try:
            choice = input("\nEnter your choice (1-5): ")
            
            if choice == "1":
                view_categories(ticket_data)
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
