from datetime import datetime

class Ticket:
    """
    Represents a single bus ticket/top-up option.
    
    This class encapsulates all information about a bus ticket including
    its category, type, price, duration, entitlement details, and passenger
    class. Price is automatically converted from pence to pounds.
    
    Attributes:
        category (str): The category name of the ticket
        category_id (str): Unique identifier for the category
        category_description (str): Description of the category
        topup_type (str): Name/type of the top-up ticket
        topup_id (str): Unique identifier for the top-up
        topup_description (str): Description of the top-up
        price (float): Price in pounds (converted from pence)
        entitlement_type (str): Type of entitlement (e.g., 'fixed', 'flexible')
        entitlement_unit (str): Unit of entitlement (e.g., 'journey', 'day')
        entitlement_value (str): Value of the entitlement
        entitlement_quantity (str): Quantity of entitlements
        start_date (str): Start date of validity
        end_date (str): End date of validity
        passenger_class (str): Passenger class (e.g., 'Adult', 'Student')
    """
    
    def __init__(self, ticket_data):
        """
        Initialize ticket from CSV data dictionary.
        
        Extracts all relevant fields from the CSV data dictionary and
        converts price from pence to pounds. Handles missing or invalid
        data gracefully with default values.
        
        Args:
            ticket_data (dict): Dictionary containing CSV row data with
                              fields like 'category_title', 'topup_title',
                              'topup_price_in_pence', etc.
        """
        self.category = ticket_data.get('category_title', 'Unknown')
        self.category_id = ticket_data.get('category_id', '')
        self.category_description = ticket_data.get('category_description', '')
        self.topup_type = ticket_data.get('topup_title', 'Unknown')
        self.topup_id = ticket_data.get('topup_id', '')
        self.topup_description = ticket_data.get('topup_description', '')
        # Convert price from pence to pounds
        price_pence = ticket_data.get('topup_price_in_pence', '0')
        try:
            self.price = float(price_pence) / 100.0
        except (ValueError, TypeError):
            self.price = 0.0
        self.entitlement_type = ticket_data.get('topup_entitlement_type', 'N/A')
        self.entitlement_unit = ticket_data.get('topup_entitlement_unit', 'N/A')
        self.entitlement_value = ticket_data.get('topup_entitlement_value', 'N/A')
        self.entitlement_quantity = ticket_data.get('topup_entitlement_quantity', 'N/A')
        self.start_date = ticket_data.get('topup_entitlement_start_date', 'N/A')
        self.end_date = ticket_data.get('topup_entitlement_end_date', 'N/A')
        self.passenger_class = ticket_data.get('topup_passenger_class_name', 'N/A')
    
    def display_info(self):
        """
        Display ticket information in a formatted, readable way.
        
        Prints all relevant ticket details including category, type, price,
        description, entitlement information, validity dates, and passenger
        class. Formats output with clear labels and separators.
        
        Returns:
            None
        """
        print(f"\nCategory: {self.category}")
        print(f"Type: {self.topup_type}")
        print(f"Price: £{self.price:.2f}")
        print(f"Description: {self.topup_description}")
        print(f"Entitlement: {self.entitlement_type}")
        if self.entitlement_value != 'N/A':
            print(f"Value: {self.entitlement_value} {self.entitlement_unit}")
        if self.start_date != 'N/A' and self.end_date != 'N/A':
            print(f"Valid: {self.start_date} to {self.end_date}")
        print(f"Passenger Class: {self.passenger_class}")
        print("-" * 40)
    
    def get_price(self):
        """
        Return the ticket price in pounds.
        
        Returns:
            float: The price of the ticket in pounds
        """
        return self.price
    
    def __str__(self):
        """
        Return string representation of the ticket.
        
        Provides a concise string representation showing the ticket type
        and price, suitable for display in lists and menus.
        
        Returns:
            str: String in format "TicketType (£XX.XX)"
        """
        return f"{self.topup_type} (£{self.price:.2f})"


class Category:
    """
    Represents a ticket category containing multiple tickets.
    
    This class groups related Ticket objects together by category.
    Provides methods to add tickets, retrieve tickets, and display
    category information.
    
    Attributes:
        name (str): The name of the category
        tickets (list): List of Ticket objects in this category
    """
    
    def __init__(self, name):
        """
        Initialize category with a name.
        
        Creates a new category with an empty list of tickets.
        
        Args:
            name (str): The name of the category
        """
        self.name = name
        self.tickets = []  # List to store Ticket objects
    
    def add_ticket(self, ticket):
        """
        Add a ticket to this category.
        
        Validates that the provided object is a Ticket instance before
        adding it to the category's ticket list.
        
        Args:
            ticket (Ticket): The Ticket object to add to this category
            
        Returns:
            None
        """
        if isinstance(ticket, Ticket):
            self.tickets.append(ticket)
        else:
            print("Error: Can only add Ticket objects")
    
    def get_all_tickets(self):
        """
        Return all tickets in this category.
        
        Returns:
            list: List of all Ticket objects in this category
        """
        return self.tickets
    
    def get_ticket_count(self):
        """
        Return the number of tickets in this category.
        
        Returns:
            int: The count of tickets in this category
        """
        return len(self.tickets)
    
    def display_info(self):
        """
        Display category information and all tickets.
        
        Shows the category name, ticket count, and a numbered list
        of all tickets in the category using their string representation.
        
        Returns:
            None
        """
        print(f"\nCategory: {self.name}")
        print(f"Available tickets: {self.get_ticket_count()}")
        print("=" * 40)
        
        for i, ticket in enumerate(self.tickets, 1):
            print(f"{i}. {ticket}")
    
    def __str__(self):
        """
        Return string representation of the category.
        
        Provides a concise string showing the category name and ticket count.
        
        Returns:
            str: String in format "CategoryName (X tickets)"
        """
        return f"{self.name} ({self.get_ticket_count()} tickets)"


class Purchase:
    """
    Represents a ticket purchase transaction.
    
    This class records a purchase of one or more tickets, including
    the timestamp, total cost, and all relevant details. Provides methods
    to display receipts and convert to/from file format for persistence.
    
    Attributes:
        ticket (Ticket): The Ticket object that was purchased
        quantity (int): The number of tickets purchased
        timestamp (datetime): The date and time of the purchase
        total (float): The total cost (price * quantity)
    """
    
    def __init__(self, ticket, quantity=1):
        """
        Initialize a purchase with a ticket and quantity.
        
        Creates a new purchase record with the current timestamp and
        calculates the total cost based on ticket price and quantity.
        
        Args:
            ticket (Ticket): The Ticket object being purchased
            quantity (int, optional): Number of tickets to purchase. Defaults to 1.
        """
        self.ticket = ticket
        self.quantity = quantity
        self.timestamp = datetime.now()
        self.total = ticket.get_price() * quantity
    
    def get_total(self):
        """
        Return the total cost of the purchase.
        
        Returns:
            float: The total cost (price * quantity) in pounds
        """
        return self.total
    
    def display_receipt(self):
        """
        Display a formatted purchase receipt.
        
        Shows all purchase details including date, ticket information,
        quantity, unit price, and total cost in a nicely formatted receipt.
        
        Returns:
            None
        """
        print("\n" + "="*40)
        print("   PURCHASE RECEIPT")
        print("="*40)
        print(f"Date: {self.timestamp.strftime('%Y-%m-%d %H:%M')}")
        print(f"Ticket: {self.ticket.topup_type}")
        print(f"Category: {self.ticket.category}")
        print(f"Unit Price: £{self.ticket.get_price():.2f}")
        print(f"Quantity: {self.quantity}")
        print(f"Total: £{self.total:.2f}")
        print("="*40)
    
    def to_file_format(self):
        """
        Convert purchase to string format for saving to file.
        
        Creates a pipe-delimited string containing all purchase information
        that can be saved to a text file and later parsed back.
        
        Returns:
            str: Pipe-delimited string with timestamp, category, type, quantity, total
        """
        return f"{self.timestamp}|{self.ticket.category}|{self.ticket.topup_type}|{self.quantity}|{self.total}"
    
    @staticmethod
    def from_file_format(line):
        """
        Create a purchase dictionary from a saved file line.
        
        Parses a pipe-delimited string (created by to_file_format) and
        returns a dictionary with purchase information. This is a static
        method that doesn't require a Purchase instance.
        
        Args:
            line (str): Pipe-delimited string from purchase file
            
        Returns:
            dict: Dictionary with keys: 'timestamp', 'category', 'topup_type',
                  'quantity', 'total'
        """
        # This is for loading purchases later
        parts = line.strip().split('|')
        # Return dictionary with purchase info
        return {
            'timestamp': parts[0],
            'category': parts[1],
            'topup_type': parts[2],
            'quantity': parts[3],
            'total': parts[4]
        }


# Test code
if __name__ == "__main__":
    # Test Ticket class
    test_data = {
        'category_title': 'Adult',
        'topup_title': 'Single',
        'topup_price_in_pence': '250',
        'topup_description': 'Single journey ticket',
        'topup_entitlement_type': 'fixed',
        'topup_entitlement_unit': 'journey',
        'topup_entitlement_value': '1',
        'topup_passenger_class_name': 'Adult'
    }
    
    ticket = Ticket(test_data)
    ticket.display_info()
    print(f"Price: £{ticket.get_price()}")
    
    # Test Category class
    category = Category("Adult")
    category.add_ticket(ticket)
    category.display_info()
    
    # Test Purchase class
    print("\n" + "="*50)
    print("Testing Purchase class:")
    print("="*50)
    purchase = Purchase(ticket, quantity=2)
    purchase.display_receipt()
    print(f"\nFile format: {purchase.to_file_format()}")

