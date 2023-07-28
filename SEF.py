import numpy as np
import sys
import tkinter as tk
from tkinter import messagebox

# Message box
def message_box(msg, title = "Warning", stop = False):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo(title, msg)
    if stop:
        sys.exit()

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
    # Delete the non-unique ones
    indexes = np.unique(emoticons, return_index = True)[1]
    return [emoticons[index] for index in sorted(indexes)]

# Func. to split into multiple showcases
def showcase_split(emoticons, count, em_type, chr_lim):
    s = []
    # This method is for cutting by the characters
    if em_type == 0:
        a = ':' + ('::').join(emoticons) + ':'
        while len(a) > chr_lim:
            pointer = chr_lim - 1
            while count != 1:

                if a[pointer] == ':':

                    if a[pointer - 1] == ':':
                        s.append(a[:pointer])
                        a = a[pointer:]
                    else:
                        s.append(a[:pointer + 1])
                        a = a[pointer + 1:]
                    count -= 1
                    break
                else:
                    pointer -= 1
                    continue
        s.append(a)
        return s
    # This method is for cutting by the emoticons equally
    elif em_type == 1:
        start = 0
        for i in range(count):
            end = round(len(emoticons) * (i + 1) / count) + 1
            s.append(emoticons[start:end])
            start = end
        # Assemble all the emotcions into lines
        return [':' + ('::').join(i) + ':' for i in s]
    # If there is incorrect value in split_type oyu will see a message
    else:
        message_box(msg = "Check the value of split_type. It should be 0 or 1", stop = True)

def main():

    # Values to manage https://github.com/KroSheChKa/SteamEmoticonsFilter/edit/main/README.md#setting-preferences
    invert_emoticons = 1 # -1 invert | 1 keep unchanged
    showcase_count = 1 # Split emoticons into x showcases | 1/x
    split_type = 1 # How the string should 'fill' showcases | 0/1

    # You can set the limit for max symbol/character in each showcase
    character_limit = 8000 # x <= 8000 | Change it only if split_type = 0

    # Read emoticons and black list as strings
    emoticons_line_splitted = get_line(r'Text Files\Emoticons.txt')
    emoticons_black_list_splitted = get_line(r'Text Files\BlackList.txt')
    
    # Trying to catch incorrect string recognition
    if emoticons_black_list_splitted == None:
        message_box(msg = "Incorrect string recognition in BlackList.txt", stop = True)
    elif emoticons_line_splitted == None:
       message_box(msg = "Incorrect string recognition in Emoticons.txt", stop = True)
    else:
        emoticons_list = clean_up(emoticons_line_splitted, emoticons_black_list_splitted)

    # Split into multiple showcases
    emoticons_split_done = showcase_split(emoticons_list[::invert_emoticons],
                                          showcase_count,
                                          split_type,
                                          character_limit)

    res = ''
    # 8000 is the character limit for the Steam showcase
    for i in emoticons_split_done:
        if len(i) > 8000:
            message_box(msg = f"You have exceeded the character limit for the Steam showcase \n8000 < {len(emoticons_split_done)}")
            
            # Y/n 
            user_inp = messagebox.askyesno("Confirmation", "Write it to a file anyway?")

            # NO - quit. Yes - write.
            if user_inp == False:
                sys.exit()
            elif user_inp == True:
                break
        res += i + '\n\n'

    # Write the result in the file
    with open("Text Files\Result.txt", "w") as result:
        result.write(res)

if __name__ == '__main__':
    main()