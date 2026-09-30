import tkinter as tk
from tkinter import messagebox
import secrets
import string


def check_password():
    password = password_entry.get()

    if password == "":
        messagebox.showwarning("Warning", "Please enter a password.")
        return

    score = 0
    suggestions = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    # Check uppercase
    if any(char.isupper() for char in password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    # Check lowercase
    if any(char.islower() for char in password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    # Check numbers
    if any(char.isdigit() for char in password):
        score += 1
    else:
        suggestions.append("Add numbers.")

    # Check special characters
    if any(char in string.punctuation for char in password):
        score += 1
    else:
        suggestions.append("Add special characters.")

    # Display result
    if score <= 2:
        strength = "WEAK"
    elif score == 3:
        strength = "MEDIUM"
    elif score == 4:
        strength = "STRONG"
    else:
        strength = "VERY STRONG"

    result_label.config(
        text=f"Password Strength: {strength}"
    )

    if suggestions:
        suggestion_label.config(
            text="Suggestions:\n" + "\n".join(suggestions)
        )
    else:
        suggestion_label.config(
            text="Excellent! Your password satisfies all basic requirements."
        )


def generate_password():
    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = ''.join(
        secrets.choice(characters)
        for _ in range(16)
    )

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

    result_label.config(
        text="Generated a 16-character password"
    )

    suggestion_label.config(
        text="Use this password only for a legitimate account."
    )


def clear_fields():
    password_entry.delete(0, tk.END)
    result_label.config(text="")
    suggestion_label.config(text="")


# Main window
root = tk.Tk()
root.title("CNS Password Security Tool")
root.geometry("600x450")
root.resizable(False, False)

# Title
title_label = tk.Label(
    root,
    text="PASSWORD SECURITY TOOL",
    font=("Arial", 22, "bold")
)
title_label.pack(pady=20)

# Description
description = tk.Label(
    root,
    text="Check password strength and generate secure passwords",
    font=("Arial", 11)
)
description.pack(pady=5)

# Password label
password_label = tk.Label(
    root,
    text="Enter Password:",
    font=("Arial", 12)
)
password_label.pack(pady=10)

# Password entry
password_entry = tk.Entry(
    root,
    width=40,
    show="*",
    font=("Arial", 12)
)
password_entry.pack()

# Buttons
check_button = tk.Button(
    root,
    text="Check Password Strength",
    command=check_password,
    width=25
)
check_button.pack(pady=15)

generate_button = tk.Button(
    root,
    text="Generate Secure Password",
    command=generate_password,
    width=25
)
generate_button.pack(pady=5)

clear_button = tk.Button(
    root,
    text="Clear",
    command=clear_fields,
    width=25
)
clear_button.pack(pady=5)

# Result
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 15, "bold")
)
result_label.pack(pady=20)

# Suggestions
suggestion_label = tk.Label(
    root,
    text="",
    font=("Arial", 11),
    justify="left"
)
suggestion_label.pack()

root.mainloop()