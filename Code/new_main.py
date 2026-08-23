history = [] #clipboard history list
clipboard_entry = input("Enter text to add to clipboard: ") #gets user input for clipboard entry
history.append(clipboard_entry) #adds the user input to the clipboard history list
print(history[-1]) #prints most recent clipboard entry
