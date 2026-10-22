import pyperclip
import tkinter as tk
from tkinter.font import nametofont 
from tkinter import messagebox

with open('clipboard.txt', 'r', encoding='utf-8') as f: #reads clipboard file and closes when finished
    clipboard = [line.strip() for line in f.readlines()] #removes whitespace, and new lines creating list of entries created from .txt file

with open("clipboard.txt", "w", encoding="utf-8") as file: #save clipboard entries
    for entry in clipboard:
        file.write(entry + "\n")

with open("clipboard.txt", "r", encoding="utf-8") as file: #load clipboard entries
    clipboard = file.read() #puts clipboard entries on other lines

root = tk.Tk() #create root window

root.title("PastClip") #program name

height_dimensions = { #amount of clipboard entries
    1: 210,
    2: 230,
    3: 260,
    4: 300,
    5: 320,
    6: 340,
    7: 360,
    8: 390,
    9: 410,
    10:440
}

with open("clipboard.txt", "w", encoding="utf-8") as file:
    paste = pyperclip.paste()
    file.write(paste) #creates new clipboard entries

with open("clipboard.txt", "r", encoding="utf-8") as file: #opens .txt file
    clipboard = file.read().split() #string becomes list of separate entries

num_entries = len(clipboard) #counts list entries
    
count = clipboard.count("\n")
with open("clipboard.txt", "r", encoding="utf-8") as file:
    newline_count = file.read().count("\n")

num_entries = len(clipboard)
window_height = height_dimensions.get(num_entries) #retrieves dict value corresponing with key
root.geometry(f"375x{window_height}") #sets dimensions for window based on how many entries exist

i = 0 #integer that will change based on iteration

#storage for easy tracking
labels = []
row_frames = []
commands = []

def quit_program(): #function when quit button is clicked
    quit()

def clear_clipboard():
    empty_label = tk.Label(root, text="Clipboard is empty")
    empty_label.pack(before=row_frames[0]) #places empty_label before label[i] is removed
    for i in range(10):
        row_frames[i].destroy()
        commands[i].destroy()
        i+=1
    delete.destroy()
    quit_divider.destroy()
    root.geometry('375x140')

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

def clipboard_clicked(event):
    pyperclip.copy(event.widget.cget("text")) #copies entries when clicked

rgb = root.winfo_rgb("systemControlAccentColor") #retrieves MacOS accent colour

r, g, b = rgb[0] >> 8, rgb[1] >> 8, rgb[2] >> 8 #shifts from 8-bit RGB to hexcode
hex_colour = f"#{r:02x}{g:02x}{b:02x}" #formats bits into hexcode

def on_hover(e):
    e.widget['background'] = f'{hex_colour}'

def on_leave(e):
    e.widget['background'] = '#435363'

#all widgets will be here
label = tk.Label(root, text="Select the clip to copy the entry to your clipboard!", fg="#B1B1B1") #creates text in root layer
label.pack() #pack arranges label vertically
divider = tk.Frame(root, height=2, bg="#808080") #created divider that goes from edge to edge in gray
divider.pack(fill="x", pady=10) #fills horizontally with margin of padding 10px on both sides
for i in range(len(clipboard)): #creates 10 clipboard entries
    row_frame = tk.Frame(root) #create row frame for every clipboard entry
    row_frame.columnconfigure(0, weight=1) #column 0 expands, and absorbs space in between column 1
    row_frame.pack(fill="x", padx=15, pady=2) #stores rows vertically with invisible box stretching across to add a padding of 10px across and 2 up and down
    row_frames.append(row_frame) #stores for easy deletion
    width_within_300, width_beyond_300 = check_length()
    clipboard_text_button = tk.Label(row_frame, text=f"{width_within_300}", wraplength=300, anchor="w", justify="left", bg="#435363",activebackground=f"{hex_colour}",) #clipboard entry label wihin row_frame is added with a restriction of 220px across, whilst left aligned even if multiple lines long as well as space on right for commands
    clipboard_text_button.bind("<Enter>", on_hover)
    clipboard_text_button.bind("<Leave>", on_leave)
    clipboard_text_button.grid(row=0, column=0, sticky="ew", padx=(0, 0)) #uses grid for rows and column easier placing labels at 0,0 within row frame whilst being stretched from west to east and with padding of 10 sides on bot
    clipboard_text_button.bind("<Button-1>", clipboard_clicked) #when left clicked done run clipboard_clicked
    clipboard_text_button.bind("<Enter>", on_hover)
    clipboard_text_button.bind("<Leave>", on_leave)
    clipboard_text_button.bind("<Command-Key-1>", clipboard_clicked) #when left clicked done run clipboard_clicked
    command = tk.Label(row_frame, text=f"⌘ {i}", fg="#B1B1B1", anchor="e", justify="right") #separate label created within same row of light gray right aligned
    command.grid(row=0, column=1, sticky="e", padx=(0, 0)) #command text placed in next column right aligned
    commands.append(command)
    labels.append(label) #adds individual labels to list to store for later
divider = tk.Frame(root, height=2, bg="#808080")
divider.pack(fill="x", pady=10)
delete = tk.Button(root, text="Clear all clipboard entries", command=clear_clipboard) #creates interactable button for deleting clipboard entries
delete.pack(fill="x", padx=80, pady=5) #button extends across horizontal window for maximum coverage to click
quit_divider = tk.Frame(root, height=2, bg="#808080")
quit_divider.pack(fill="x", pady=10)
quit_button = tk.Button(root, text="Quit", bg="#808080", command=quit_program)
quit_button.pack(fill="x", padx=80, pady=5)
divider = tk.Frame(root, height=2, bg="#808080")
divider.pack(fill="x", pady=10)



root.mainloop() # execute Tkinter