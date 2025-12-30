import csv

def load_ticket_data(filename):
    """
    Load ticket data from CSV file.
    Returns: list of dictionaries, or empty list if error
    """
    ticket_data = []
    
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            ticket_data = list(reader)
            print(f"Successfully loaded {len(ticket_data)} tickets")
            
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        print("Please ensure the CSV file is in the data folder.")
        
    except Exception as e:
        print(f"Error loading data: {e}")
    
    return ticket_data


def get_unique_categories(ticket_data):
    """
    Extract unique category names from ticket data.
    Returns: list of unique categories
    """
    categories = set()  # Use set to avoid duplicates
    
    for ticket in ticket_data:
        if 'Category' in ticket:  # Check field exists
            categories.add(ticket['Category'])
    
    return sorted(list(categories))  # Return sorted list


def save_purchase(purchase_data, filename='data/purchases.txt'):
    """
    Save a purchase to file.
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
    Returns: list of purchases
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


# Test code
if __name__ == "__main__":
    # Test loading
    data = load_ticket_data('data/bus_tickets.csv')
    print(f"Loaded {len(data)} records")
    
    # Test getting categories
    categories = get_unique_categories(data)
    print(f"Found {len(categories)} categories")
    print(categories)

