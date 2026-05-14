import re
import random
import string
from tkinter import *
from tkinter import messagebox

# -----------------------------
# PASSWORD STRENGTH ANALYZER
# -----------------------------
# Because people still use "123456" in 2026.
# Humanity is truly committed to speedrunning cyber attacks.

common_passwords = [
    "123456",
    "password",
    "password123",
    "qwerty",
    "admin",
    "welcome",
    "abc123",
    "letmein",
    "iloveyou"
]


def analyze_password(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 20
    else:
        feedback.append("Use at least 8 characters")

    if len(password) >= 12:
        score += 10

    # Uppercase Check
    if re.search(r"[A-Z]", password):
        score += 15
    else:
        feedback.append("Add uppercase letters")

    # Lowercase Check
    if re.search(r"[a-z]", password):
        score += 15
    else:
        feedback.append("Add lowercase letters")

    # Number Check
    if re.search(r"[0-9]", password):
        score += 15
    else:
        feedback.append("Add numbers")

    # Special Character Check
    if re.search(r"[^A-Za-z0-9]", password):
        score += 15
    else:
        feedback.append("Add special characters")

    # Common Password Check
    if password.lower() not in common_passwords:
        score += 10
    else:
        feedback.append("This password is too common")

    # Repeated Character Check
    if re.search(r"(.)\\1{2,}", password):
        score -= 10
        feedback.append("Avoid repeated characters")

    score = max(0, min(score, 100))

    return score, feedback


def get_strength_label(score):
    if score < 30:
        return "Weak"
    elif score < 60:
        return "Moderate"
    elif score < 80:
        return "Strong"
    else:
        return "Very Strong"


def check_password():
    password = password_entry.get()

    if not password:
        messagebox.showwarning("Warning", "Please enter a password")
        return

    score, feedback = analyze_password(password)
    strength = get_strength_label(score)

    result_text.set(f"Strength: {strength}\nScore: {score}/100")

    if feedback:
        suggestions.set("\n".join(feedback))
    else:
        suggestions.set("Excellent password. Cybercriminals are crying.")



def generate_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*()_+"

    generated = ''.join(random.choice(characters) for _ in range(16))

    password_entry.delete(0, END)
    password_entry.insert(0, generated)


# -----------------------------
# GUI WINDOW
# -----------------------------

root = Tk()
root.title("Password Strength Analyzer")
root.geometry("600x500")
root.configure(bg="#f4f6f9")

# Title
Label(
    root,
    text="Password Strength Analyzer",
    font=("Arial", 22, "bold"),
    bg="#f4f6f9",
    fg="#1e293b"
).pack(pady=20)

# Subtitle
Label(
    root,
    text="Evaluate password security using cybersecurity concepts",
    font=("Arial", 12),
    bg="#f4f6f9",
    fg="#475569"
).pack()

# Password Entry
Label(
    root,
    text="Enter Password",
    font=("Arial", 14, "bold"),
    bg="#f4f6f9"
).pack(pady=15)

password_entry = Entry(root, width=35, font=("Arial", 16), show="*")
password_entry.pack(pady=10)

# Buttons
button_frame = Frame(root, bg="#f4f6f9")
button_frame.pack(pady=15)

Button(
    button_frame,
    text="Check Strength",
    font=("Arial", 12, "bold"),
    bg="#2563eb",
    fg="white",
    padx=15,
    pady=8,
    command=check_password
).grid(row=0, column=0, padx=10)

Button(
    button_frame,
    text="Generate Strong Password",
    font=("Arial", 12, "bold"),
    bg="#16a34a",
    fg="white",
    padx=15,
    pady=8,
    command=generate_password
).grid(row=0, column=1, padx=10)

# Result Variables
result_text = StringVar()
suggestions = StringVar()

# Result Display
Label(
    root,
    textvariable=result_text,
    font=("Arial", 16, "bold"),
    bg="#f4f6f9",
    fg="#0f172a"
).pack(pady=20)

# Suggestions Box
Label(
    root,
    text="Suggestions",
    font=("Arial", 14, "bold"),
    bg="#f4f6f9"
).pack()

Label(
    root,
    textvariable=suggestions,
    font=("Arial", 12),
    bg="#ffffff",
    fg="#334155",
    width=50,
    height=8,
    wraplength=450,
    justify=LEFT,
    relief=SOLID,
    padx=10,
    pady=10
).pack(pady=10)

# Footer
Label(
    root,
    text="Concepts Used: Regex | Password Entropy | Secure Generation | Validation",
    font=("Arial", 10),
    bg="#f4f6f9",
    fg="#64748b"
).pack(side=BOTTOM, pady=20)

root.mainloop()