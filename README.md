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
✅ Purchase statistics visualization (bar chart)  
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

## Testing Documentation

### Test 1: CSV Loading
**Test:** Load valid CSV file  
**Expected:** Data loads successfully with ticket count displayed  
**Result:** ✅ Pass - Successfully loaded tickets from bus_tickets.csv

**Test:** Load non-existent file  
**Expected:** Error message displayed, program continues gracefully  
**Result:** ✅ Pass - Shows helpful error message with file path and instructions

**Test:** Load empty CSV  
**Expected:** Warning message displayed  
**Result:** ✅ Pass - Shows "Warning: CSV file is empty!" message

**Test:** Load file with permission errors  
**Expected:** Permission error message displayed  
**Result:** ✅ Pass - Shows detailed permission error message

**Test:** Load corrupted CSV file  
**Expected:** CSV format error message displayed  
**Result:** ✅ Pass - Shows "Invalid CSV format" error with details

### Test 2: Menu Navigation
**Test:** Enter valid choice (1-5)  
**Expected:** Correct feature loads and executes  
**Result:** ✅ Pass - All menu options work correctly

**Test:** Enter invalid number (6, 0, -1)  
**Expected:** Error message displayed, menu redisplays  
**Result:** ✅ Pass - Shows "Invalid choice! Please enter 1-5." and menu reappears

**Test:** Enter letter instead of number  
**Expected:** Error message, no crash  
**Result:** ✅ Pass - Handled gracefully, program continues

**Test:** Press Enter without input  
**Expected:** Menu redisplays or handles empty input  
**Result:** ✅ Pass - Menu redisplays correctly

**Test:** Use Ctrl+C to exit  
**Expected:** Graceful exit with goodbye message  
**Result:** ✅ Pass - Shows "Program interrupted. Goodbye!" and exits cleanly

### Test 3: Category Browsing
**Test:** View all categories  
**Expected:** Numbered list of all categories displayed  
**Result:** ✅ Pass - Categories displayed with ticket counts

**Test:** Select valid category number  
**Expected:** Detailed ticket list for that category displayed  
**Result:** ✅ Pass - Shows all tickets in selected category with prices

**Test:** Select invalid category number (too high)  
**Expected:** Error message displayed  
**Result:** ✅ Pass - Shows "Invalid number!" message

**Test:** Select invalid category number (negative)  
**Expected:** Error message displayed  
**Result:** ✅ Pass - Handled correctly

**Test:** Press Enter to return without selecting  
**Expected:** Returns to main menu  
**Result:** ✅ Pass - Returns to menu without error

### Test 4: Search Functionality
**Test:** Search with valid term that matches tickets  
**Expected:** List of matching tickets displayed  
**Result:** ✅ Pass - Shows matching tickets with category, type, and price

**Test:** Search with term matching category name  
**Expected:** All tickets in that category displayed  
**Result:** ✅ Pass - Correctly finds tickets by category

**Test:** Search with term matching ticket type  
**Expected:** Matching tickets displayed  
**Result:** ✅ Pass - Correctly finds tickets by type

**Test:** Search with term that matches nothing  
**Expected:** "No tickets found" message displayed  
**Result:** ✅ Pass - Shows "No tickets found matching '[term]'"

**Test:** Search with empty string  
**Expected:** Error message or no results  
**Result:** ✅ Pass - Shows "Search term cannot be empty!"

**Test:** Case-insensitive search  
**Expected:** Finds matches regardless of case  
**Result:** ✅ Pass - Search works with any case combination

### Test 5: Purchase Flow
**Test:** Complete valid purchase  
**Expected:** Purchase confirmed, receipt displayed, saved to file  
**Result:** ✅ Pass - Full purchase flow works correctly

**Test:** Select valid category  
**Expected:** Category selected successfully  
**Result:** ✅ Pass - Category selection works

**Test:** Select valid ticket from category  
**Expected:** Ticket selected successfully  
**Result:** ✅ Pass - Ticket selection works

**Test:** Enter valid quantity  
**Expected:** Quantity accepted  
**Result:** ✅ Pass - Quantity input works

**Test:** Enter invalid quantity (0 or negative)  
**Expected:** Error message, purchase cancelled  
**Result:** ✅ Pass - Shows "Quantity must be positive!"

**Test:** Enter non-numeric quantity  
**Expected:** Error message displayed  
**Result:** ✅ Pass - Shows "Invalid input! Please enter numbers only."

**Test:** Confirm purchase with 'yes'  
**Expected:** Purchase completed, receipt shown  
**Result:** ✅ Pass - Purchase confirmed and saved

**Test:** Confirm purchase with 'y'  
**Expected:** Purchase completed  
**Result:** ✅ Pass - Accepts 'y' as confirmation

**Test:** Cancel purchase with 'no'  
**Expected:** Purchase cancelled, returns to menu  
**Result:** ✅ Pass - Shows "Purchase cancelled." and returns

**Test:** Select invalid category number during purchase  
**Expected:** Error message, returns to menu  
**Result:** ✅ Pass - Shows "Invalid category!" and returns

**Test:** Select invalid ticket number during purchase  
**Expected:** Error message, returns to menu  
**Result:** ✅ Pass - Shows "Invalid ticket!" and returns

### Test 6: Purchase History
**Test:** View purchases with existing purchase history  
**Expected:** All purchases displayed with details  
**Result:** ✅ Pass - Shows all purchases with date, ticket, quantity, total

**Test:** View purchases with no history  
**Expected:** "No purchases found" message  
**Result:** ✅ Pass - Shows appropriate message

**Test:** Total spent calculation  
**Expected:** Correct total calculated and displayed  
**Result:** ✅ Pass - Total calculated accurately

**Test:** Multiple purchases displayed correctly  
**Expected:** All purchases shown in numbered list  
**Result:** ✅ Pass - All purchases displayed correctly

### Test 7: File Saving
**Test:** Purchase saved to file  
**Expected:** Purchase data written to purchases.txt  
**Result:** ✅ Pass - File created/updated correctly

**Test:** Multiple purchases saved sequentially  
**Expected:** All purchases appended to file  
**Result:** ✅ Pass - All purchases saved correctly

**Test:** Purchase file format  
**Expected:** Correct pipe-delimited format  
**Result:** ✅ Pass - Format: timestamp|category|type|quantity|total

**Test:** Load purchases from file  
**Expected:** Purchases loaded and parsed correctly  
**Result:** ✅ Pass - Purchases loaded successfully

### Test 8: Error Handling
**Test:** Handle missing CSV file gracefully  
**Expected:** Program exits with helpful message  
**Result:** ✅ Pass - Shows detailed error and exits gracefully

**Test:** Handle invalid input throughout program  
**Expected:** No crashes, error messages displayed  
**Result:** ✅ Pass - All invalid inputs handled gracefully

**Test:** Handle file permission errors  
**Expected:** Error message displayed, program continues  
**Result:** ✅ Pass - Permission errors handled correctly

**Test:** Handle corrupted purchase data  
**Expected:** Error message for invalid purchase, continues  
**Result:** ✅ Pass - Shows "Error reading purchase" and continues

### Test 9: Purchase Statistics
**Test:** View statistics with purchase history  
**Expected:** Bar chart displayed showing purchases by category  
**Result:** ✅ Pass - Statistics displayed with visual bar chart

**Test:** View statistics with no purchase history  
**Expected:** "No purchase data to analyze" message  
**Result:** ✅ Pass - Shows appropriate message

**Test:** Statistics bar chart formatting  
**Expected:** Categories sorted by count, bars proportional  
**Result:** ✅ Pass - Chart displays correctly with Unicode blocks

**Test:** Statistics total calculation  
**Expected:** Total purchases count displayed correctly  
**Result:** ✅ Pass - Total count accurate

## Known Limitations
- No admin features to modify prices
- Text-based interface only (no GUI)
- No user authentication
- No payment processing integration
- Statistics visualization is text-based only

## Future Enhancements
- Add graphical data visualization with charts (matplotlib)
- Implement user accounts
- Add admin panel for price management
- Export purchases to PDF
- Add filtering options for purchase history
- Implement shopping cart for multiple items
- Add discount/promotion codes
- Add more detailed statistics (spending trends, popular tickets)

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

### Week 6: Testing, Final Features & Submission Prep
- Comprehensive testing documentation
- Added purchase statistics visualization feature
- Final testing and validation
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
