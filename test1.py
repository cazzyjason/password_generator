import random
import string
import tkinter as tk
import pyperclip
from tkinter import BooleanVar

def generate_password(length, include_special, lowercase_only):
    # Define the character sets to use in the password
    if lowercase_only:
        letters = string.ascii_lowercase
    else:
        letters = string.ascii_letters
    digits = string.digits
    special_characters = string.punctuation

    # Create a list of characters based on the desired password options
    all_characters = list(letters + digits)
    if include_special:
        all_characters += special_characters

    # Shuffle the list to create a random order
    random.shuffle(all_characters)

    # Take the first `length` characters from the shuffled list
    password = ''.join(random.sample(all_characters, length))

    return password

def generate_and_display_password():
    # Get the desired password length from the user
    length_str = length_entry.get()

    # Validate that the length is a positive integer
    if length_str == "":
        password_label.configure(text="請先輸入密碼長度。")#Please enter a password length.
        return
    elif not length_str.isdigit() or int(length_str) <= 0:
        password_label.configure(text="請輸入有效的密碼長度。")#Please enter a valid password length.
        return

    length = int(length_str)

    # Generate a password of the desired length and with the desired options
    password = generate_password(length, include_special.get(), lowercase_only.get())

    # Display the password in the UI
    password_label.configure(text=password)

    # Enable the "Copy" button
    copy_button.configure(state="normal")

    # Save the password to the clipboard
    pyperclip.copy(password)

def copy_password():
    # Get the password from the label
    password = password_label.cget("text")

    # Save the password to the clipboard
    pyperclip.copy(password)

# Create the main window
window = tk.Tk()
window.title("高強度密碼生成器")#Password Generator
window.geometry("350x250")
window.resizable(False, False)
window.configure(bg="#F6F6F6")

# Define the fonts and colors
title_font = ("Arial", 16, "bold")
label_font = ("Arial", 12)
button_font = ("Arial", 10)
button_bg = "#007AFF"
button_fg = "#FFFFFF"

# Create a BooleanVar to store the value of the "Include special characters" checkbox
include_special = BooleanVar()
include_special.set(True)

# Create a BooleanVar to store the value of the "Lowercase only" checkbox
lowercase_only = BooleanVar()
lowercase_only.set(False)

# Create a label and entry field for the desired password length
length_label = tk.Label(window, text="密碼長度:")#Password length:
length_label.pack()
length_entry = tk.Entry(window)
length_entry.pack()
include_special_checkbox = tk.Checkbutton(window, text="包括特殊字元", variable=include_special)#Include special characters
include_special_checkbox.pack()
# Create a Checkbutton to allow the user to choose whether to restrict the password to lowercase letters only
lowercase_only_checkbox = tk.Checkbutton(window, text="僅限小寫", variable=lowercase_only)#Lowercase only
lowercase_only_checkbox.pack()
# Create a label for the generic name
generic_name_label = tk.Label(window, text="cazzyjason", font=("Arial", 8))
generic_name_label.pack(side="left", padx=(10, 0), pady=(0, 10))


# Create a button to generate and display the password
generate_button = tk.Button(window, text="生成密碼", command=generate_and_display_password)#Generate
generate_button.pack()

# Create a label to display the generated password
password_label = tk.Label(window, text="")
password_label.pack()

# Create a button to copy the generated password
copy_button = tk.Button(window, text="Copy", command=copy_password, state="disabled")
copy_button.pack()

# Create a label for the generated password
password_label = tk.Label(window, font=("Arial", 12))
password_label.pack(side="right", padx=(0, 10), pady=(0, 10))


# Start the main event loop
window.mainloop()
