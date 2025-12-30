# Bus Ticket Purchase System

## Project Goal
Create a Python program to help users browse and purchase bus tickets.

## Features to Implement
- [x] Read ticket data from CSV
- [x] Display menu system
- [x] Browse categories
- [ ] Purchase tickets
- [ ] Save purchases to file

## Development Log
### Week 1
- Created project structure
- Added CSV reading test function (reads first 3 rows)
- Created basic menu system with error handling

### Week 2 Progress
- ✅ Created file_handler.py module
- ✅ Load CSV data successfully
- ✅ View categories feature working
- ✅ Category details display working

### Week 3 Progress
- ✅ Designed class structure
- ✅ Implemented Ticket class
- ✅ Implemented Category class
- ✅ Refactored code to use objects
- ✅ All features still working

## Class Design

### Category Class
**Attributes:**
- name (string)
- tickets (list of Ticket objects)

**Methods:**
- __init__(name)
- add_ticket(ticket)
- get_all_tickets()
- display_info()

### Ticket Class
**Attributes:**
- category (string)
- topup_type (string)
- price (float)
- duration (string)
- entitlement_type (string)

**Methods:**
- __init__(data_dict)
- display_info()
- get_price()

### CSV Structure
The CSV contains the following fields:
- category_id, category_title, category_description
- topup_id, topup_title, topup_description, topup_price_in_pence
- topup_entitlement_type, topup_entitlement_unit, topup_entitlement_value, topup_entitlement_quantity
- topup_entitlement_start_date, topup_entitlement_end_date
- topup_passenger_class_id, topup_passenger_class_name, topup_passenger_class_quantity
