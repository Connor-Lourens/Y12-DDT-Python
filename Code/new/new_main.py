i = 0 # constant variable to be used for iteration
history = [] #clipboard history list

menu = """
|================================|
|            PastClip            |
|                                |
|        Clipboard History       |
|             Manager            |
|================================|
|1. View clipboard history       |
|================================|
|2. Add new clipboard entry      |
|================================|
|3. Exit                         |
|================================|
"""
 #saves main menu as variable to reuse
print(menu)
entry = int(input("Enter your choice: ")) #gets user input for menu choice
while entry < 1 or entry > 4: #checks if user input is valid
    print("Invalid choice. Please try again") #prints error message
    entry = int(input("Enter your choice: ")) #gets user input for menu choice  
while True:
    if entry == 1: #user selects viewing clipboard history
        if history == []:
            print("Clipboard is empty")
        else:
            print("Clipboard History:")
            print(*history, sep=", ") #prints all items of the list without square brackets and adds commas
        print(menu)
        entry = int(input("Enter your choice: ")) #gets user input for menu choice

    if entry == 2: #user selects adding new clipboard entry
        clipboard_entry = input("Enter text to add to clipboard: ")
        history.append(clipboard_entry)
        more_entries_query = input("Would you like to add more entries? (Y/N): ").upper() #queries user to add more clipboard entries
        if more_entries_query == "Y": #yes option
            while more_entries_query != "N":
                if more_entries_query == "Y":
                    clipboard_entry = input("Enter text to add to clipboard: ")
                    history.append(clipboard_entry)
                    more_entries_query = input("Would you like to add more entries? (Y/N): ").upper() #queries user to add more clipboard entries
                    if more_entries_query == "N":
                        print(menu)
                        entry = int(input("Enter your choice: ")) #gets user input for menu choice
                        #if 1-4
                else:
                    while more_entries_query != "Y" or more_entries_query != "N":
                        print("Please type 'Y' to indicate 'Yes', or 'N' to indicate 'No'")
                        more_entries_query = input("Would you like to add more entries? (Y/N): ").upper()
        elif  more_entries_query == "N":
            print(menu)
    print(menu)
    entry = int(input("Enter your choice: ")) #gets user input for menu choice
    while entry < 1 or entry > 4: #checks if user input is valid
        print("Invalid choice. Please try again") #prints error message
        entry = int(input("Enter your choice: ")) #gets user input for menu choice  

    if entry == 2: #user selects adding new clipboard entry
        clipboard_entry = input("Enter text to add to clipboard: ")
        history.append(clipboard_entry)
        more_entries_query = input("Would you like to add more entries? (Y/N): ").upper() #queries user to add more clipboard entries
        if more_entries_query == "Y": #yes option
            while more_entries_query != "N":
                if more_entries_query == "Y":
                    clipboard_entry = input("Enter text to add to clipboard: ")
                    history.append(clipboard_entry)
                    more_entries_query = input("Would you like to add more entries? (Y/N): ").upper() #queries user to add more clipboard entries
                    if more_entries_query == "N":
                        print(menu)
                        entry = int(input("Enter your choice: ")) #gets user input for menu choice
                        #if 1-4
                else:
                    while more_entries_query != "Y" or more_entries_query != "N":
                        print("Please type 'Y' to indicate 'Yes', or 'N' to indicate 'No'")
                        more_entries_query = input("Would you like to add more entries? (Y/N): ").upper()
        elif  more_entries_query == "N":
            print(menu)
        else:
            while more_entries_query != "Y" or more_entries_query != "N":
                print("Please type 'Y' to indicate 'Yes', or 'N' to indicate 'No'")
                more_entries_query = input("Would you like to add more entries? (Y/N): ").upper()

    if entry == 3: #user selects exiting the program
        break