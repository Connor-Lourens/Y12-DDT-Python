import pyperclip
import tkinter as tk
from idlelib.tooltip import Hovertip
from tkinter.font import nametofont
from tkinter import messagebox
from datetime import datetime

root = tk.Tk()
root.title("PastClip")
height_dimensions = { #amount of clipboard entries
    0: 140,
    1: 210,
    2: 230,
    3: 260,
    4: 300,
    5: 320,
    6: 340,
    7: 360,
    8: 390,
    9: 410,
    10: 440
}
display_clear_entries = False

def update_time():
    time_label.config(text=get_time())
    root.after(1000, update_time)

with open("clipboard.txt", "r", encoding="utf-8") as file: #opens clipboard.txt to read
    clipboard = [line.strip() for line in file if line.strip()] #reads through every line removing empty white spaces and entries then adding to clipboard the result

num_entries = len(clipboard) #counts list entries
    
count = clipboard.count("\n")
with open("clipboard.txt", "r", encoding="utf-8") as file:
    newline_count = file.read().count("\n")

num_entries = len(clipboard)
window_height = height_dimensions.get(num_entries, 440) #retrieves dict value corresponing with key, if neither sets to 440
root.geometry(f"375x{window_height}") #sets dimensions for window based on how many entries exist

i = 0 #integer that will change based on iteration

#storage for easy tracking
labels = []
row_frames = []
commands = []
dates = []

last_clipboard = pyperclip.paste() #most recent clipboard entry

def quit_program(): #function when quit button is clicked
    root.destroy()

def clear_clipboard():
    empty_label = tk.Label(root, text="Clipboard is empty")
    empty_label.pack(before=row_frames[0]) #places empty_label before label[i] is removed
    for row_frame in row_frames:
        row_frame.destroy()
    row_frames.clear()
    commands.clear()
    labels.clear()
    clipboard.clear()
    delete.destroy()
    quit_divider.destroy()
    root.geometry('375x140')
    with open("clipboard.txt", "w", encoding="utf-8") as file:
        file.write("")

def check_clipboard():
    global last_clipboard
    current_clipboard = pyperclip.paste()
    
    if current_clipboard != last_clipboard:
        last_clipboard = current_clipboard
        if current_clipboard.strip(): #removes whitespace, and empty entries
            clipboard.insert(0, current_clipboard) #adds most recent clipboard entry to beginning of list

            with open("clipboard.txt", "w", encoding="utf-8") as file:
                file.write("\n".join(clipboard) + "\n")

            #create a new row for the new clipboard entry
            row_frame = tk.Frame(root)
            row_frame.pack(fill="x", padx=15, pady=2)
            row_frames.insert(0, row_frame) #stores frame for easy deletion later

            label = tk.Label(row_frame, text=current_clipboard, wraplength=300, anchor="w", justify="left", bg="#435363", fg="white")
            label.pack(fill="x")
            label.bind("<Button-1>", clipboard_clicked) #copies entry when clicked
            label.bind("<Enter>", on_hover)
            label.bind("<Leave>", on_leave)
            labels.insert(0, label) #stores label for easy tracking
            command = tk.Label(row_frame, text=f"⌘ {i}", fg="#B1B1B1", anchor="e", justify="right") #separate label created within same row of light gray right aligned
            command.pack(row=0, column=1, sticky="e", padx=(0, 0)) #command text placed in next column right aligned
            commands.append(command)
            labels.append(label) #adds individual labels to list to store for later


    root.after(500, check_clipboard) #every 500ms checks if there are new clipboard entries

def clipboard_clicked(event):
    pyperclip.copy(event.widget.cget("text")) #copies entries when clicked

rgb = root.winfo_rgb("systemControlAccentColor") #retrieves MacOS accent colour

r, g, b = rgb[0] >> 8, rgb[1] >> 8, rgb[2] >> 8 #shifts from 8-bit RGB to hexcode
hex_colour = f"#{r:02x}{g:02x}{b:02x}" #formats bits into hexcode

def on_hover(e):
    e.widget['background'] = f'{hex_colour}'

def on_leave(e):
    e.widget['background'] = '#435363'

def get_time():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S") #fetches current date and formats into # DD/MM/YYYY HH:MM:SS

#all widgets will be here
label = tk.Label(root, text="Select the clip to copy the entry to your clipboard!", fg="#B1B1B1") #creates text in root layer
label.pack() #pack arranges label vertically
divider = tk.Frame(root, height=2, bg="#808080") #created divider that goes from edge to edge in gray
divider.pack(fill="x", pady=10) #fills horizontally with margin of padding 10px on both sides
if clipboard == []:
    empty_label = tk.Label(root, text="Clipboard is empty")
    empty_label.pack()
    display_clear_entries = False
else:
    if len(clipboard) < 11:
        for i in range(len(clipboard)): #creates 10 clipboard entries
            row_frame = tk.Frame(root) #create row frame for every clipboard entry
            row_frame.columnconfigure(0, weight=1) #column 0 expands, and absorbs space in between column 1
            row_frame.pack(fill="x", padx=15, pady=2) #stores rows vertically with invisible box stretching across to add a padding of 10px across and 2 up and down
            row_frames.append(row_frame) #stores for easy deletion
            clipboard_text_button = tk.Label(row_frame, text=clipboard[i], wraplength=300, anchor="w", justify="left", bg="#435363",activebackground=f"{hex_colour}",) #clipboard entry label wihin row_frame is added with a restriction of 220px across, whilst left aligned even if multiple lines long as well as space on right for commands
            clipboard_text_button.bind("<Enter>", on_hover)
            clipboard_text_button.bind("<Leave>", on_leave)
            clipboard_text_button.grid(row=0, column=0, sticky="ew", padx=(0, 0)) #uses grid for rows and column easier placing labels at 0,0 within row frame whilst being stretched from west to east and with padding of 10 sides on bot
            clipboard_text_button.bind("<Button-1>", clipboard_clicked) #when left clicked done run clipboard_clicked
            command = tk.Label(row_frame, text=f"⌘ {i}", fg="#B1B1B1", anchor="e", justify="right") #separate label created within same row of light gray right aligned
            command.grid(row=0, column=1, sticky="e", padx=(0, 0)) #command text placed in next column right aligned
            commands.append(command)
            labels.append(label) #adds individual labels to list to store for later
divider = tk.Frame(root, height=2, bg="#808080")
divider.pack(fill="x", pady=10)
delete = tk.Button(root, text="Clear all clipboard entries", command=clear_clipboard) #creates interactable button for deleting clipboard entries
if display_clear_entries:
    delete.pack(fill="x", padx=80, pady=5)
    quit_divider = tk.Frame(root, height=2, bg="#808080")
    quit_divider.pack(fill="x", pady=10)
else:
    delete.pack_forget()
quit_button = tk.Button(root, text="Quit", bg="#808080", command=quit_program)
quit_button.pack(fill="x", padx=80, pady=5)
divider = tk.Frame(root, height=2, bg="#808080")
divider.pack(fill="x", pady=10)

time_label = tk.Label(root, text=get_time())
time_label.pack()

update_time()

check_clipboard()

root.mainloop() # execute