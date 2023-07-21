import numpy as np
import sys
import tkinter as tk
from tkinter import messagebox

# Read the lines in file that do not starts with # or empty
def get_line(file_path):
    
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if len(line) != 0 and not line.startswith('#'):
                # Remove 1st and last symbol and split each string
                return line[1:-1].split('::')

# Trying to find a black-listed and if so delete + unique
def clean_up(emoticons, black_list):
    step = 0
    while step < len(emoticons):
        if emoticons[step] in black_list:
            del emoticons[step]
        else:
            step += 1
    # Delete the non-unique
    indexes = np.unique(emoticons, return_index = True)[1]
    return [emoticons[index] for index in sorted(indexes)]

# Read emoticons and black list as strings
emoticons_line_splitted = get_line(r'Text Files\Emoticons.txt')
emoticons_black_list_splitted = get_line(r'Text Files\BlackList.txt')

emoticons_list = clean_up(emoticons_line_splitted, emoticons_black_list_splitted)

# Assemble all the emotcions back into one line
emoticons_done = ':' + ('::').join(emoticons_list) + ':'

# 8000 is the character limit for the Steam showcase
if len(emoticons_done) > 8000:
    while True:
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("Warning", f"You have exceeded the character limit for the Steam showcase \n8000 < {len(emoticons_done)}")

        user_inp = messagebox.askyesno("Confirmation", "Write it to a file anyway?")

        if user_inp == False:
            sys.exit()
        elif user_inp == True:
            break
        
# Write the result in the file
with open("Text Files\Result.txt", "w") as result:
    result.write(emoticons_done)
