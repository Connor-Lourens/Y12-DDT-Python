import pyperclip # Allows the program to read and copy clipboard content.
import tkinter as tk # Provides tools to create the GUI.
from idlelib.tooltip import Hovertip # Adds tooltips that appear when hovering over widgets.
from tkinter.font import nametofont # Allows access to named Tkinter fonts.
from tkinter import messagebox # Displays pop-up message boxes.
from datetime import datetime # Provides the current date and time.
from pathlib import Path # Gets path of files.

# checks if clipboard.txt exists, if not creates it.
file_path = Path("clipboard.txt")
if file_path.is_file():
    pass
else:
    open("clipboard.txt", "w").close()


root = tk.Tk()
root.title("PastClip")
root.option_add("*Font", "Inter 11")


# dimensions of window as per number of clipboard entries
HEIGHT_DIMENSIONS = { 
    0: 140,
    1: 200,
    2: 230,
    3: 260,
    4: 290,
    5: 320,
    6: 340,
    7: 370,
    8: 430,
    9: 440,
    10: 460
}

empty_label = None
display_clear_entries = False


def get_time():
    """Return the current date and time as a formatted string."""
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")


with open("clipboard.txt", "r", encoding="utf-8") as file:
    clipboard = []

    for line in file:
        if line.strip():
            clipboard.append(
                line.rstrip("\n").replace("<NEWLINE>", "\n")
            )

num_entries = len(clipboard) #counts list entries

num_entries = len(clipboard)

window_height = HEIGHT_DIMENSIONS.get(num_entries, 460) #retrieves dict value
# corresponing with key, if neither sets to 460

root.geometry(f"375x{window_height}") #sets dimensions for window based on
# how many entries exist
root.minsize(375, 140) #minimum window size


i = 0 #integer that will change based on iteration


#storage for easy tracking
labels = []
row_frames = []
commands = []
dates = []

last_clipboard = pyperclip.paste() #most recent clipboard entry


def quit_program(): #function when quit button is clicked
    """Close the PastClip application."""
    root.destroy()


def clear_clipboard():
    """Clear all saved clipboard entries and update the interface."""
    global empty_label

    empty_label = tk.Label(
        root,
        text="Clipboard is empty"
    )

    empty_label.pack(before=row_frames[0]) #places empty_label before label[i]
    # is removed

    for row_frame in row_frames:
        row_frame.destroy()

    row_frames.clear()
    commands.clear()
    labels.clear()
    clipboard.clear()

    root.geometry('375x140')

    with open("clipboard.txt", "w", encoding="utf-8") as file:
        file.write("")

    update_clear_button()


def check_clipboard():
    """Check for new clipboard content and update the saved history."""
    global last_clipboard, empty_label

    current_clipboard = pyperclip.paste()

    if current_clipboard != last_clipboard:
        last_clipboard = current_clipboard

        if current_clipboard.strip(): #removes whitespace and empty entries
            if current_clipboard in clipboard: #checks if entry already exists
                clipboard.remove(current_clipboard) #removes duplicate entry

            clipboard.insert(0, current_clipboard) #adds newest entry to beginning
            del clipboard[10:] #removes entries past the first 10

            with open("clipboard.txt", "w", encoding="utf-8") as file:
                for entry in clipboard:
                    file.write(
                        entry.replace("\n", "<NEWLINE>") + "\n"
                    )

            if empty_label is not None: #removes empty message if it exists
                empty_label.destroy()
                empty_label = None

            row_frame = tk.Frame(root) #creates a new row for the new clipboard entry

            row_frame.columnconfigure(
                0,
                weight=1,
                minsize=280
            )

            row_frame.columnconfigure(
                1,
                minsize=45
            )

            if row_frames: #places new row before existing entries
                row_frame.pack(
                    fill="x",
                    padx=15,
                    pady=2,
                    before=row_frames[0]
                )
            else:
                row_frame.pack(
                    fill="x",
                    padx=15,
                    pady=2,
                    before=entries_bottom_divider
                )

            row_frames.insert(0, row_frame) #stores frame for easy deletion later

            global clean_text
            clean_text = current_clipboard.replace("\n", " ")

            clipboard_text_button = tk.Label(
                row_frame,
                text=clean_text,
                height=1,
                anchor="w", 
                justify="left",
                bg="#435363",
                activebackground=hex_colour,
                fg="#FFFFFF"
            )

            clipboard_text_button.grid(
                            row=0,
                            column=0,
                            sticky="ew",
                            padx=(0, 0)
                        )

            Hovertip(
                clipboard_text_button,
                current_clipboard
            ) #shows full entry when hovering

            clipboard_text_button.bind(
                "<Button-1>",
                clipboard_clicked
            ) #copies entry when clicked

            clipboard_text_button.bind("<Enter>", on_hover)
            clipboard_text_button.bind("<Leave>", on_leave)

            labels.insert(0, clipboard_text_button) #stores label for easy tracking

            shortcut_number = i + 1 if i < 9 else 0

            command = tk.Label(
                row_frame,
                text=f"⌘ {shortcut_number}",
                fg="#808080",
                anchor="e",
                justify="right"
            )

            command.grid(
                row=0,
                column=1,
                sticky="e"
            ) #places shortcut label in second column

            commands.insert(0, command) #stores command for easy tracking

            if len(row_frames) > 10: #removes oldest row if more than 10 entries
                row_frames.pop().destroy()
                labels.pop()
                commands.pop()

            for index, command_label in enumerate(commands): #updates shortcut numbers by checking if in list of numbers for commands
                shortcut_number = index + 1 if index < 9 else 0

                command_label.config(
                    text=f"⌘ {shortcut_number}"
                )

            root.geometry(
                f"375x{HEIGHT_DIMENSIONS.get(len(clipboard), 440)}"
            ) #updates window height

            update_clear_button()

    root.after(1000, check_clipboard) #checks for new clipboard entries every second


def clipboard_clicked(event):
    """Copy the selected clipboard entry when its label is clicked."""
    global last_clipboard

    selected_entry = event.widget.cget("text") #retrieves text from selected entry upon clicking

    pyperclip.copy(selected_entry) #copies text to clipboard
    last_clipboard = selected_entry


def copy_history_entry(index):
    """Copy a clipboard history entry selected by its shortcut index."""
    global last_clipboard

    if index < len(clipboard): #assesses whether index is less than the amount of entries in clipboard list
        selected_entry = clipboard[index] #sets selected_entry as equal to clipboard entry at certain index

        pyperclip.copy(selected_entry) 
        last_clipboard = selected_entry


for index in range(10):
    shortcut_number = index + 1 if index < 9 else 0

    root.bind_all(
        f"<Command-KeyPress-{shortcut_number}>",
        lambda event, index=index: copy_history_entry(index) #creates event with index set to value of index within stage of loop, and when lambda is triggered
    )


rgb = root.winfo_rgb("systemControlAccentColor") #retrieves MacOS accent colour

r, g, b = rgb[0] >> 8, rgb[1] >> 8, rgb[2] >> 8 #shifts from 8-bit RGB to hexcode

hex_colour = f"#{r:02x}{g:02x}{b:02x}" #formats bits into hexcode


def on_hover(e):
    """Change the clipboard entry background to the system accent colour."""
    e.widget['background'] = f'{hex_colour}'


def on_leave(e):
    """Restore the clipboard entry's default background colour."""
    e.widget['background'] = '#435363'


def get_time():
    """Return the current date and time as a formatted string."""
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S") #fetches current date and formats into # DD/MM/YYYY HH:MM:SS


#all widgets will be here
label = tk.Label(
    root,
    text="Click the clip to copy the entry to your clipboard!",
    fg="#B1B1B1"
) #creates text in root layer

label.pack(pady=(10, 0)) #pack arranges label vertically


entries_divider = tk.Frame(
    root,
    width=350,
    height=1,
    bg="#808080"
) #created divider that goes from edge to edge in gray

entries_divider.pack(pady=10) #fills horizontally with margin of padding 10px on both sides


if clipboard == []:
    empty_label = tk.Label(
        root,
        text="Clipboard is empty"
    )

    empty_label.pack()
    display_clear_entries = False

else:
    for i in range(min(len(clipboard), 10)): #creates 10 clipboard entries
        row_frame = tk.Frame(root) #create row frame for every clipboard entry

        row_frame.columnconfigure(
            0,
            weight=1,
            minsize=280
        ) #column 0 takes space it needs horizontally within limit of weight 1 with minimum size of 280px

        row_frame.columnconfigure(1, minsize=45)

        row_frame.pack(
            fill="x",
            padx=15,
            pady=2
        ) #stores rows vertically with invisible box stretching across to add a padding of 10px across and 2 up and down

        row_frames.append(row_frame)

        global clean_text
        clean_text = clipboard[i].replace("\n", " ") # FIXED: changed from current_clipboard to clipboard[i]

        clipboard_text_button = tk.Label(
            row_frame,
            text=clean_text,
            height=1,
            anchor="w",
            justify="left",
            bg="#435363",
            activebackground=f"{hex_colour}",
            fg="#FFFFFF"
        )
        
        clipboard_text_button.grid(
                row=0,
                column=0,
                sticky="ew",
                padx=(0, 0)
            )#clipboard entry label wihin row_frame is added with a restriction of 300px across, whilst left aligned even if multiple lines long as well as space on right for commands

        dates.append(get_time())

        Hovertip(clipboard_text_button, dates[i])

        clipboard_text_button.bind(
            "<Enter>",
            on_hover,
            add="+"
        ) #creates hover bindings, and preserves old ones

        clipboard_text_button.bind(
            "<Leave>",
            on_leave,
            add="+"
        )

        clipboard_text_button.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=(0, 0)
        ) #uses grid for rows and column easier placing labels at 0,0 within row frame whilst being stretched from west to east and with padding of 10 sides on bot

        clipboard_text_button.bind(
            "<Button-1>",
            clipboard_clicked
        ) #when left clicked done run clipboard_clicked

        shortcut_number = i + 1 if i < 9 else 0

        command = tk.Label(
            row_frame,
            text=f"⌘ {shortcut_number}",
            fg="#808080",
            anchor="e",
            justify="right"
        )

        command.grid(
            row=0,
            column=1,
            sticky="e",
            padx=(0, 0)
        )

        commands.append(command)
        labels.append(clipboard_text_button) #adds individual entries to list to store for later


entries_bottom_divider = tk.Frame(
    root,
    width=350,
    height=1,
    bg="#808080"
)

entries_bottom_divider.pack(pady=10)


delete = tk.Label(
    root,
    text="Clear all clipboard entries",
    bg=root.cget("bg"),
    cursor="hand2",
    justify="left",
    anchor="w",
    fg="#808080"
)
delete.bind("<Button-1>", lambda event: clear_clipboard())


quit_divider = tk.Frame(
    root,
    width=350,
    height=1,
    bg="#808080"
)


quit_button = tk.Label(
    root,
    text="Quit",
    bg=root.cget("bg"),
    cursor="hand2",
    anchor="w",
    fg="#808080"
)

quit_button.bind("<Button-1>", lambda event: quit_program())

quit_button.pack(
    fill="x",
    padx=12,
    pady=5
)


def update_clear_button():
    """Show or hide the clear button depending on clipboard contents."""
    if clipboard:
        delete.pack(
            fill="x",
            padx=12,
            before=quit_button
        )

        quit_divider.pack(
            pady=10,
            before=quit_button
        )

    else:
        delete.pack_forget()  # hides button when no entries exist
        quit_divider.pack_forget()


divider = tk.Frame(
    root,
    width=350,
    height=1,
    bg="#808080"
)

divider.pack(pady=10)

check_clipboard()
update_clear_button()

root.mainloop() # execute