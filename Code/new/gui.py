import tkinter as tk
from tkinter.font import nametofont

clipboard = ["print('Hello World')", "import random", "total_lines = sum(1 for line in f)","{word}: {count}","россия",
             "😎","johnsmith@gmail.com", "password", "https://classroom.google.com/c/ODQyNDM1MTYxNjUz/a/ODY0NjcxMjc3NDEw/details", "Clipboard Entry 10!"]

root = tk.Tk() #create root window

# root window title and dimension
root.title("PastClip") #program name
root.geometry('375x480') #width x height window of 375x480px

i = 0 #integer that will change based on iteration

#storage for easy tracking
labels = []
row_frames = []
commands = []
over_300_pixels = { #key value pairs of the clipboard entry and True or False if >300 pixels
    }


def quit_program(): #function when quit button is clicked
    quit()

def clear_clipboard():
    empty_label = tk.Label(root, text="Clipboard is empty")
    empty_label.pack(before=row_frames[0]) #places empty_label before label[i] is removed
    clipboard.clear() #empties clipboard
    for label, cmd in zip(labels, commands): #loops through labels and commands at same time
        label.destroy()
        cmd.destroy()
    preferences_divider.destroy()
    delete.destroy()
    root.geometry('375x480')

def check_length():
    text_to_check_character = 0 #index iteration number throughout loop
    widget_font = nametofont(label.cget("font")) #extract font and text to check
    text_to_check = clipboard[i] #string storing characters
    text_within_300 = "" #stores characters within 300px
    while text_to_check_character < len(text_to_check):
        next_character = text_to_check[text_to_check_character] #looping through characters
        if widget_font.measure(text_within_300 + next_character) > 300: #check if next character added on exceeds 300 pixels
            break
        text_within_300 += next_character #adds next character to string
        text_to_check_character += 1
    width_within_300 = text_within_300
    width_beyond_300 = text_to_check[text_to_check_character:]
    return width_within_300, width_beyond_300

#all widgets will be here
label = tk.Label(root, text="Select the clip to copy the entry to your clipboard!", fg="#B1B1B1") #creates text in root layer
label.pack() #pack arranges label vertically
divider = tk.Frame(root, height=2, bg="#808080") #created divider that goes from edge to edge in gray
divider.pack(fill="x", pady=10) #fills horizontally with margin of padding 10px on both sides
for i in range(10): #creates 10 clipboard entries
    row_frame = tk.Frame(root) #create row frame for every clipboard entry
    row_frame.columnconfigure(0, weight=1) #column 0 expands, and absorbs space in between column 1
    row_frame.pack(fill="x", padx=15, pady=2) #stores rows vertically with invisible box stretching across to add a padding of 10px across and 2 up and down
    row_frames.append(row_frame) #stores for easy deletion
    width_within_300, width_beyond_300 = check_length()
    label = tk.Label(row_frame, text=f"{width_within_300}", wraplength=300, anchor="w", justify="left") #clipboard entry label wihin row_frame is added with a restriction of 220px across, whilst left aligned even if multiple lines long as well as space on right for commands
    label.grid(row=0, column=0, sticky="ew", padx=(0, 10)) #uses grid for rows and column easier placing labels at 0,0 within row frame whilst being stretched from west to east and with padding of 10 sides on bot

    command = tk.Label(row_frame, text=f"⌘ {i}", fg="#B1B1B1", anchor="e", justify="right") #separate label created within same row of light gray right aligned
    command.grid(row=0, column=1, sticky="e", padx=(0, 0)) #command text placed in next column right aligned
    commands.append(command)
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