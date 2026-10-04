#ANSI colour codes
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"

i = 0 # constant variable to be used for iteration
history = [] #clipboard history list

menu = CYAN + """
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
""" + RESET
 #saves main menu as variable to reuse
print(menu)
def get_entry(): #asks for a menu choice until a valid number from 1-3 is entered
    while True:
        try:
            entry = int(input(GREEN + "Enter your choice: " + RESET))
        except ValueError: #runs if the input isn't a whole number (letters, symbols, blank, float)
            print(RED + "Please enter a number (1-3)" + RESET)
            continue
        if 1 <= entry <= 3:
            return entry
        print(RED + "Invalid choice. Please try again" + RESET)
entry = get_entry()
while True: #loops until loop broken
    if entry == 1: #user selects viewing clipboard history
        if history == []:
            print(YELLOW + "Clipboard is empty" + RESET)
        else:
            print(BOLD + YELLOW + "Clipboard History:" + RESET)
            print(MAGENTA, end="")
            print(*history, sep=", ") #prints all items of the list without square brackets and adds commas
            print(RESET, end="")
        print(menu)
        entry = get_entry() #gets user input for menu choice

    if entry == 2:  #user selects adding new clipboard entry
        while True:  #main loop for continuous adding if user wants "Y"
            history.append(input(GREEN + "Enter text to add to clipboard: " + RESET)) #adds to list of clipboard entries after asking question
            
            while True: #failsafe loop for Y/N input
                more_entries_query = input(GREEN + "Would you like to add more entries? (Y/N): " + RESET).upper()
                if more_entries_query in ["Y", "N"]:
                    break
                print(RED + "Please type 'Y' to indicate 'Yes', or 'N' to indicate 'No'" + RESET) #default answer is anything but "Y"/"N"
     
            if more_entries_query == "N":    
                print(menu) #return to menu
                entry = get_entry()
                break
    if entry == 3: #user selects exiting the program
        break
