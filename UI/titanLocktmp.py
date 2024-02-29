import tkinter as tk
from tkinter import messagebox
from tkinter import *
#import titanLocktmpdatabase

# Reference: https://realpython.com/python-gui-tkinter/#displaying-clickable-buttons-with-button-widgets

root = tk.Tk()
w = root.winfo_height
root.geometry("400x400+500+400")

root.title("TitanLock Password Manager")
root.resizable(width=True, height=True)

lab1 = tk.Label(root, text="Super Fun\nBest Password\n Manager Ever!", font="Arial 20", bg="black", fg= "white")
#lab1.pack()

#button = tk.Button(text="Click if you're dumb!", width=25, height=5, bg="blue", fg="yellow")
#button.pack()

# junk
from tkinter.filedialog import askopenfilename, asksaveasfilename
root.rowconfigure(0, minsize=800, weight=1)
root.columnconfigure(1, minsize=800, weight=1)

# Make the buttons actually open a file 

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    root.title(f"Simple Text Editor - {filepath}")

# Make the buttons save the file 
    # ...

def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    root.title(f"Simple Text Editor - {filepath}")



    

# Code to create open and save buttons
txt_edit = tk.Text(root)
frm_buttons = tk.Frame(root, relief=tk.RAISED, bd=2)
btn_open = tk.Button(frm_buttons, text="Open", command=open_file)
btn_save = tk.Button(frm_buttons, text="Save As...", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")




    
# end junk

root.mainloop()