# ============================================================================
# BUS TICKET PURCHASE SYSTEM - MAIN PROGRAM
# ============================================================================
# This is the main file that runs the bus ticket purchase system.
# It imports functions from other files and creates the menu system.
# ============================================================================

# Import functions from our other files
from file_handler import load_ticket_objects, save_purchase, load_purchases
from ticket_classes import Purchase
from collections import Counter
from admin import admin_panel


# ============================================================================
# FUNCTION 1: DISPLAY MENU
# ============================================================================
# This function shows the user all available options in the program
# ============================================================================
def display_menu():
    """Show the main menu to the user"""
    print("\n" + "="*40)
    print("   BUS TICKET PURCHASE SYSTEM")
    print("="*40)
    print("1. View Ticket Categories")
    print("2. Search Top-ups")
    print("3. Purchase Ticket")
    print("4. View My Purchases")
    print("5. View Purchase Statistics")
    print("6. Admin Panel")
    print("7. Exit")
    print("="*40)


# ============================================================================
# FUNCTION 2: VIEW CATEGORIES
# ============================================================================
# This function shows all ticket categories and lets user see tickets in each
# ============================================================================
def view_categories(categories):
    """Show all ticket categories and let user browse tickets"""
    
    # Check if we have any categories
    if not categories:
        print("No categories available.")
        return
    
    # Display header
    print("\n" + "="*40)
    print("   AVAILABLE TICKET CATEGORIES")
    print("="*40)
    
    # Convert dictionary to list so we can number them
    category_list = list(categories.values())
    
    # Show each category with a number
    for number, category in enumerate(category_list, 1):
        print(f"{number}. {category}")
    
    print("="*40)
    
    # Ask user if they want to see details
    try:
        user_input = input("\nEnter category number for details (or Enter to return): ")
        
        # If user entered something (not just pressed Enter)
        if user_input.strip():
            # Convert to number (subtract 1 because list starts at 0)
            category_number = int(user_input) - 1
            
            # Check if the number is valid
            if 0 <= category_number < len(category_list):
                # Show all tickets in that category
                selected_category = category_list[category_number]
                selected_category.display_info()
            else:
                print("Invalid number!")
                
    except ValueError:
        print("Please enter a valid number!")


# ============================================================================
# FUNCTION 3: SEARCH TICKETS
# ============================================================================
# This function lets the user search for tickets by typing keywords
# ============================================================================
def search_tickets(categories):
    """Search for tickets by name or category"""
    
    # Get search term from user
    search_word = input("\nEnter search term: ").lower()
    
    # Check if user entered something
    if not search_word.strip():
        print("Search term cannot be empty!")
        return
    
    # List to store matching tickets
    matching_tickets = []
    
    # Look through all categories
    for category in categories.values():
        # Look through all tickets in each category
        for ticket in category.get_all_tickets():
            # Check if search word matches ticket name or category name
            ticket_name_lower = ticket.topup_type.lower()
            category_name_lower = ticket.category.lower()
            
            if search_word in ticket_name_lower or search_word in category_name_lower:
                # Add this ticket to our results
                matching_tickets.append((category.name, ticket))
    
    # Check if we found anything
    if not matching_tickets:
        print(f"\nNo tickets found matching '{search_word}'")
        return
    
    # Show results
    print(f"\nFound {len(matching_tickets)} results:")
    print("="*40)
    
    # Display each matching ticket
    for number, (category_name, ticket) in enumerate(matching_tickets, 1):
        print(f"\n{number}. {category_name} - {ticket.topup_type}")
        print(f"   Price: £{ticket.get_price():.2f}")
        if ticket.topup_description:
            description = ticket.topup_description[:50]
            print(f"   Description: {description}...")


# ============================================================================
# FUNCTION 4: PURCHASE TICKET
# ============================================================================
# This function handles the entire purchase process step by step
# ============================================================================
def purchase_ticket(categories):
    """Handle the ticket purchase process"""
    
    print("\n" + "="*40)
    print("   PURCHASE TICKET")
    print("="*40)
    
    try:
        # STEP 1: Show categories and let user choose
        category_list = list(categories.values())
        
        print("\nAvailable Categories:")
        for number, category in enumerate(category_list, 1):
            print(f"{number}. {category.name}")
        
        # Get user's category choice
        category_choice = int(input("\nSelect category number: ")) - 1
        
        # Check if choice is valid
        if category_choice < 0 or category_choice >= len(category_list):
            print("Invalid category!")
            return
        
        # Get the selected category
        chosen_category = category_list[category_choice]
        
        # STEP 2: Show tickets in that category and let user choose
        tickets_in_category = chosen_category.get_all_tickets()
        
        print(f"\nTickets in {chosen_category.name}:")
        for number, ticket in enumerate(tickets_in_category, 1):
            price = ticket.get_price()
            print(f"{number}. {ticket.topup_type} - £{price:.2f}")
        
        # Get user's ticket choice
        ticket_choice = int(input("\nSelect ticket number: ")) - 1
        
        # Check if choice is valid
        if ticket_choice < 0 or ticket_choice >= len(tickets_in_category):
            print("Invalid ticket!")
            return
        
        # Get the selected ticket
        chosen_ticket = tickets_in_category[ticket_choice]
        
        # STEP 3: Ask for quantity
        quantity = int(input("Enter quantity: "))
        
        # Check if quantity is valid
        if quantity <= 0:
            print("Quantity must be positive!")
            return
        
        # STEP 4: Show summary and ask for confirmation
        unit_price = chosen_ticket.get_price()
        total_price = unit_price * quantity
        
        print(f"\nYou are purchasing:")
        print(f"{quantity}x {chosen_ticket.topup_type}")
        print(f"Total: £{total_price:.2f}")
        
        # Ask user to confirm
        confirm_answer = input("\nConfirm purchase? (yes/no): ").lower()
        
        # If user confirms
        if confirm_answer in ['yes', 'y']:
            # Create a Purchase object
            new_purchase = Purchase(chosen_ticket, quantity)
            
            # Save to file
            purchase_saved = save_purchase(new_purchase.to_file_format())
            
            if purchase_saved:
                # Show receipt
                new_purchase.display_receipt()
                print("\n✓ Purchase saved successfully!")
            else:
                print("\n✗ Error saving purchase!")
        else:
            print("Purchase cancelled.")
    
    except ValueError:
        print("Invalid input! Please enter numbers only.")
    except Exception as e:
        print(f"Error during purchase: {e}")


# ============================================================================
# FUNCTION 5: VIEW PURCHASE HISTORY
# ============================================================================
# This function shows all previous purchases the user has made
# ============================================================================
def view_my_purchases():
    """Display all previous purchases"""
    
    # Load all purchases from file
    all_purchases = load_purchases()
    
    # Check if there are any purchases
    if not all_purchases:
        print("\nNo purchases found.")
        return
    
    # Display header
    print("\n" + "="*40)
    print("   YOUR PURCHASE HISTORY")
    print("="*40)
    
    # Variable to keep track of total money spent
    total_money_spent = 0.0
    
    # Go through each purchase
    for purchase_number, purchase_data in enumerate(all_purchases, 1):
        try:
            # Convert the saved data back to a dictionary
            purchase_info = Purchase.from_file_format(purchase_data)
            
            # Display purchase details
            print(f"\n{purchase_number}. Date: {purchase_info['timestamp']}")
            print(f"   Ticket: {purchase_info['topup_type']}")
            print(f"   Quantity: {purchase_info['quantity']}")
            print(f"   Total: £{purchase_info['total']}")
            
            # Add to total
            total_money_spent += float(purchase_info['total'])
            
        except Exception as e:
            print(f"Error reading purchase: {e}")
    
    # Show total
    print("\n" + "="*40)
    print(f"Total spent: £{total_money_spent:.2f}")
    print("="*40)
    
    # Ask if user wants to see statistics
    try:
        want_stats = input("\nView purchase statistics? (yes/no): ").lower()
        if want_stats in ['yes', 'y']:
            view_purchase_stats()
    except Exception:
        pass  # If user cancels, just continue


# ============================================================================
# FUNCTION 6: VIEW PURCHASE STATISTICS
# ============================================================================
# This function shows a simple bar chart of purchases by category
# ============================================================================
def view_purchase_stats():
    """Show statistics about purchases with a simple bar chart"""
    
    # Load all purchases
    all_purchases = load_purchases()
    
    # Check if there are any purchases
    if not all_purchases:
        print("No purchase data to analyze.")
        return
    
    # Count how many purchases in each category
    category_purchase_count = Counter()
    
    # Go through each purchase
    for purchase_data in all_purchases:
        try:
            # Get purchase information
            purchase_info = Purchase.from_file_format(purchase_data)
            category_name = purchase_info['category']
            
            # Add 1 to the count for this category
            category_purchase_count[category_name] += 1
            
        except Exception:
            continue  # Skip invalid purchases
    
    # Check if we have any valid data
    if not category_purchase_count:
        print("No valid purchase data to analyze.")
        return
    
    # Display header
    print("\n" + "="*40)
    print("   PURCHASES BY CATEGORY")
    print("="*40)
    
    # Find the maximum count (for scaling the bars)
    max_purchases = max(category_purchase_count.values())
    
    # Sort categories by count (most purchases first)
    sorted_categories = sorted(category_purchase_count.items(), 
                               key=lambda x: x[1], 
                               reverse=True)
    
    # Display each category with a bar
    for category_name, purchase_count in sorted_categories:
        # Calculate bar length (scale to 30 characters max)
        bar_size = int((purchase_count / max_purchases) * 30)
        bar_chart = "█" * bar_size
        
        # Display category name, bar, and count
        print(f"{category_name:20} {bar_chart} ({purchase_count})")
    
    # Show total
    print("="*40)
    total_purchases = sum(category_purchase_count.values())
    print(f"Total purchases: {total_purchases}")


# ============================================================================
# MAIN FUNCTION - THIS IS WHERE THE PROGRAM STARTS
# ============================================================================
# This function runs the entire program
# ============================================================================
def main():
    """Main program - this is where everything starts"""
    
    # STEP 1: Load ticket data from CSV file
    print("Loading ticket data...")
    categories = load_ticket_objects('data/bus_tickets.csv')
    
    # Check if data loaded successfully
    if not categories:
        print("Cannot run without ticket data. Exiting.")
        return
    
    # STEP 2: Main program loop - keeps running until user exits
    while True:
        # Show menu
        display_menu()
        
        try:
            # Get user's choice
            user_choice = input("\nEnter your choice (1-7): ")
            
            # Handle each menu option
            if user_choice == "1":
                # View categories
                view_categories(categories)
                
            elif user_choice == "2":
                # Search for tickets
                search_tickets(categories)
                
            elif user_choice == "3":
                # Purchase a ticket
                purchase_ticket(categories)
                
            elif user_choice == "4":
                # View purchase history
                view_my_purchases()
                
            elif user_choice == "5":
                # View statistics
                view_purchase_stats()
                
            elif user_choice == "6":
                # Admin panel
                admin_panel(categories)
                
            elif user_choice == "7":
                # Exit program
                print("Thank you for using Bus Ticket System!")
                break
                
            else:
                # Invalid choice
                print("Invalid choice! Please enter 1-7.")
                
        except KeyboardInterrupt:
            # User pressed Ctrl+C
            print("\nProgram interrupted. Goodbye!")
            break
            
        except Exception as e:
            # Any other error
            print(f"An error occurred: {e}")


# ============================================================================
# START THE PROGRAM
# ============================================================================
# This code runs when you execute the file
# ============================================================================
if __name__ == "__main__":
    main()
