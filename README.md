# Bus Ticket Purchase System

**Author:** [Your Name]  
**Module:** COMP10121 - Foundations of Computer Programming  
**Date:** January 2026

## Project Overview
A Python console application for browsing and purchasing bus tickets.
Users can view available ticket categories, search for specific tickets,
make purchases, and view their purchase history.

## Features Implemented
✅ Read ticket data from CSV file  
✅ Object-oriented design with Ticket, Category, and Purchase classes  
✅ Menu-driven interface  
✅ Browse tickets by category  
✅ Search functionality  
✅ Purchase tickets with quantity selection  
✅ Save purchases to file  
✅ View purchase history  
✅ Comprehensive error handling  
✅ Input validation  

## How to Run
1. Ensure Python 3.x is installed
2. Place CSV file in `data/` folder as `bus_tickets.csv`
3. Run: `python3 main.py` or `python main.py`

## Project Structure
```
bus_ticket_project/
├── main.py                 # Main program and menu
├── ticket_classes.py       # Ticket, Category, Purchase classes
├── file_handler.py         # File I/O operations
├── data/
│   ├── bus_tickets.csv    # Ticket data
│   └── purchases.txt      # Saved purchases
└── README.md              # This file
```

## Class Design

### Ticket Class
Represents individual bus ticket/top-up options.

**Attributes:**
- category (str): The category name of the ticket
- category_id (str): Unique identifier for the category
- topup_type (str): Name/type of the top-up ticket
- price (float): Price in pounds (converted from pence)
- entitlement_type (str): Type of entitlement
- passenger_class (str): Passenger class (e.g., 'Adult', 'Student')
- And more...

**Methods:**
- `__init__(data_dict)`: Initialize from CSV data
- `display_info()`: Display formatted ticket information
- `get_price()`: Return ticket price
- `__str__()`: String representation

### Category Class
Groups tickets by category.

**Attributes:**
- name (str): The name of the category
- tickets (list): List of Ticket objects in this category

**Methods:**
- `__init__(name)`: Initialize category with name
- `add_ticket(ticket)`: Add a ticket to this category
- `get_all_tickets()`: Return all tickets
- `get_ticket_count()`: Return number of tickets
- `display_info()`: Display category and all tickets
- `__str__()`: String representation

### Purchase Class
Records ticket purchases.

**Attributes:**
- ticket (Ticket): The Ticket object that was purchased
- quantity (int): The number of tickets purchased
- timestamp (datetime): The date and time of the purchase
- total (float): The total cost (price * quantity)

**Methods:**
- `__init__(ticket, quantity)`: Initialize purchase
- `get_total()`: Return total cost
- `display_receipt()`: Display formatted receipt
- `to_file_format()`: Convert to string for saving
- `from_file_format(line)`: Parse from saved string [static]

## CSV Structure
The CSV contains the following fields:
- category_id, category_title, category_description
- topup_id, topup_title, topup_description, topup_price_in_pence
- topup_entitlement_type, topup_entitlement_unit, topup_entitlement_value, topup_entitlement_quantity
- topup_entitlement_start_date, topup_entitlement_end_date
- topup_passenger_class_id, topup_passenger_class_name, topup_passenger_class_quantity

## Testing Log

### File Reading
- ✅ Successfully reads CSV with correct field mapping
- ✅ Handles missing file gracefully
- ✅ Handles corrupted CSV format
- ✅ Provides detailed error messages

### Menu System
- ✅ All menu options work correctly
- ✅ Invalid input handled without crash
- ✅ Exit cleanly on option 5 or Ctrl+C
- ✅ Menu displays correctly formatted

### Purchase Flow
- ✅ Can select category and ticket
- ✅ Quantity validation works
- ✅ Purchase confirmation required
- ✅ Purchase saved to file correctly
- ✅ Receipt displays accurate information

### Search
- ✅ Finds tickets by partial match
- ✅ Searches both ticket type and category
- ✅ Handles no results gracefully
- ✅ Displays results in formatted list

### Purchase History
- ✅ Loads all previous purchases
- ✅ Displays purchase details correctly
- ✅ Calculates total spent accurately
- ✅ Handles empty history gracefully

## Known Limitations
- No admin features to modify prices
- No graphical visualization of purchase data
- Text-based interface only
- No user authentication
- No payment processing integration

## Future Enhancements
- Add data visualization with charts
- Implement user accounts
- Add admin panel for price management
- Export purchases to PDF
- Add filtering options for purchase history
- Implement shopping cart for multiple items
- Add discount/promotion codes

## Development Process
This project was developed iteratively with weekly goals:

### Week 1: Setup and Basic Structure
- Created project structure
- Set up git repository
- Implemented basic menu system
- Added CSV reading functionality

### Week 2: File Handling & Data Structures
- Created file_handler.py module
- Implemented data loading functions
- Added view categories feature
- Organized data into appropriate structures

### Week 3: Object-Oriented Design
- Designed class structure
- Implemented Ticket class
- Implemented Category class
- Refactored code to use objects

### Week 4: Purchase System & More Features
- Created Purchase class
- Implemented full purchase flow
- Added purchase history viewing
- Implemented file persistence

### Week 5: Polish, Documentation & Advanced Features
- Added search functionality
- Improved error handling
- Added comprehensive docstrings
- Updated documentation

### Week 6: Testing and Final Submission
- Final testing and bug fixes
- Code review and optimization
- Final documentation updates

## GenAI Usage
I used Cursor's AI assistance to:
- Understand Python syntax (e.g., "How does csv.DictReader work?")
- Learn about object-oriented programming concepts
- Debug specific errors
- Learn about docstring formats
- Understand best practices for error handling

All code was written and understood by me. No AI generated complete
sections of code without my review and understanding.

## Error Handling
The application includes comprehensive error handling for:
- Missing or invalid CSV files
- File permission errors
- Invalid user input
- Empty search results
- Corrupted purchase data
- Network/file system errors

All errors provide clear, user-friendly messages with guidance on how to resolve issues.

## License
This project is part of an academic assignment and is for educational purposes only.
