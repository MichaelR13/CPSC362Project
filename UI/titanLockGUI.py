import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

class Titan_Locker(tk.Tk):

    def userInputTxtFile():
        var1 = 2 #Function should allow user input to do something
        

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
        #padx was 80
        def save_file():
            """Save the current file as a new file."""
            filepath = asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
            )
            if not filepath:
                return
            with open(filepath, mode="w", encoding="utf-8") as output_file:
                userText = userEntry.get()#txt_edit.get("1.0", tk.END)
                userPW = pwEntry.get() #currently spaces are allowed
                link = linkEntry.get()
                output_file.write(userText  +' '+ userPW  +' '+ link)
            self.title(f"Simple Text Editor - {filepath}")
        
        # Title pack
        text.pack()

        # Create a Button
        btn = Button(self, text = 'SUBMIT',font= 'Arial 12',  width= '10', height= '1', bd = '5',  command = save_file) 
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
    #create a command for the submit button to take the user entry 
    def userInput(): # Should take the input from the entry then send it to a file via thesubmitbutto
        var2 =5

    

 
        
if __name__ == "__main__":
    app = Titan_Locker()
    app.mainloop()