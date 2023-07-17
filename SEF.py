import numpy as np
import sys
import tkinter as tk
from tkinter import messagebox

# Read emoticons and black list as strings
with open('Text Files\Emoticons.txt', "r") as emoticons:
    emoticons_line = emoticons.readline()[1:-1]
with open('Text Files\BlackList.txt', "r") as emoticons_blcklst:
    emoticons_black_list = emoticons_blcklst.readline()[1:-1]

# Split each string
emoticons_line_splitted = emoticons_line.split('::')
emoticons_black_list_splitted = emoticons_black_list.split('::')

# Trying to find a black-listed and if so delete
step = 0
while step < len(emoticons_line_splitted):
    if emoticons_line_splitted[step] in emoticons_black_list_splitted:
        del emoticons_line_splitted[step]
    else:
        step += 1

# Here is method of creating unique list without sorting it
indexes = np.unique(emoticons_line_splitted, return_index = True)[1]
emoticons_line_splitted = [emoticons_line_splitted[index] for index in sorted(indexes)]

# Assemble all the emotcions back into one line
emoticons_done = ':' + ('::').join(emoticons_line_splitted) + ':'

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
