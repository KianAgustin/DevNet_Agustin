"""
Module 2 — Activity: File Sorting with os and shutil
Student: Agustin, Kian Gabriel P
Date: September 26, 2026-

============================================
WHAT DID YOU BUILD? 6
============================================
the system allows to access your files and manage it based on the file type.


============================================
KEY VOCABULARY
============================================
- os module:a built in ssystem that allows your code to access directly with the operating system
- shutil module: collection of libraries inside python
- file path: this is the directory where are your files located
- directory: directory is the human readable location of a folder or file.
3


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil


fpath = input("Choose a Folder Path : ")

if os.path.exists(fpath):
    print("Path available!")
else:
    print("Sorry the path is not available :(")
    print("All folders & files:", os.listdir())


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what tripped you up while building this? e.g. a path that didn't
exist, a file that got overwritten, something that didn't work the
way you expected at first]
at first i was confused because i really dont know what we are gonna do. but when i get it i was able to code a little bit of the system


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
"""
