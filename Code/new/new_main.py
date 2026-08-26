i = 0 #variable to be used for iteration
history = [] #clipboard history list
page_counter = 1

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
|3. View clipboard entry metadata|
|================================|
|4. Exit                         |
|================================|
"""
 #saves main menu as variable to reuse
print(menu)
entry = int(input("Enter your choice: ")) #gets user input for menu choice
while entry < 1 or entry > 4: #checks if user input is valid
    print("Invalid choice. Please try again") #prints error message
    entry = int(input("Enter your choice: ")) #gets user input for menu choice  

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
        clipboard_entry = input("Enter text to add to clipboard: ")
        history.append(clipboard_entry)
    elif more_entries_query == "N": #no option
        print(menu)
        entry = int(input("Enter your choice: ")) #gets user input for menu choice
        pass
    else:
        while more_entries_query != "Y" or more_entries_query != "N":
            print("Please type 'Y' to indicate 'Yes', or 'N' to indicate 'No'")
            more_entries_query = input("Would you like to add more entries? (Y/N): ").upper()
            

if entry == 3: #user selects viewing clipboard entry metadata
    pages_amount = -(-len(history) // 3) #uses negative floor division to divide amount of clipboard entries by 3 then round up (floor division is usually down)
    print(range(history[3])) #prints the last 3 clipboard entries in the list
    next_page = int(input("Would you like to go to the next page? (Y/N): "))
    if next_page == "Y": #user selects next page
        print(history[:3]) #prints first 3 items in the list
    elif next_page == "N": #user doesn't select next page
        print("""
|================================|
|1. Go back a page               |
|================================|
|2. Go back to main menu         |
|================================|
""")
        next_step_query = int(input("What would you like to do next?: "))
        if next_step_query == 1:
            pass
        elif next_step_query == 2:
            print(menu)
        else:
            pass
if entry == 4: #user selects exiting the program
    quit()

