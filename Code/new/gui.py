import tkinter as tk

clipboard = ["print('Hello World')", "import random", "total_lines = sum(1 for line in f)","    {word}: {count}","россия",
             "😎","johnsmith@gmail.com", "password", "  ", "Clipboard Entry 1!"]

root = tk.Tk() # create root window

# root window title and dimension
root.title("PastClip") #program name
root.geometry('375x440') #width x height window of 375x700px

i = 0 #integer that will change based on iteration

def quit_program(): #function when quit button is clicked
    quit()

def clear_clipboard():
    clipboard.clear()

    empty_label = tk.Label(root, text="Clipboard is empty") #creates label in root placement with text indicating the text to add
    empty_label.pack(before=label_1) #places empty_label before label_1

    label_1.destroy()
    label_2.destroy()
    label_3.destroy()
    label_4.destroy()
    label_5.destroy()
    label_6.destroy()
    label_7.destroy()
    label_8.destroy()
    label_9.destroy()
    label_10.destroy()
    delete.destroy()
    preferences_divider.destroy()
    root.geometry('375x190') #changes width x height window to 375x444px
#all widgets will be here
label = tk.Label(root, text="Select the clip to copy the entry to your clipboard!") #creates text in root layer
label.pack() #pack arranges label vertically
divider = tk.Frame(root, height=2, bg="gray") #created divider that goes from edge to edge in gray
divider.pack(fill="x", pady=10) #fills horizontally with margin of padding 10px on both sides
label_1 = tk.Label(root, text=f"{clipboard[-1]} ⌘0", anchor="w", justify="left") #anchor moves text to left side of label box and justify sends multiline text to left
label_1.pack()
label_2 = tk.Label(root, text=f"{clipboard[-2]} ⌘1")
label_2.pack()
label_3 = tk.Label(root, text=f"{clipboard[-3]} ⌘2")
label_3.pack()
label_4= tk.Label(root, text=f"{clipboard[-4]} ⌘3")
label_4.pack()
label_5 = tk.Label(root, text=f"{clipboard[-5]} ⌘4")
label_5.pack()
label_6 = tk.Label(root, text=f"{clipboard[-6]} ⌘5")
label_6.pack()
label_7 = tk.Label(root, text=f"{clipboard[-7]} ⌘6")
label_7.pack()
label_8 = tk.Label(root, text=f"{clipboard[-8]} ⌘7")
label_8.pack()
label_9 = tk.Label(root, text=f"{clipboard[-9]}! ⌘8")
label_9.pack()
label_10 = tk.Label(root, text=f"{clipboard[-10]} ⌘9")
label_10.pack()
divider = tk.Frame(root, height=2, bg="gray")
divider.pack(fill="x", pady=10)
delete = tk.Button(root, text="Clear all clipboard entries", command=clear_clipboard) #creates interactable button for deleting clipboard entries
delete.pack(fill="x", pady=5) #button extends across horizontal window for maximum coverage to click
preferences_divider = tk.Frame(root, height=2, bg="gray")
preferences_divider.pack(fill="x", pady=10) 
preferences = tk.Label(root, text="Preferences")
preferences.pack()
divider = tk.Frame(root, height=2, bg="gray")
divider.pack(fill="x", pady=10)
button = tk.Button(root, text="Quit", command=quit_program)
button.pack(fill="x", pady=5)
divider = tk.Frame(root, height=2, bg="gray")
divider.pack(fill="x", pady=10)

root.mainloop() # execute Tkinter
