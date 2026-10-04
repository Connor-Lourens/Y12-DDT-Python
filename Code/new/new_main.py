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
while entry < 1 or entry > 3: #checks if user input is valid
    print("Invalid choice. Please try again") #prints error message
    entry = int(input("Enter your choice: ")) #gets user input for menu choice  
while True: #loops until loop broken
    if entry == 1: #user selects viewing clipboard history
        if history == []:
            print("Clipboard is empty")
        else:
            print("Clipboard History:")
            print(*history, sep=", ") #prints all items of the list without square brackets and adds commas
        print(menu)
        entry = int(input("Enter your choice: ")) #gets user input for menu choice

    if entry == 2:  #user selects adding new clipboard entry
        while True:  #main loop for continuous adding if user wants "Y"
            history.append(input("Enter text to add to clipboard: ")) #adds to list of clipboard entries after asking question
            
            while True: #failsafe loop for Y/N input
                more_entries_query = input("Would you like to add more entries? (Y/N): ").upper()
                if more_entries_query in ["Y", "N"]:
                    break
                print("Please type 'Y' to indicate 'Yes', or 'N' to indicate 'No'") #default answer is anything but "Y"/"N"
     
            if more_entries_query == "N":    
                print(menu) #return to menu
                entry = int(input("Enter your choice: "))
                while entry < 1 or entry > 3:
                    print("Invalid choice. Please try again")
                    entry = int(input("Enter your choice: "))
                break
    if entry == 3: #user selects exiting the program
        break
