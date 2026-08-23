history = [] #clipboard history list
clipboard_entry = input("Enter text to add to clipboard: ") #gets user input for clipboard entry
history.append(clipboard_entry) #adds the user input to the clipboard history list
print(history[-1]) #prints most recent clipboard entry

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