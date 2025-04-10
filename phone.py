import phonenumbers
import pandas as pd
import pyperclip
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from phonenumbers import geocoder, carrier, timezone

# Load existing contacts from CSV
def load_contacts():
    try:
        return pd.read_csv("contacts.csv")
    except FileNotFoundError:
        return pd.DataFrame(columns=["Phone Number", "Name"])

# Get phone number details
def get_number_details():
    number = entry.get().strip()

    if not number:
        messagebox.showerror("Error", "Please enter a phone number!")
        return

    try:
        parsed_number = phonenumbers.parse(number)

        if not phonenumbers.is_possible_number(parsed_number):
            messagebox.showerror("Error", "Invalid phone number!")
            return

        # Check in contacts CSV
        contacts = load_contacts()
        name = contacts.loc[contacts["Phone Number"] == number, "Name"].values
        name = name[0] if len(name) > 0 else "Unknown"

        # Get details
        country = geocoder.description_for_number(parsed_number, "en")
        sim_operator = carrier.name_for_number(parsed_number, "en")
        time_zones = timezone.time_zones_for_number(parsed_number)

        # Display results
        result_text = f"""
        ✅ Phone Number: {number}
        📍 Country: {country}
        📡 Carrier: {sim_operator if sim_operator else "Unknown"}
        ⏰ Timezone: {', '.join(time_zones)}
        🏷️ Name: {name}
        """
        result_label.configure(text=result_text, fg="green")

        # Copy to clipboard
        pyperclip.copy(result_text.strip())
        messagebox.showinfo("Copied!", "Result copied to clipboard!")

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong!\n{e}")

# Add new contact
def add_contact():
    number = entry.get().strip()
    name = name_entry.get().strip()

    if not number or not name:
        messagebox.showerror("Error", "Enter both Name and Phone Number!")
        return

    contacts = load_contacts()
    
    if number in contacts["Phone Number"].values:
        messagebox.showinfo("Info", "Contact already exists!")
        return

    # Append new contact
    new_contact = pd.DataFrame({"Phone Number": [number], "Name": [name]})
    contacts = pd.concat([contacts, new_contact], ignore_index=True)
    contacts.to_csv("contacts.csv", index=False)

    messagebox.showinfo("Success", f"{name} added to contacts!")

# Create GUI
ctk.set_appearance_mode("dark")  # Dark Mode
app = ctk.CTk()
app.title("📞 Phone Number Details Finder")
app.geometry("450x500")

# Title Label
ctk.CTkLabel(app, text="Enter Phone Number:", font=("Arial", 14)).pack(pady=10)

# Input Field
entry = ctk.CTkEntry(app, font=("Arial", 14), width=300)
entry.pack(pady=5)

# Search Button
ctk.CTkButton(app, text="🔍 Get Details", font=("Arial", 14), command=get_number_details).pack(pady=10)

# Name Input Field
ctk.CTkLabel(app, text="Enter Name (if adding contact):", font=("Arial", 12)).pack(pady=5)
name_entry = ctk.CTkEntry(app, font=("Arial", 12), width=300)
name_entry.pack(pady=5)

# Add Contact Button
ctk.CTkButton(app, text="➕ Add Contact", font=("Arial", 12), command=add_contact, fg_color="green").pack(pady=10)

# Result Label
result_label = ctk.CTkLabel(app, text="", font=("Arial", 12), wraplength=400)
result_label.pack(pady=10)

# Run the App
app.mainloop()
