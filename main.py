from file_handler import load_ticket_data, get_unique_categories, load_ticket_objects, save_purchase, load_purchases
from ticket_classes import Purchase
from collections import Counter

def display_menu():
    """
    Display the main menu options to the user.
    
    Shows all available menu options (1-5) with clear formatting.
    Menu options include viewing categories, searching, purchasing,
    viewing purchases, and exiting the program.
    
    Returns:
        None
    """
    print("\n" + "="*40)
    print("   BUS TICKET PURCHASE SYSTEM")
    print("="*40)
    print("1. View Ticket Categories")
    print("2. Search Top-ups")
    print("3. Purchase Ticket")
    print("4. View My Purchases")
    print("5. View Purchase Statistics")
    print("6. Exit")
    print("="*40)

def view_categories_v2(categories):
    """
    Display all available ticket categories using Category objects.
    
    Shows a numbered list of all categories and allows the user to
    select a category to view detailed ticket information. Uses the
    Category object's __str__ and display_info methods.
    
    Args:
        categories (dict): Dictionary of Category objects to display
        
    Returns:
        None
    """
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

def search_tickets(categories):
    """
    Search for tickets by name or category.
    
    Searches through all categories and tickets to find matches
    based on partial string matching in ticket type or category name.
    Displays all matching results with their details.
    
    Args:
        categories (dict): Dictionary of Category objects to search through
        
    Returns:
        None
    """
    search_term = input("\nEnter search term: ").lower()
    
    if not search_term.strip():
        print("Search term cannot be empty!")
        return
    
    results = []
    
    # Search through all categories
    for category in categories.values():
        for ticket in category.get_all_tickets():
            # Check if search term in ticket type or category
            if (search_term in ticket.topup_type.lower() or 
                search_term in ticket.category.lower()):
                results.append((category.name, ticket))
    
    if not results:
        print(f"\nNo tickets found matching '{search_term}'")
        return
    
    print(f"\nFound {len(results)} results:")
    print("="*40)
    
    for i, (cat_name, ticket) in enumerate(results, 1):
        print(f"\n{i}. {cat_name} - {ticket.topup_type}")
        print(f"   Price: £{ticket.get_price():.2f}")
        if hasattr(ticket, 'topup_description') and ticket.topup_description:
            print(f"   Description: {ticket.topup_description[:50]}...")

def purchase_ticket(categories):
    """
    Handle the complete ticket purchase process.
    
    Guides the user through a multi-step purchase flow:
    1. Select a category from available categories
    2. Select a specific ticket from the chosen category
    3. Enter the quantity of tickets to purchase
    4. Confirm the purchase before finalizing
    
    Creates a Purchase object and saves it to file upon confirmation.
    Displays a receipt after successful purchase.
    
    Args:
        categories (dict): Dictionary of Category objects containing tickets
        
    Returns:
        None
        
    Raises:
        ValueError: If user enters invalid numeric input
        Exception: For any other unexpected errors during purchase
    """
    print("\n" + "="*40)
    print("   PURCHASE TICKET")
    print("="*40)
    
    # Step 1: Select category
    cat_list = list(categories.values())
    
    print("\nAvailable Categories:")
    for i, cat in enumerate(cat_list, 1):
        print(f"{i}. {cat.name}")
    
    try:
        cat_choice = int(input("\nSelect category number: ")) - 1
        
        if not (0 <= cat_choice < len(cat_list)):
            print("Invalid category!")
            return
        
        selected_category = cat_list[cat_choice]
        
        # Step 2: Select ticket from category
        tickets = selected_category.get_all_tickets()
        
        print(f"\nTickets in {selected_category.name}:")
        for i, ticket in enumerate(tickets, 1):
            print(f"{i}. {ticket.topup_type} - £{ticket.get_price():.2f}")
        
        ticket_choice = int(input("\nSelect ticket number: ")) - 1
        
        if not (0 <= ticket_choice < len(tickets)):
            print("Invalid ticket!")
            return
        
        selected_ticket = tickets[ticket_choice]
        
        # Step 3: Enter quantity
        quantity = int(input("Enter quantity: "))
        
        if quantity <= 0:
            print("Quantity must be positive!")
            return
        
        # Step 4: Confirm purchase
        print(f"\nYou are purchasing:")
        print(f"{quantity}x {selected_ticket.topup_type}")
        print(f"Total: £{selected_ticket.get_price() * quantity:.2f}")
        
        confirm = input("\nConfirm purchase? (yes/no): ").lower()
        
        if confirm in ['yes', 'y']:
            # Create purchase
            purchase = Purchase(selected_ticket, quantity)
            
            # Save to file
            if save_purchase(purchase.to_file_format()):
                purchase.display_receipt()
                print("\n✓ Purchase saved successfully!")
            else:
                print("\n✗ Error saving purchase!")
        else:
            print("Purchase cancelled.")
    
    except ValueError:
        print("Invalid input! Please enter numbers only.")
    except Exception as e:
        print(f"Error during purchase: {e}")

def view_my_purchases():
    """
    Display all previous purchases from purchase history file.
    
    Loads all saved purchases from the purchases file, displays them
    in a formatted list with details (date, ticket type, quantity, total),
    and calculates the total amount spent across all purchases.
    
    Returns:
        None
    """
    purchases = load_purchases()
    
    if not purchases:
        print("\nNo purchases found.")
        return
    
    print("\n" + "="*40)
    print("   YOUR PURCHASE HISTORY")
    print("="*40)
    
    total_spent = 0.0
    
    for i, purchase_line in enumerate(purchases, 1):
        try:
            purchase_dict = Purchase.from_file_format(purchase_line)
            
            print(f"\n{i}. Date: {purchase_dict['timestamp']}")
            print(f"   Ticket: {purchase_dict['topup_type']}")
            print(f"   Quantity: {purchase_dict['quantity']}")
            print(f"   Total: £{purchase_dict['total']}")
            
            total_spent += float(purchase_dict['total'])
            
        except Exception as e:
            print(f"Error reading purchase: {e}")
    
    print("\n" + "="*40)
    print(f"Total spent: £{total_spent:.2f}")
    print("="*40)
    
    # Offer to view statistics
    try:
        view_stats = input("\nView purchase statistics? (yes/no): ").lower()
        if view_stats in ['yes', 'y']:
            view_purchase_stats()
    except Exception:
        pass  # Silently continue if user cancels

def view_purchase_stats():
    """
    Show simple bar chart of category purchases.
    
    Analyzes purchase history and displays a text-based bar chart
    showing the distribution of purchases by category. Uses Unicode
    block characters to create a visual representation.
    
    Returns:
        None
    """
    purchases = load_purchases()
    
    if not purchases:
        print("No purchase data to analyze.")
        return
    
    # Count purchases by category
    category_counts = Counter()
    
    for purchase_line in purchases:
        try:
            purchase_dict = Purchase.from_file_format(purchase_line)
            category_counts[purchase_dict['category']] += 1
        except Exception:
            continue  # Skip invalid purchases
    
    if not category_counts:
        print("No valid purchase data to analyze.")
        return
    
    # Display simple text bar chart
    print("\n" + "="*40)
    print("   PURCHASES BY CATEGORY")
    print("="*40)
    
    max_count = max(category_counts.values()) if category_counts else 1
    
    # Sort by count (descending) for better visualization
    sorted_categories = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)
    
    for category, count in sorted_categories:
        bar_length = int((count / max_count) * 30)
        bar = "█" * bar_length
        print(f"{category:20} {bar} ({count})")
    
    print("="*40)
    print(f"Total purchases: {sum(category_counts.values())}")

def main():
    """
    Main program entry point.
    
    Loads ticket data, displays menu, and handles user choices
    in a loop until user exits. Manages the overall program flow
    and routes user selections to appropriate functions.
    
    Handles:
    - Menu display
    - User input validation
    - Feature routing (view categories, search, purchase, view history)
    - Graceful exit on option 5 or Ctrl+C
    
    Returns:
        None
    """
    # Load ticket data as objects organized by category
    categories = load_ticket_objects('data/bus_tickets.csv')
    
    if not categories:
        print("Cannot run without ticket data. Exiting.")
        return
    
    while True:
        display_menu()
        
        try:
            choice = input("\nEnter your choice (1-6): ")
            
            if choice == "1":
                view_categories_v2(categories)
            elif choice == "2":
                search_tickets(categories)
            elif choice == "3":
                purchase_ticket(categories)
            elif choice == "4":
                view_my_purchases()
            elif choice == "5":
                view_purchase_stats()
            elif choice == "6":
                print("Thank you for using Bus Ticket System!")
                break
            else:
                print("Invalid choice! Please enter 1-6.")
                
        except KeyboardInterrupt:
            print("\nProgram interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
