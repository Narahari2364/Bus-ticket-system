class Ticket:
    """Represents a single bus ticket/top-up option"""
    
    def __init__(self, ticket_data):
        """
        Initialize ticket from CSV data dictionary
        ticket_data: dictionary with CSV fields
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
        """Display ticket information in formatted way"""
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
        """Return ticket price"""
        return self.price
    
    def __str__(self):
        """String representation of ticket"""
        return f"{self.topup_type} (£{self.price:.2f})"


class Category:
    """Represents a ticket category containing multiple tickets"""
    
    def __init__(self, name):
        """Initialize category with name"""
        self.name = name
        self.tickets = []  # List to store Ticket objects
    
    def add_ticket(self, ticket):
        """Add a ticket to this category"""
        if isinstance(ticket, Ticket):
            self.tickets.append(ticket)
        else:
            print("Error: Can only add Ticket objects")
    
    def get_all_tickets(self):
        """Return all tickets in this category"""
        return self.tickets
    
    def get_ticket_count(self):
        """Return number of tickets in category"""
        return len(self.tickets)
    
    def display_info(self):
        """Display category information"""
        print(f"\nCategory: {self.name}")
        print(f"Available tickets: {self.get_ticket_count()}")
        print("=" * 40)
        
        for i, ticket in enumerate(self.tickets, 1):
            print(f"{i}. {ticket}")
    
    def __str__(self):
        """String representation"""
        return f"{self.name} ({self.get_ticket_count()} tickets)"


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

