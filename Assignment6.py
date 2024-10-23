#ADMISSION FORM:
import tkinter as tk
from tkinter import ttk

# Function to get data from the form
def submit_form():
    full_name = entry_name.get()
    address = entry_address.get()  # For multi-line text
    course = combo_course.get()
    contact_no = entry_contact.get()

    print(f"Full Name: {full_name}")
    print(f"Address: {address}")
    print(f"Course: {course}")
    print(f"Contact No: {contact_no}")

# Function to reset the form
def reset_form():
    entry_name.delete(0, 'end')  # Clears the full name
    entry_address.delete("1.0", "end")  # Clears the address
    combo_course.current(0)  # Resets the course to the first option
    entry_contact.delete(0, 'end')  # Clears the contact number

# Create the main window
root = tk.Tk()
root.title("Student Information Form")
root.geometry("400x450")

# ITM University Gwalior Title
label_title = tk.Label(root, text="ITM University Gwalior", font=("Arial", 16, "bold"), fg="blue")
label_title.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Full Name
label_name = tk.Label(root, text="Full Name:")
label_name.grid(row=1, column=0, padx=10, pady=5)
entry_name = tk.Entry(root, width=30)
entry_name.grid(row=1, column=1, padx=10, pady=5)

# Address
label_address = tk.Label(root, text="Address:")
label_address.grid(row=2, column=0, padx=10, pady=5)
entry_address = tk.Text(root, width=30, height=4)  # Multi-line text for address
entry_address.grid(row=2, column=1, padx=10, pady=5)

# Course (with ComboBox)
label_course = tk.Label(root, text="Course:")
label_course.grid(row=3, column=0, padx=10, pady=5)

# Creating ComboBox for Course selection
course_options = ["Computer Science", "Electrical Engineering", "Mechanical Engineering", "Civil Engineering", "Business Administration"]
combo_course = ttk.Combobox(root, values=course_options, width=28)
combo_course.grid(row=3, column=1, padx=10, pady=5)
combo_course.current(0)  # Set default value to the first option

# Set background color of the course combo box to blue
combo_course.configure(background="blue", foreground="white")

# Contact No
label_contact = tk.Label(root, text="Contact No:")
label_contact.grid(row=4, column=0, padx=10, pady=5)
entry_contact = tk.Entry(root, width=30)
entry_contact.grid(row=4, column=1, padx=10, pady=5)

# Add Button
add_button = tk.Button(root, text="Add", command=submit_form)
add_button.grid(row=5, column=0, padx=10, pady=20)

# Reset Button
reset_button = tk.Button(root, text="Reset", command=reset_form)
reset_button.grid(row=5, column=1, padx=10, pady=20)

# Start the Tkinter event loop
root.mainloop()