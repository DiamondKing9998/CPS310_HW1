# Menu display function
def display_menu():
    print("===============================")
    print("==== FRC INVENTORY MANAGER ====")
    print("===============================")
    print("1. View Inventory")
    print("2. Add an Item")
    print("3. Update an Item Quantity")
    print("4. Remove an Item")
    print("5. Search Inventory")
    print("6. View Inventory Summary")
    print("7. Exit")
    print("===============================")
    choice = input("Enter your selection (1-7): ")
    if choice == '1':
        view_inventory()
    elif choice == '2':
        add_item()
    elif choice == '3':
        update_item_quantity()
    elif choice == '4':
        remove_item()
    elif choice == '5':
        search_inventory()
    elif choice == '6':
        view_inventory_summary()
    elif choice == '7':
        exit_program()
    else:
        print("Invalid choice. Please try again.")
    

# 1. View Inventory function
def view_inventory():
    print("Viewing inventory... (Functionality not yet implemented)")

    display_menu()
# 2. Add an Item function
def add_item():
    print("Adding an item... (Functionality not yet implemented)")

    display_menu()
# 3. Update an Item Quantity function
def update_item_quantity():
    print("Updating item quantity... (Functionality not yet implemented)")

    display_menu()
# 4. Remove an Item function
def remove_item():
    print("Removing an item... (Functionality not yet implemented)")

    display_menu()
# 5. Search Inventory function
def search_inventory():
    print("Searching inventory... (Functionality not yet implemented)")

    display_menu()
# 6. View Inventory Summary function
def view_inventory_summary():
    print("Viewing inventory summary... (Functionality not yet implemented)")

    display_menu()
#7. Exit function
def exit_program():
    print("Exiting the program. Goodbye!")
    exit()

# Program runtime loop
if __name__ == "__main__":
    while True:
        display_menu()
            