import tkinter as tk

clipboard = ["print('Hello World')", "import random", "total_lines = sum(1 for line in f)","{word}: {count}","россия",
             "😎","johnsmith@gmail.com", "password", "https://classroom.google.com/c/ODQyNDM1MTYxNjUz/a/ODY0NjcxMjc3NDEw/details", "Clipboard Entry 1!"]

root = tk.Tk() # create root window

# root window title and dimension
root.title("PastClip") #program name
root.geometry('375x480') #width x height window of 375x480px

i = 0 #integer that will change based on iteration

labels = []

def quit_program(): #function when quit button is clicked
    quit()

def clear_clipboard():
    empty_label = tk.Label(root, text="Clipboard is empty")
    empty_label.pack(before=labels[i]) #places empty_label before label[i] is removed
    clipboard.clear() #empties clipboard
    for label in labels: #for each label in the labels list
        label.destroy() #destroys each label
        delete.destroy()
        preferences_divider.destroy()
        root.geometry('375x190')
#all widgets will be here
label = tk.Label(root, text="Select the clip to copy the entry to your clipboard!", fg="#B1B1B1") #creates text in root layer
label.pack() #pack arranges label vertically
divider = tk.Frame(root, height=2, bg="#808080") #created divider that goes from edge to edge in gray
divider.pack(fill="x", pady=10) #fills horizontally with margin of padding 10px on both sides
for i in range(10): #creates 10 clipboard entries
    row_frame = tk.Frame(root) #create row frame for elements within row
    row_frame.pack(fill="x", padx=10, pady=2) #keeps the lines separated top-to-bottom
    label = tk.Label(row_frame, text=f"{clipboard[-(i-1)]}", anchor="w", justify="left")
    label.pack(side="left",fill="x", padx=(10, 60),expand=True) #renders labels with left side 10px and 60px on right
    command = tk.Label(row_frame, text=f"⌘ {i}", fg="#B1B1B1", anchor="e", justify="right") #creates text in root layer
    command.pack(side="right",fill="x")
    labels.append(label) #adds individual labels to list to store for later
divider = tk.Frame(root, height=2, bg="#808080")
divider.pack(fill="x", pady=10)
delete = tk.Button(root, text="Clear all clipboard entries", command=clear_clipboard) #creates interactable button for deleting clipboard entries
delete.pack(fill="x", padx=80, pady=5) #button extends across horizontal window for maximum coverage to click
preferences_divider = tk.Frame(root, height=2, bg="#808080")
preferences_divider.pack(fill="x", pady=10) 
preferences = tk.Label(root, text="Preferences")
preferences.pack(fill="x")
divider = tk.Frame(root, height=2, bg="#808080")
divider.pack(fill="x", pady=10)
button = tk.Button(root, text="Quit", bg="#808080", command=quit_program)
button.pack(fill="x", padx=80, pady=5)
divider = tk.Frame(root, height=2, bg="#808080")
divider.pack(fill="x", pady=10)
root.mainloop() # execute Tkinter