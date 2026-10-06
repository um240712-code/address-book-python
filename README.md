Address Book (Python CLI)
A simple interactive command-line address book written in Python. It lets you add, search,
delete, and list contacts from a looping main menu.
Features
Add a new contact (name, type, phone number)
Prevent duplicate phone numbers
Search contacts by name (partial match) or by number
Delete a contact by name or by number
Show all saved contacts
Input validation for menu choices
Requirements
Python 3.8 or newer
No external libraries
How to Run
1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Run:
python address_book.py
Rename the file to address_book.py if your file has a different name.
Menu
1. Add new contact
2. Search by name
3. Search by number
4. Delete contact by name
5. Delete contact by number
6. Show all contacts
7. Exit
Example
Please enter your choice: 1
Enter name: ahmad
Enter type: friend
Enter number: 0791111111
Contact added.
Adding the same number again prints:
Number already exists, process.
How It Works
Contacts are stored in memory as a list of lists: [name, type, number] .
The main menu runs inside a while True loop until the user chooses Exit.
Search loops over the list and compares the name or number.
Delete finds the matching index and removes it with pop() .
Skills Demonstrated
Python lists and nested lists
Loops and conditional logic
User input handling
Basic CRUD operations (Create, Read, Delete)
Limitations and Future Improvements
Data is lost when the program closes. Next step: save contacts to a file (JSON or CSV).
Add an update/edit option.
Validate phone number format.
Rewrite using functions or a Contact class (OOP).
Author
University project, Data Science and AI.
