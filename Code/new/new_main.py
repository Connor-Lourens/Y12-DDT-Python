i = 0 #variable to be used for iteration
history = [] #clipboard history list

menu = "\n|================================|"
"\n|PastClip - Clipboard History    |\n"
"|================================|\n"
"|1. View clipboard history       |\n"
"|2. Add new clipboard entry      |\n"
"|3. View clipboard entry metadata|\n"
"|4. Exit                         |\n"
"|================================|\n" #saves main menu as variable to reuse
print(menu)
entry = int(input("Enter your choice: ")) #gets user input for menu choice
while entry < 1 or entry > 4: #checks if user input is valid
    print("Invalid choice. Please try again.") #prints error message
    entry = int(input("Enter your choice: ")) #gets user input for menu choice  

if entry == 1:
    print("Clipboard History:")
    if history == "":
        print("Clipboard is empty")
    
    print(*history, sep=", ") #prints all items of the list without square brackets and adds commas

if entry == 2:
    clipboard_entry = input("Enter text to add to clipboard: ")
    history.append(clipboard_entry)
    more_entries_query = input("Would you like to add more entries? (Y/N): ").upper() #queries user to add more clipboard entries
    if clipboard_entry == "Y": #yes option
        clipboard_entry = input("Enter text to add to clipboard: ")
        history.append(clipboard_entry)
    elif clipboard_entry == "N": #no option
        print(menu)
    else:
        while more_entries_query != "Y" or more_entries_query != "N":
            print("Please type 'Y' to indicate 'Yes', or 'N' to indicate 'No")
            more_entries_query = input("Would you like to add more entries? (Y/N): ").upper()

if entry == 3:

    print("")
if entry == 4:
    quit()