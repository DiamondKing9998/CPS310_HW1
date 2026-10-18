# FRC Inventory Manager

## Project Description
During a hectic FIRST Robotics Competition (FRC) build season or out at a district event, keeping track of spare parts is usually pure chaos. Between scrambling to rebuild a swerve module between playoff matches and losing track of how many CANcoders are left in the pit bins, stuff goes missing constantly. 

I built the FRC Inventory Manager as a clean, simple command-line Python tool to solve that problem. It lets our team keep a reliable tally of our critical hardware—like brushless motors, motor controllers, sensors, and structural spares—so we always know what we have on hand and what needs to be reordered before competition weekend.

## Features
The program uses a simple numbered console menu with seven options:
1. **View Inventory**: Prints a numbered list of all tracked parts along with their category and current stock level.
2. **Add an Item**: Adds a new part by asking for its name, subsystem category, and quantity. It checks to make sure inputs aren't blank, quantities aren't negative, and you don't use pipe characters (`|`) or quotes that would mess up file saving.
3. **Update an Item Quantity**: Shows the current parts list with index numbers so you can pick an item and change its quantity (and automatically saves the change).
4. **Remove an Item**: Lets you select a part by its line number to delete it entirely from the system and updates the save file.
5. **Search Inventory**: Lets you type in a keyword to search across part names or categories (case-insensitive) to quickly locate what you need.
6. **View Inventory Summary**: Gives a quick dashboard showing total unique parts, total item count, how many items arae running low (quantity under 5), and a breakdown of parts per category.
7. **Exit**: Prints a goodbye message and closes out the program cleanly.

## Requirements
* Python 3.14

## Project Files
* `inventory_manager.py`: The main script containing the interactive CLI loop, menu logic, search/update functions, and file I/O helpers (`load_inventory` and `save_inventory`).
* `inventory.txt`: A plain-text flat file that acts as our database so inventory persists between sessions.
* `README.md`: Project documentation covering how the tool works, how to run it, and development notes.
* `AI_USAGE.md` : Required disclosure of project AI usage for the assignment

## Inventory Data Format
All items are stored line-by-line inside `inventory.txt` using a basic pipe-separated format[cite: 1, 2]:

```text
Name|Category|Quantity