import tkinter as tk

clipboard = ["Clipboard Entry 10!", "Clipboard Entry 9!", "Clipboard Entry 8!", "Clipboard Entry 7!", "Clipboard Entry 6!",
             "Clipboard Entry 5!", "Clipboard Entry 4!", "Clipboard Entry 3!", "Clipboard Entry 2!", "Clipboard Entry 1!"]

def quit_program(): #function when quit button is clicked
    quit()

root = tk.Tk() # create root window

# root window title and dimension
root.title("PastClip") #program name
root.geometry('375x700') #width x height window of 375x700

#all widgets will be here
label = tk.Label(root, text="Select the clip to copy the entry to your clipboard!") #creates text in root layer
label.pack() #pack arranges label vertically
divider = tk.Frame(root, height=2, bg="gray") #created divider that goes from edge to edge in gray
divider.pack(fill="x", pady=10) #fills horizontally with margin of padding 10px on both sides
label_1 = tk.Label(root, text=f"{clipboard[-1]} ⌘0")
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
delete = tk.Label(root, text="Delete all clipboard entries")
delete.pack()
divider = tk.Frame(root, height=2, bg="gray")
divider.pack(fill="x", pady=10) 
preferences = tk.Label(root, text="Preferences")
preferences.pack()
divider = tk.Frame(root, height=2, bg="gray")
divider.pack(fill="x", pady=10)
button = tk.Button(root, text="Quit", command=quit_program)
button.pack(fill="x", pady=5)
divider = tk.Frame(root, height=2, bg="gray")
divider.pack(fill="x", pady=10)






root.mainloop() # execute Tkinter
