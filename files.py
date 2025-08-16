# -*- coding: utf-8 -*-
"""
Created on Sat Aug 16 05:35:57 2025

@author: motlatsi seeko
"""

def modify_file_content(filename):
    try:
        # Try to open and read the original file
        with open(filename, 'r') as infile:
            content = infile.read()

        # Modify content: convert to uppercase
        modified_content = content.upper()

        # Write modified content to a new file
        with open('modified_output.txt', 'w') as outfile:
            outfile.write(modified_content)

        print("✅ Success! Modified content has been written to 'modified_output.txt'.")

    except FileNotFoundError:
        print("❌ Error: The file you entered does not exist.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

# Ask user for the file name
user_filename = input("Enter the filename you want to read: ")
modify_file_content(user_filename)
