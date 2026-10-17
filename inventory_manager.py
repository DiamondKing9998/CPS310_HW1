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
        view_inventory(inventory)
    elif choice == '2':
        add_item(inventory)
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
def view_inventory(inventory):
    print("======== FRC INVENTORY ========")
    rowNumber = 0
    if inventory:
        for item, data in inventory.items():
            rowNumber += 1
            print(f"{rowNumber}. {data['item']} | {data['category']} | {data['quantity']}")
    else:
        print("No inventory items found.")

    display_menu()
# 2. Add an Item function
def add_item(inventory):
    nameChoice = input("Enter the name of the item: ")
    categoryChoice = input("Enter the category of the item: ")
    quantityChoice = int(input("Enter the quantity of the item: "))

    if not nameChoice:
        print("Item name cannot be empty. Please try again.")
        add_item(inventory)
        return
    if not categoryChoice:
        print("Item category cannot be empty. Please try again.")
        add_item(inventory)
        return
    if quantityChoice < 0:
        print("Item quantity cannot be negative. Please try again.")
        add_item(inventory)
        return
    if r"\"" in nameChoice or r"|" in nameChoice:
        print("Item name cannot contain quotes or pipe characters. Please try again.")
        add_item(inventory)
        return
    if r"\"" in categoryChoice or r"|" in categoryChoice:
        print("Item category cannot contain quotes or pipe characters. Please try again.")
        add_item(inventory)
        return
    if not isinstance(quantityChoice, int):
        print("Item quantity must be an integer. Please try again.")
        add_item(inventory)
        return

    inventory[nameChoice] = {"item": nameChoice, "category": categoryChoice, "quantity": quantityChoice}
    print(f"Item '{nameChoice}' added to inventory.")

    display_menu()
# 3. Update an Item Quantity function
def update_item_quantity():
    if not inventory:
        print("No inventory items found. Please add items first.")
        display_menu()
        return
    else:
        print("======== FRC INVENTORY ========")
        rowNumber = 0
        for item, data in inventory.items():
            rowNumber += 1
            print(f"{rowNumber}. {data['item']} | {data['category']} | {data['quantity']}")

        print("===============================")
        quantityChoice = int(input("Enter the number of the item you want to update: "))

        if quantityChoice < 1 or quantityChoice > len(inventory):
            print("Invalid item number. Please try again.")
            update_item_quantity()
            return
        else:
            item_to_update = list(inventory.keys())[quantityChoice - 1]
            new_quantity = int(input(f"Enter the new quantity for '{item_to_update}': "))
            if new_quantity < 0:
                print("Item quantity cannot be negative. Please try again.")
                update_item_quantity()
                return
            inventory[item_to_update]["quantity"] = new_quantity
            print(f"Quantity for '{item_to_update}' updated to {new_quantity}.")

            save_inventory(inventoryFile, inventory)

    display_menu()
# 4. Remove an Item function
def remove_item():
    if not inventory:
        print("No inventory items found. Please add items first.")
        display_menu()
        return
    else:
        print("======== FRC INVENTORY ========")
        rowNumber = 0
        for item, data in inventory.items():
            rowNumber += 1
            print(f"{rowNumber}. {data['item']} | {data['category']} | {data['quantity']}")

        print("===============================")
        quantityChoice = int(input("Enter the number of the item you want to remove: "))

        if quantityChoice < 1 or quantityChoice > len(inventory):
            print("Invalid item number. Please try again.")
            remove_item()
            return
        else:
            item_to_remove = list(inventory.keys())[quantityChoice - 1]
            del inventory[item_to_remove]
            print(f"Item '{item_to_remove}' removed from inventory.")

            save_inventory(inventoryFile, inventory)

    display_menu()
# 5. Search Inventory function
def search_inventory():
    print("Searching inventory... (Functionality not yet implemented)")

    display_menu()
# 6. View Inventory Summary function
def view_inventory_summary():
    print("Viewing inventory summary... (Functionality not yet implemented)")

    display_menu()
# 7. Exit function
def exit_program():
    print("Exiting the program. Goodbye!")
    exit()

# Other helpful functions can be added here as needed for inventory management, such as saving/loading inventory data, generating reports, etc.
def load_inventory(filename):
    inventory = {}
    try:
        with open((filename + ".txt"), "r", encoding="utf-8") as file:
            for line in file:
                name, category, quantity = line.strip().split("|")
                inventory[name] = {"item": name, "category": category, "quantity": int(quantity)}
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with an empty inventory.")
    return inventory

def save_inventory(filename, inventory):
    with open((filename + ".txt"), "w", encoding="utf-8") as file:
        for item, data in inventory.items():
            file.write(f"{data['item']}|{data['category']}|{data['quantity']}\n")


# Program runtime loop
if __name__ == "__main__":
    # Prepare inventory from file
    inventoryFile = "inventory"
    inventory = load_inventory(inventoryFile)

    display_menu()
