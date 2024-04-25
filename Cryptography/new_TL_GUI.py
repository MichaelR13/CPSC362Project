import tkinter as tk
from tkinter import ttk
from encryption import *
from decryption import *
from fileCheck import fileExist
from tkinter import messagebox 
  
#GLOBAL CSUF COLORS
t_blue = '#00244E'
t_orange = '#FF7900'
masterKey = ''
class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp 
    def __init__(self, *args, **kwargs): 
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Titan Lock")
        self.geometry('400x400+500+500')
        self.minsize(500,420)
        self.resizable(True, True)
        
        
        
       
        # creating a container
        container = tk.Frame(self)
        
        container.pack(side = "top", fill = "both", expand = True) 
        container.configure(bg=t_blue)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        
       
        # initializing frames to an empty array
        self.frames = {}  
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, AddPage, SavedPage):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with 
            # for loop
            self.frames[F] = frame 
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        if cont == StartPage:
            frame.keyEntry.delete(0, tk.END)
            
        elif cont == AddPage:
            frame.userEntry.delete(0, 'end')
            frame.pwEntry.delete(0, 'end')
            frame.linkEntry.delete(0, 'end')
  
# first window frame startpage
  
class StartPage(tk.Frame):
    def saveSaveKey(self, keyEntry, controller):
        global masterKey
        masterKey = keyEntry
        messageBox.messageboxEnterkey(keyEntry, controller, SavedPage)
        # self.keyEntry.delete(0, tk.END)

    def saveAddKey(keyEntry, controller):
        global masterKey
        masterKey = keyEntry
        messageBox.messageboxEnterkey(keyEntry, controller, AddPage)
        # MasterKey Check
        #print (masterKey)
        # controller.show_frame(AddPage)
        # keyEntry.delete(0, tk.END)
      
    
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        self.configure(bg = t_blue)
        # label of frame Layout 2
        label = ttk.Label(self, text='Titan Lock 🐘', font='Arial 36', foreground = t_orange, background = t_blue)
         
        # putting the grid in its place by using
        # grid
        label.grid(row = 0, column = 4, padx = 10, pady = 10) 
  
        style = ttk.Style()
        #style.theme_use('alt')
        style.configure('TButton', foreground = 'black', width = 15)
        style.map('TButton', background=[('active', 'white')])
        addButton = ttk.Button(self, text ="ADD", command = lambda : StartPage.saveAddKey(self.keyEntry.get(), controller))
        
        # putting the button in its place by
        # using grid
        addButton.grid(row = 1, column = 4, padx = 10, pady = 10)
        ## button to show frame 2 with text layout2
        savedButton = ttk.Button(self, text ="Saved", command = lambda : StartPage.saveSaveKey(self, self.keyEntry.get(), controller))

        # putting the button in its place by
        # using grid
        
        savedButton.grid(row = 2, column = 4, padx = 10, pady = 10)
        key = tk.Label(self, text="Enter Key: ", bg= t_blue, fg='white')
        key.grid(row = 3, column = 4)
        self.keyEntry = tk.Entry(self, width ='25')
        self.keyEntry.grid(row = 4, column = 4)
        #keyEntry.delete(0, tk.END)
        #keyEntry.delete(len(keyEntry))

        
  
          
# second window frame ADD BUTTON AND ENTRY PAGE
class AddPage(tk.Frame):
    def save_file(userText, userPW, link):
        messageBox.messageboxSaved(userText, userPW, link)

            
    
    def __init__(self, parent, controller):
       
        
        tk.Frame.__init__(self, parent)
        self.configure(bg = t_blue)
        label = ttk.Label(self, text='Titan Lock 🐘', font='Arial 36', foreground = t_orange, background = t_blue)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
        # button to show frame 2 with text
        # layout2
        backButton  = ttk.Button(self, text ="Back",
                            command = lambda : controller.show_frame(StartPage))
        backButton.grid(row = 1, column = 1)

        #ALL ENTRIES AND SUBMIT BUTTON FOR ADD PAGE
        
        # Set the position of USER,PW, LINK AND THEIR RESPECTIVE ENTRIES
        user = tk.Label(self, text="User: ", bg= t_blue, fg='white')
        self.userEntry = tk.Entry(self, width ='25')
        pw = tk.Label(self, text="Password: ", bg= t_blue, fg='white')
        self.pwEntry = tk.Entry(self, width ='25', show = '*')
        link = tk.Label(self, text="Link: ", bg= t_blue, fg='white')
        self.linkEntry = tk.Entry(self, width ='25')
        
        #TODO: add command to submit button
        submitButton = ttk.Button(self, text = 'SUBMIT', command = lambda: AddPage.save_file(self.userEntry.get(), self.pwEntry.get(),self.linkEntry.get()))
        user.grid(row = 2, column = 4)
        self.userEntry.grid(row = 3, column = 4)
        pw.grid(row = 4, column = 4)
        self.pwEntry.grid(row = 5, column = 4)
        link.grid(row = 6, column = 4)
        self.linkEntry.grid(row = 7, column = 4)
        
        submitButton.grid(row= 8, column = 4, pady = 30)
        
        
                    
        
# third window frame SAVED DATA PAGE
class SavedPage(tk.Frame): 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = t_blue)
        label = ttk.Label(self, text='Titan Lock 🐘', font='Arial 36', foreground = t_orange, background = t_blue)
        
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
        # button to show frame 2 with text
        # layout2
        def remove_label():
            for  label in dataLabelList:
                label.destroy()

        def backButtonReset(controller):
            remove_label()
            controller.show_frame(StartPage)

        backButton = ttk.Button(self, text ="Back",
                            command = lambda : backButtonReset(controller))
     
        # putting the button in its place 
        # by using grid
        backButton.grid(row = 1, column = 1, padx = 10, pady = 10)
        dataLabelList = []
        def showUserData():
            
            resultList = decrypt(masterKey)
            for  row, item in enumerate(resultList):
                line = ' '.join(map(str, item))
                dataLabel = ttk.Label(self, text = line)
                dataLabel.grid(row = (row + 5) , column=(4), pady = 10)
                dataLabelList.append(dataLabel)
        
        showButton = ttk.Button(self, text ="Show user Data",
                            command = lambda : showUserData())
        showButton.grid(row = 4, column = 4)
        
#class for messageboxes
class messageBox():
    def messageboxSaved(userText, userPW, link):
        if not all((userText, userPW, link)):
            messagebox.showerror("Error", "Please fill in all fields")
            return
        encrypt(masterKey, userText, userPW, link)
        messagebox.showinfo("Submission", "Information has been submitted!")
        
    def messageboxEnterkey(keyEntry, controller, page):
        if not (keyEntry):
            messagebox.showerror("Error", "Please fill in all fields.")
        elif len(keyEntry) < 16 or len(keyEntry) > 16:
            messagebox.showerror("Error", "The key must be 16 characters.")
        elif fileExist(keyEntry):
            messagebox.showerror("Error", "Incorrect key.")
        else:
            controller.show_frame(page)



  
  
# Driver Code
app = tkinterApp()
app.mainloop()