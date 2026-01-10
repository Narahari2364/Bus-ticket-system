# ============================================================================
# ADMIN INTERFACE - BUS TICKET SYSTEM
# ============================================================================
# This file contains all admin functions for managing tickets and viewing data
# ============================================================================

import csv
from file_handler import load_ticket_objects, load_ticket_data, load_purchases
from ticket_classes import Ticket, Category, Purchase


# ============================================================================
# ADMIN MENU
# ============================================================================
def display_admin_menu():
    """Show the admin menu options"""
    print("\n" + "="*40)
    print("   ADMIN PANEL")
    print("="*40)
    print("1. View All Tickets")
    print("2. Add New Ticket")
    print("3. Edit Ticket Price")
    print("4. Delete Ticket")
    print("5. View All Purchases")
    print("6. View System Statistics")
    print("7. Back to Main Menu")
    print("="*40)


# ============================================================================
# FUNCTION 1: VIEW ALL TICKETS
# ============================================================================
def view_all_tickets(categories):
    """Display all tickets in the system organized by category"""
    
    print("\n" + "="*50)
    print("   ALL TICKETS IN SYSTEM")
    print("="*50)
    
    total_tickets = 0
    
    # Go through each category
    for category_name, category_obj in categories.items():
        print(f"\n--- {category_name} ---")
        tickets = category_obj.get_all_tickets()
        
        # Show each ticket in this category
        for number, ticket in enumerate(tickets, 1):
            print(f"  {number}. {ticket.topup_type}")
            print(f"     Price: £{ticket.price:.2f}")
            print(f"     ID: {ticket.topup_id[:8]}...")
            total_tickets += 1
    
    print("\n" + "="*50)
    print(f"Total tickets in system: {total_tickets}")
    print("="*50)


# ============================================================================
# FUNCTION 2: ADD NEW TICKET
# ============================================================================
def add_new_ticket(categories):
    """Add a new ticket to the system"""
    
    print("\n" + "="*40)
    print("   ADD NEW TICKET")
    print("="*40)
    
    try:
        # Get ticket information from admin
        print("\nEnter ticket details:")
        category_name = input("Category name: ").strip()
        
        if not category_name:
            print("Category name cannot be empty!")
            return
        
        ticket_type = input("Ticket type/name: ").strip()
        if not ticket_type:
            print("Ticket type cannot be empty!")
            return
        
        # Get price (in pounds)
        price_input = input("Price in pounds (e.g., 5.50): ").strip()
        try:
            price_pounds = float(price_input)
            if price_pounds < 0:
                print("Price cannot be negative!")
                return
            # Convert to pence for storage
            price_pence = int(price_pounds * 100)
        except ValueError:
            print("Invalid price! Please enter a number.")
            return
        
        description = input("Description (optional): ").strip()
        passenger_class = input("Passenger class (e.g., Adult, Student): ").strip() or "Adult"
        
        # Create ticket data dictionary
        new_ticket_data = {
            'category_title': category_name,
            'category_id': 'new-' + category_name.lower().replace(' ', '-'),
            'category_description': f'Tickets for {category_name}',
            'topup_title': ticket_type,
            'topup_id': 'new-' + ticket_type.lower().replace(' ', '-'),
            'topup_description': description or f'{ticket_type} ticket',
            'topup_price_in_pence': str(price_pence),
            'topup_entitlement_type': 'fixed',
            'topup_entitlement_unit': 'journey',
            'topup_entitlement_value': '1',
            'topup_passenger_class_name': passenger_class
        }
        
        # Create Ticket object
        new_ticket = Ticket(new_ticket_data)
        
        # Add to category
        if category_name not in categories:
            categories[category_name] = Category(category_name)
        
        categories[category_name].add_ticket(new_ticket)
        
        print(f"\n✓ Ticket '{ticket_type}' added successfully!")
        print(f"  Category: {category_name}")
        print(f"  Price: £{price_pounds:.2f}")
        
    except Exception as e:
        print(f"Error adding ticket: {e}")


# ============================================================================
# FUNCTION 3: EDIT TICKET PRICE
# ============================================================================
def edit_ticket_price(categories):
    """Edit the price of an existing ticket"""
    
    print("\n" + "="*40)
    print("   EDIT TICKET PRICE")
    print("="*40)
    
    # Show all categories
    category_list = list(categories.items())
    
    print("\nSelect category:")
    for number, (cat_name, cat_obj) in enumerate(category_list, 1):
        print(f"{number}. {cat_name}")
    
    try:
        # Get category choice
        cat_choice = int(input("\nCategory number: ")) - 1
        
        if cat_choice < 0 or cat_choice >= len(category_list):
            print("Invalid category!")
            return
        
        selected_category_name, selected_category = category_list[cat_choice]
        tickets = selected_category.get_all_tickets()
        
        # Show tickets in category
        print(f"\nTickets in {selected_category_name}:")
        for number, ticket in enumerate(tickets, 1):
            print(f"{number}. {ticket.topup_type} - £{ticket.price:.2f}")
        
        # Get ticket choice
        ticket_choice = int(input("\nTicket number: ")) - 1
        
        if ticket_choice < 0 or ticket_choice >= len(tickets):
            print("Invalid ticket!")
            return
        
        selected_ticket = tickets[ticket_choice]
        
        # Show current price
        print(f"\nCurrent price: £{selected_ticket.price:.2f}")
        
        # Get new price
        new_price_input = input("Enter new price in pounds: ").strip()
        try:
            new_price = float(new_price_input)
            if new_price < 0:
                print("Price cannot be negative!")
                return
            
            # Update the price
            selected_ticket.price = new_price
            
            print(f"\n✓ Price updated successfully!")
            print(f"  New price: £{new_price:.2f}")
            
        except ValueError:
            print("Invalid price! Please enter a number.")
            
    except ValueError:
        print("Invalid input! Please enter numbers only.")
    except Exception as e:
        print(f"Error: {e}")


# ============================================================================
# FUNCTION 4: DELETE TICKET
# ============================================================================
def delete_ticket(categories):
    """Delete a ticket from the system"""
    
    print("\n" + "="*40)
    print("   DELETE TICKET")
    print("="*40)
    
    # Show all categories
    category_list = list(categories.items())
    
    print("\nSelect category:")
    for number, (cat_name, cat_obj) in enumerate(category_list, 1):
        print(f"{number}. {cat_name}")
    
    try:
        # Get category choice
        cat_choice = int(input("\nCategory number: ")) - 1
        
        if cat_choice < 0 or cat_choice >= len(category_list):
            print("Invalid category!")
            return
        
        selected_category_name, selected_category = category_list[cat_choice]
        tickets = selected_category.get_all_tickets()
        
        # Show tickets in category
        print(f"\nTickets in {selected_category_name}:")
        for number, ticket in enumerate(tickets, 1):
            print(f"{number}. {ticket.topup_type} - £{ticket.price:.2f}")
        
        # Get ticket choice
        ticket_choice = int(input("\nTicket number to delete: ")) - 1
        
        if ticket_choice < 0 or ticket_choice >= len(tickets):
            print("Invalid ticket!")
            return
        
        ticket_to_delete = tickets[ticket_choice]
        
        # Confirm deletion
        print(f"\nYou are about to delete: {ticket_to_delete.topup_type}")
        confirm = input("Are you sure? (yes/no): ").lower()
        
        if confirm in ['yes', 'y']:
            # Remove ticket from category
            selected_category.tickets.remove(ticket_to_delete)
            print(f"\n✓ Ticket '{ticket_to_delete.topup_type}' deleted successfully!")
        else:
            print("Deletion cancelled.")
            
    except ValueError:
        print("Invalid input! Please enter numbers only.")
    except Exception as e:
        print(f"Error: {e}")


# ============================================================================
# FUNCTION 5: VIEW ALL PURCHASES
# ============================================================================
def view_all_purchases():
    """View all purchases made by all users"""
    
    print("\n" + "="*50)
    print("   ALL PURCHASES (ADMIN VIEW)")
    print("="*50)
    
    # Load all purchases
    all_purchases = load_purchases()
    
    if not all_purchases:
        print("\nNo purchases found in the system.")
        return
    
    # Display all purchases
    total_revenue = 0.0
    purchase_count = 0
    
    for purchase_number, purchase_data in enumerate(all_purchases, 1):
        try:
            purchase_info = Purchase.from_file_format(purchase_data)
            
            print(f"\nPurchase #{purchase_number}:")
            print(f"  Date: {purchase_info['timestamp']}")
            print(f"  Category: {purchase_info['category']}")
            print(f"  Ticket: {purchase_info['topup_type']}")
            print(f"  Quantity: {purchase_info['quantity']}")
            print(f"  Total: £{purchase_info['total']}")
            
            total_revenue += float(purchase_info['total'])
            purchase_count += 1
            
        except Exception as e:
            print(f"Error reading purchase: {e}")
    
    # Show summary
    print("\n" + "="*50)
    print("SUMMARY:")
    print(f"  Total purchases: {purchase_count}")
    print(f"  Total revenue: £{total_revenue:.2f}")
    print("="*50)


# ============================================================================
# FUNCTION 6: VIEW SYSTEM STATISTICS
# ============================================================================
def view_system_statistics(categories):
    """Show comprehensive system statistics"""
    
    print("\n" + "="*50)
    print("   SYSTEM STATISTICS")
    print("="*50)
    
    # Count tickets
    total_tickets = 0
    total_categories = len(categories)
    
    for category_obj in categories.values():
        total_tickets += len(category_obj.get_all_tickets())
    
    print(f"\nTICKET INFORMATION:")
    print(f"  Total categories: {total_categories}")
    print(f"  Total tickets: {total_tickets}")
    
    # Show tickets per category
    print(f"\nTICKETS BY CATEGORY:")
    for category_name, category_obj in categories.items():
        ticket_count = len(category_obj.get_all_tickets())
        print(f"  {category_name}: {ticket_count} tickets")
    
    # Load purchase statistics
    all_purchases = load_purchases()
    
    if all_purchases:
        total_purchases = len(all_purchases)
        total_revenue = 0.0
        
        for purchase_data in all_purchases:
            try:
                purchase_info = Purchase.from_file_format(purchase_data)
                total_revenue += float(purchase_info['total'])
            except Exception:
                continue
        
        print(f"\nPURCHASE INFORMATION:")
        print(f"  Total purchases: {total_purchases}")
        print(f"  Total revenue: £{total_revenue:.2f}")
        if total_purchases > 0:
            avg_purchase = total_revenue / total_purchases
            print(f"  Average purchase: £{avg_purchase:.2f}")
    else:
        print(f"\nPURCHASE INFORMATION:")
        print(f"  No purchases yet")
    
    print("\n" + "="*50)


# ============================================================================
# ADMIN LOGIN (Simple password check)
# ============================================================================
def admin_login():
    """Simple admin login - check password"""
    
    # Simple password (in real app, this would be encrypted)
    admin_password = "admin123"
    
    print("\n" + "="*40)
    print("   ADMIN LOGIN")
    print("="*40)
    
    password = input("Enter admin password: ")
    
    if password == admin_password:
        print("✓ Login successful!")
        return True
    else:
        print("✗ Invalid password!")
        return False


# ============================================================================
# ADMIN MAIN FUNCTION
# ============================================================================
def admin_panel(categories):
    """Main admin panel function"""
    
    # Check login
    if not admin_login():
        return
    
    # Admin menu loop
    while True:
        display_admin_menu()
        
        try:
            choice = input("\nEnter your choice (1-7): ")
            
            if choice == "1":
                view_all_tickets(categories)
            elif choice == "2":
                add_new_ticket(categories)
            elif choice == "3":
                edit_ticket_price(categories)
            elif choice == "4":
                delete_ticket(categories)
            elif choice == "5":
                view_all_purchases()
            elif choice == "6":
                view_system_statistics(categories)
            elif choice == "7":
                print("Returning to main menu...")
                break
            else:
                print("Invalid choice! Please enter 1-7.")
                
        except KeyboardInterrupt:
            print("\nExiting admin panel...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

