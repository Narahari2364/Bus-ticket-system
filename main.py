import csv

# Test reading the CSV file
def test_read_csv():
    """Test function to see what's in the CSV file"""
    try:
        with open('data/bus_tickets.csv', 'r') as file:
            reader = csv.DictReader(file)
            
            # Print first 3 rows to understand structure
            count = 0
            for row in reader:
                print(row)
                count += 1
                if count >= 3:
                    break
    except FileNotFoundError:
        print("Error: CSV file not found!")
    except Exception as e:
        print(f"Error reading file: {e}")

def display_menu():
    """Display main menu options"""
    print("\n" + "="*40)
    print("   BUS TICKET PURCHASE SYSTEM")
    print("="*40)
    print("1. View Ticket Categories")
    print("2. Search Top-ups")
    print("3. Purchase Ticket")
    print("4. View My Purchases")
    print("5. Exit")
    print("="*40)

def main():
    """Main program loop"""
    while True:
        display_menu()
        
        try:
            choice = input("\nEnter your choice (1-5): ")
            
            if choice == "1":
                print("View categories - Coming soon!")
            elif choice == "2":
                print("Search top-ups - Coming soon!")
            elif choice == "3":
                print("Purchase - Coming soon!")
            elif choice == "4":
                print("View purchases - Coming soon!")
            elif choice == "5":
                print("Thank you for using Bus Ticket System!")
                break
            else:
                print("Invalid choice! Please enter 1-5.")
                
        except KeyboardInterrupt:
            print("\nProgram interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

