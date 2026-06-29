import mimetypes #supports proper file types
import pyperclip #supports copying and pasting text from clipboard
from datetime import datetime
from pathlib import Path
from datetime import datetime
from PIL import Image, ImageGrab

class Entry():
    def __init__(self, #creates initialisisation function for class and parameters

            # identifiers
            source_app,
            date_time_copied,

            # text data
            character_length,
            line_count,
            word_count,

            # file metadata
            file_name,
            file_extension,
            file_type,
            file_path,
            file_size,

            # image metadata
            width,
            height,

            # behavior
            favourite,
            tags,
            folder,
            exists,
            data,
        ):

        self.source_app = source_app #self values stores the object parameters under self
        self.date_time_copied = date_time_copied

        self.character_length = character_length
        self.line_count = line_count
        self.word_count = word_count

        self.file_name = file_name
        self.file_extension = file_extension
        self.file_type = file_type
        self.file_path = file_path
        self.file_size = file_size

        self.width = width
        self.height = height

        self.favourite = favourite
        self.tags = tags
        self.folder = folder
        self.exists = exists

        self.data = data

i = 0 #gives i variable value of 0 for accesing list index and looping

def get_time():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S") #fetches current date and formats into # DD/MM/YYYY HH:MM:SS

date_list = [] #chronological list order of dates
date_list.append(get_time()) #adds date and time to chronological order list
entries = [] #list of entries with info associated
images_list = []  #list of image entries
tags = [] #list of tags
tag_item = ""
folder_list = []
folder = ""


entries.append(Entry( #appends individual entries under Entry class, so information is saved based off list index
    # identifiers
    source_app = "Notes",
    date_time_copied = date_list[-1],

    # text data
    character_length = 30,
    line_count = 2,
    word_count = 24,

    # file metadata
    file_name = "text.txt",
    file_extension = "txt",
    file_type = "text/txt",
    file_path = "/Users/connorlourens/Downloads/text.txt",
    file_size = 38,

    # image metadata
    width = 0,
    height = 0,

    # behavior
    favourite = False,
    tags = [],
    folder = "",
    exists = True,

    # stored data
    data = pyperclip.paste()
))

entries.append(Entry(
    # identifiers
    source_app = "Anki",
    date_time_copied = date_list[-1],

    # text data
    character_length = 0,
    line_count = 0,
    word_count = 0,

    # file metadata
    file_name = "image.jpeg",
    file_extension = "jpeg",
    file_type = "image/jpeg",
    file_path = "/Users/connorlourens/Downloads/image.jpeg",
    file_size = 1286,

    # image metadata
    width = 1920,
    height = 1080,

    # behavior
    favourite = False,
    tags = [],
    folder = "",
    exists = True,

    # stored data
    data = pyperclip.paste()
))

entries.append(Entry( #appends individual entries under Entry class, so information is saved based off list index
    # identifiers
    source_app = "Notes",
    date_time_copied = date_list[-1], #✅

    # text data
    character_length = 30, #✅
    line_count = 2, #✅
    word_count = 24, #✅

    # file metadata
    file_name = "text.txt", 
    file_extension = "txt",
    file_type = "text/txt",
    file_path = "/Users/connorlourens/Downloads/text.txt",
    file_size = 38,

    # image metadata
    width = 0, #✅
    height = 0, #✅

    # behavior
    favourite = False, #✅
    tags = [], #✅
    folder = "", #✅
    exists = True,

    # stored data
    data = pyperclip.paste() #✅
))

def clipboard_copy_image(output_file_name=None):
    global ofng #makes variable accessible outside of function as is parameter
    ofng = output_file_name #assigns duplicate variable of parameter (output file_name globalo)
    if output_file_name is None: #checks if no entries in images_list
        output_file_name = f"copied_image_{len(images_list)+1}.png" #creates integer variable for image name to be saved as

    clipboard_image = ImageGrab.grabclipboard() #extracts image from clipboard

    if clipboard_image is None: #stops running program if clipboard entry is not an image
        return

    clipboard_image.save(output_file_name, "PNG") #saves clipboard entry as a PNG file
    images_list.append(output_file_name) #adds file name to images_list to indicate how many images exist

clipboard_copy_image()

"""for i in range(len(entries)): #loops for amount of times based on how many entries exist
    f = open(f"clipboard_entry_{i+1}.txt", "x") #creates new .txt file and gives name based on amount of clipboard entries
    with open(f"clipboard_entry_{i+1}.txt", "a") as f: #opens and appends info to new .txt file
        f.write(entries[i].data) #data being appended to the new .txt file
        i+=1
"""
#text data
"""
character_length = (len(entries[-1].data)) #finds length of text
line_count = len(entries[-1].data.splitlines()) #splits string into list at line breaks and counts line breaks
word_count = len(entries[-1].data.split()) #removes white space in between words (spaces) or on end of words, e,g tab/double space...
"""
#file metadata
"""
file_name = entries[-1].Path.name, 
file_extension = entries[-1].Path.suffix
file_type = entries[-1].Path.suffix
file_type = file_type.replace(".", "")
file_path = entries[-1].Path.parent,
file_size = entries[-1].Path(path).stat().stat_suze,
#meta data all extracted from pathlib library

print(file_size)
"""

#image metadata
try:
    with Image.open(images_list[i]) as img: #opens copied image to clipboard
        width, height = img.size #saves width and height tuple to img.size variable
except IndexError: #error that may pop up if there are no image entries inside the list
    pass

#behaviour
favourite = input("Would you like to favourite this entry? (Y/N): ").upper() #gets user input and when letter converts result (favourite) to uppercase, e.g y > Y to narrow options

while favourite not in ["Y", "N"]: #repeats until user provides valid option options for valid answer
    print("Invalid input. Please enter Y or N.")
    favourite = input("Would you like to favourite this entry? (Y/N): ").upper()

while True: #loops asking for tags to assign
    tag_item = input("Add tags one at a time you would like to assign to this entry: ")
    tags.append(tag_item)
    if not tag_item: #if no tag given ends loop
        break #ends tag-adding loop loop

while True: #loops asking for folders to assign
    folder = input("Add folders one at a time you would like to assign to this entry: ")
    if folder not in folder_list: #checks for duplicate entries
        folder_list.append(folder) #list of folders
    else:
        print(f"Entry already in {folder_list[-1]} folder") #when folder already exists
    if not folder: #if no tag given ends loop
        folder_list.remove(folder_list[-1]) #removes last blank entry
        break #ends folder-adding loop

clipboard_txt = f"clipboard_entry_{i}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt" #********************************************************************************************************
path = '/Users/connorlourens/Library/CloudStorage/GoogleDrive-23139@student.macleans.school.nz/My Drive/[Connor Lourens] 91896_Project Overview Structure.docx'
