# Phone-Number-Details-Finder
This application allows you to retrieve detailed information about phone numbers, including country, carrier, timezone, and any existing contact name associated with the phone number. You can also add new contacts to the app's contact list, which is stored in a CSV file.

Features
Retrieve Phone Number Details: Enter a phone number and get information such as:

Country

Carrier

Timezone

Contact name (from the existing contacts list)

Add New Contacts: Add a new contact by providing a phone number and a name. The contacts are stored in a CSV file for persistent data.

Copy Results to Clipboard: Automatically copies the phone number details to your clipboard after retrieval.

User-Friendly GUI: The application features an easy-to-use GUI with dark mode for better readability.

Requirements
Python 3.x

Required Libraries:

phonenumbers: For parsing and validating phone numbers.

pandas: For managing and storing contacts in CSV format.

pyperclip: For copying results to the clipboard.

tkinter and customtkinter: For creating the graphical user interface (GUI).

Installation
Install Python 3.x: Make sure you have Python 3.x installed. You can download it from python.org.

Install Required Libraries: Use pip to install the required libraries.

bash
Copy
Edit
pip install phonenumbers pandas pyperclip customtkinter
Run the Application: Download or clone the repository, and run the script.

bash
Copy
Edit
python phone_number_details_finder.py
How to Use
Get Phone Number Details:

Enter a phone number in the "Enter Phone Number" field and click the "🔍 Get Details" button.

The details, including country, carrier, timezone, and contact name, will appear below the button.

The details will also be copied to your clipboard for easy sharing.

Add a New Contact:

Enter the phone number and the contact name in the respective fields.

Click the "➕ Add Contact" button to save the contact to the CSV file.

If the contact already exists, a message will inform you that the contact is already in the list.

CSV File:

The contacts are stored in a CSV file named contacts.csv. You can view or edit the contacts directly in the CSV file if needed.

Files
contacts.csv: The file where all the phone numbers and associated names are stored.

phone_number_details_finder.py: The Python script containing the application logic and GUI.

License
This project is open source and available under the MIT License
