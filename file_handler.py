import csv
import os
from ticket_classes import Ticket, Category

def load_ticket_data(filename):
    """
    Load ticket data from CSV file.
    
    Reads a CSV file and converts each row into a dictionary.
    Provides detailed error messages for common issues like missing files,
    permission errors, and invalid CSV format.
    
    Args:
        filename (str): Path to the CSV file to load
        
    Returns:
        list: List of dictionaries, one per row, or empty list if error
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        PermissionError: If file cannot be read due to permissions
        csv.Error: If CSV format is invalid
    """
    ticket_data = []
    
    if not os.path.exists(filename):
        print("="*50)
        print("ERROR: Ticket data file not found!")
        print(f"Looking for: {filename}")
        print("\nPlease ensure:")
        print("1. The CSV file is downloaded from NOW")
        print("2. It's placed in the 'data' folder")
        print("3. The filename matches exactly")
        print("="*50)
        return []
    
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            ticket_data = list(reader)
            
            if not ticket_data:
                print("Warning: CSV file is empty!")
            else:
                print(f"Successfully loaded {len(ticket_data)} tickets")
                
    except PermissionError:
        print("="*50)
        print("Error: No permission to read file!")
        print(f"File: {filename}")
        print("Please check file permissions.")
        print("="*50)
        return []
        
    except csv.Error as e:
        print("="*50)
        print(f"Error: Invalid CSV format - {e}")
        print("Please ensure the CSV file is properly formatted.")
        print("="*50)
        return []
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        print("Please ensure the CSV file is in the data folder.")
        return []
        
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []
    
    return ticket_data


def get_unique_categories(ticket_data):
    """
    Extract unique category names from ticket data.
    
    Iterates through ticket data dictionaries and collects unique
    category names using a set to avoid duplicates. Returns a
    sorted list for consistent ordering.
    
    Args:
        ticket_data (list): List of dictionaries containing ticket data
        
    Returns:
        list: Sorted list of unique category names (strings)
    """
    categories = set()  # Use set to avoid duplicates
    
    for ticket in ticket_data:
        if 'Category' in ticket:  # Check field exists
            categories.add(ticket['Category'])
    
    return sorted(list(categories))  # Return sorted list


def save_purchase(purchase_data, filename='data/purchases.txt'):
    """
    Save a purchase record to a file.
    
    Appends a purchase record (as a string) to the purchases file.
    Creates the file if it doesn't exist. Uses append mode to preserve
    existing purchases.
    
    Args:
        purchase_data (str): String representation of the purchase to save
        filename (str, optional): Path to the purchases file. Defaults to 'data/purchases.txt'.
        
    Returns:
        bool: True if save was successful, False otherwise
    """
    try:
        with open(filename, 'a') as file:  # 'a' for append
            file.write(str(purchase_data) + '\n')
        return True
        
    except Exception as e:
        print(f"Error saving purchase: {e}")
        return False


def load_purchases(filename='data/purchases.txt'):
    """
    Load previous purchases from file.
    
    Reads all purchase records from the purchases file, one per line.
    Returns an empty list if the file doesn't exist (no previous purchases).
    
    Args:
        filename (str, optional): Path to the purchases file. Defaults to 'data/purchases.txt'.
        
    Returns:
        list: List of strings, each representing a purchase record, or empty list if no file
    """
    purchases = []
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                purchases.append(line.strip())
                
    except FileNotFoundError:
        print("No previous purchases found.")
        
    except Exception as e:
        print(f"Error loading purchases: {e}")
    
    return purchases


def load_ticket_objects(filename):
    """
    Load ticket data and return as Ticket objects organized by Category.
    
    Reads CSV file, creates Ticket objects for each row, and organizes
    them into Category objects. Returns a dictionary where keys are
    category names and values are Category objects containing their tickets.
    
    Args:
        filename (str): Path to the CSV file containing ticket data
        
    Returns:
        dict: Dictionary mapping category names (str) to Category objects,
              or empty dict if error
    """
    categories = {}
    
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                # Create Ticket object
                ticket = Ticket(row)
                
                # Get or create Category
                cat_name = ticket.category
                if cat_name not in categories:
                    categories[cat_name] = Category(cat_name)
                
                # Add ticket to category
                categories[cat_name].add_ticket(ticket)
        
        print(f"Loaded {len(categories)} categories successfully")
        
    except Exception as e:
        print(f"Error loading tickets: {e}")
    
    return categories


# Test code
if __name__ == "__main__":
    # Test loading
    data = load_ticket_data('data/bus_tickets.csv')
    print(f"Loaded {len(data)} records")
    
    # Test getting categories
    categories = get_unique_categories(data)
    print(f"Found {len(categories)} categories")
    print(categories)

