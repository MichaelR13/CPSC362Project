import tkinter as tk
from tkinter import *

class Titan_Locker(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # GUI Dimensions
        self.title("Titan Lock")
        self.geometry("400x400+500+400")
        self.resizable(True, True)
        
        # GUI Layout
        # CSUF colors
        t_blue = '#00244E'
        t_orange = '#FF7900'
        
        # GUI Label
        self.configure(bg=t_blue) 
        text = tk.Label(
            self, 
            text='Titan Lock', 
            font='Arial 36', 
            bg=t_orange, 
            fg=t_blue, 
            pady=10,
            padx=60
            )
        
        # Title pack
        text.pack()
        # Create a Button
        btn = Button(self, text = 'SUBMIT',font= 'Arial 12',  width= '10', height= '1', bd = '5',  command = self.destroy) 
        user = tk.Label(self, text="User: ", bg= t_blue, fg='white')
        userEntry = Entry(width ='25')
        pw = tk.Label(self, text="Password: ", bg= t_blue, fg='white')
        pwEntry = Entry(width ='25')
        link = tk.Label(self, text="Link: ", bg= t_blue, fg='white')
        linkEntry = Entry(width ='25')
        # Set the position of button 
        user.pack(pady=(30,5), padx = (0,117))
        userEntry.pack()
        pw.pack(pady=(30,5), padx = (0,91))
        pwEntry.pack()
        link.pack(pady=(30,5), padx=(0,119))
        linkEntry.pack()

        btn.pack(pady=(40,10))

        
        #pswrd = tk.Label(self, text="Password:", width= '8', height ='1' )
        
        
        
if __name__ == "__main__":
    app = Titan_Locker()
    app.mainloop()