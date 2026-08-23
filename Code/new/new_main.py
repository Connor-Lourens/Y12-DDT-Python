history = [] #clipboard history list
clipboard_entry = input("Enter text to add to clipboard: ") #gets user input for clipboard entry
history.append(clipboard_entry) #adds the user input to the clipboard history list
print(history[-1]) #prints most recent clipboard entry

#menu
while True:
    print("PastClip - Clipboard History\n")
    print("1. View clipboard history")
    print("2. Add new clipboard entry")
    print("3. View clipboard entry metadata")
    print("4. Exit\n")
    entry = int(input("Enter your choice: ")) #gets user input for menu choice