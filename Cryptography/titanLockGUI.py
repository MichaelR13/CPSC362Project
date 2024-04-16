import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from encryption import encrypt


def addWindow():
        #global win
        win = tk.Tk()
        # GUI Dimensions
        win.title("Titan Lock 🐘")
        win.geometry("400x400+500+400")
        win.minsize(500,420)
        win.resizable(True, True)
        
        # GUI Layout CSUF colors
        t_blue = '#00244E'
        t_orange = '#FF7900'
        
        # GUI Label
        win.configure(bg=t_blue) 
        text2 = tk.Label(
            win, 
            text='Titan Lock 🐘', 
            font='Arial 36', 
            bg=t_orange, 
            fg=t_blue, 
            pady=10,
            padx=60
            )
        
        def save_file():
            """Save the current file as a new file."""
            '''filepath = asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
            '''
            
            #if not filepath:
            #    return
            
            #with open(filepath, mode="w", encoding="utf-8") as output_file:
            userText = userEntry.get() #txt_edit.get("1.0", tk.END)
            userPW = pwEntry.get() #currently spaces are allowed
            link = linkEntry.get()
            #output_file.write(userText  +' '+ userPW  +' '+ link)
            key = ""
            encrypt(key, userText, userPW, link)
                
            win.title(f"Simple Text Editor")
        
        # Title pack
        text2.pack()
        # Create a Button
        btn = Button(win, text = 'SUBMIT',font= 'Arial 12',  width= '10', height= '1', bd = '5',  command = save_file) 
        user = tk.Label(win, text="User: ", bg= t_blue, fg='white')
        userEntry = Entry(win, width ='25')
        pw = tk.Label(win, text="Password: ", bg= t_blue, fg='white')
        pwEntry = Entry(win, width ='25')
        link = tk.Label(win, text="Link: ", bg= t_blue, fg='white')
        linkEntry = Entry(win, width ='25')
        
        
        # Set the position of button 
        user.pack(pady=(30,5), padx = (0,160))
        userEntry.pack()
        
        pw.pack(pady=(30,5), padx = (0,133))
        # Show asterisks (*) for password entry
        pwEntry = Entry(win, width ='25', show='*') 
        pwEntry.pack()
        
        link.pack(pady=(30,5), padx=(0,165))
        linkEntry.pack()

        btn.pack(pady=(40,10))



#BEGIN MAIN:    
app = tk.Tk()
app.title("Main Screen")
app.geometry('400x400+500+400')
app.minsize(500,420)
app.resizable(True, True)
t_blue = '#00244E'
t_orange = '#FF7900'
app.configure(bg = t_blue)
text = tk.Label(app, text='Titan Lock 🐘', font='Arial 36', bg=t_orange, fg=t_blue, pady=10, padx=60)
text.pack()

enterLabel = Label(app, text = 'Enter Master Password:', bg= t_blue, fg='white')
enterEntry = Entry(app, width ='25')
enterLabel.pack(padx = (0, 30))
enterEntry.pack()
addBtn = Button(app, text = 'ADD',font= 'Arial 12',  width= '10', height= '1', bd = '5', command = addWindow)
addBtn.pack(pady=(40,10))

userDataBtn = Button(app, text = 'Saved Passwords')
userDataBtn.pack(pady = (20, 5))


app.mainloop()