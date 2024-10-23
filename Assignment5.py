"""Now Write a similar Python Code so that you can create a Combo Box/Drop down where you can show the items as-

Sunday
Monday
Tuesday
Wednesday
THursday
Friday
Saturday"""

import tkinter as tk
from tkinter import ttk

def show_selection(event):
    selected_item = combo.get()  # Get the selected item from the combobox
    label.config(text=f"Selected: {selected_item}")

# Create the main window
root = tk.Tk()
root.title("Combo List Example")

# Create a list of items
items = ['Sunday' ,
          'Monday' ,
          'Tuesday' ,
          'Wednesday' ,
          'THursday' ,
          'Friday' ,
          'Saturday']

# Create a Combobox
combo = ttk.Combobox(root, values=items)
combo.pack(pady=10)

# Set default value
combo.set('Select an item')

# Bind the selection event
combo.bind("<<ComboboxSelected>>", show_selection)

# Create a label to show the selected item
label = tk.Label(root, text="Selected: ")
label.pack(pady=10)

# Run the main loop
root.mainloop()