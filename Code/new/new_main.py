i = 0 #variable to be used for iteration
history = [] #clipboard history list
for x in range(10):
    clipboard_entry = input("Enter text to add to clipboard: ") #gets user input for clipboard entry
    history.append(clipboard_entry) #adds the user input to the clipboard history list

#menu
print("PastClip - Clipboard History\n"
      "============================\n"
      "1. View clipboard history\n"
      "2. Add new clipboard entry\n"
      "3. View clipboard entry metadata\n"
      "4. Exit\n")
entry = int(input("Enter your choice: ")) #gets user input for menu choice
while entry < 1 or entry > 4: #checks if user input is valid
    print("Invalid choice. Please try again.") #prints error message
    entry = int(input("Enter your choice: ")) #gets user input for menu choice  

if entry == 1: #if user input is 1
    print("Clipboard History:")
    print(*history) *#prints all items of the list without square brackets and commas