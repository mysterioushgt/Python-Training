import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title("Example of treeview")
root.geometry("400x200")

tree =ttk.Treeview(root)
tree.pack()

master_item=tree.insert("","end","master_item", text="Master Item")

#Add items enter master_item
item1=tree.insert(master_item ,"end" ,"item1" ,text="Item 1")
item2=tree.insert(master_item ,"end" ,"item2" ,text="Item 2")
item3=tree.insert(master_item ,"end" ,"item3" ,text="Item 3")

#Add subitems for item1
tree.insert(item1 ,"end" ,"subtem1_1" ,text="Subitem 1.1")
tree.insert(item1 ,"end" ,"subtem1_2" ,text="Subitem 1.2")

#Add subitems for item2
tree.insert(item2 ,"end" ,"subtem2_1" ,text="Subitem 2.1")
tree.insert(item2 ,"end" ,"subtem2_2" ,text="Subitem 2.2")

#Add subitems for item3
tree.insert(item3 ,"end" ,"subtem3_1" ,text="Subitem 3.1")
tree.insert(item3 ,"end" ,"subtem3_2" ,text="Subitem 3.2")

root.mainloop()