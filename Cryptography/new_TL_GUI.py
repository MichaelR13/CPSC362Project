import tkinter as tk
from tkinter import ttk
from encryption import encrypt

  
#GLOBAL CSUF COLORS
t_blue = '#00244E'
t_orange = '#FF7900'
  
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
  
# first window frame startpage
  
class StartPage(tk.Frame):
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
        addButton = ttk.Button(self, text ="ADD",
                            command = lambda : controller.show_frame(AddPage))
        
        # putting the button in its place by
        # using grid
        addButton.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        ## button to show frame 2 with text layout2
        savedButton = ttk.Button(self, text ="Saved",
                            command = lambda : controller.show_frame(SavedPage))
     
        # putting the button in its place by
        # using grid
        savedButton.grid(row = 2, column = 1, padx = 10, pady = 10)
  
          
# second window frame ADD BUTTON AND ENTRY PAGE
class AddPage(tk.Frame):
     
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
        
        user = tk.Label(self, text="User: ", bg= t_blue, fg='white')
        userEntry = tk.Entry(self, width ='25')
        pw = tk.Label(self, text="Password: ", bg= t_blue, fg='white')
        pwEntry = tk.Entry(self, width ='25', show = '*')
        link = tk.Label(self, text="Link: ", bg= t_blue, fg='white')
        linkEntry = tk.Entry(self, width ='25')
        #TODO: add command to submit button
        submitButton = ttk.Button(self, text = 'SUBMIT')
        # Set the position of USER,PW, LINK AND THEIR RESPECTIVE ENTRIES
        user.grid(row = 2, column = 4)
        userEntry.grid(row = 3, column = 4)
        pw.grid(row = 4, column = 4)
        pwEntry.grid(row = 5, column = 4)
        link.grid(row = 6, column = 4)
        linkEntry.grid(row = 7, column = 4)
        
        submitButton.grid(row= 8, column = 4, pady = 30)
        '''def save(self ):
            messagebox.showinfo(title = 'Password saved!', message = 'Your password has been saved!')
            button = tkinter.button(window, command = save, text = 'Submit')
            window = Tk()
            button.pack()
            window.mainloop()
            frame.pack(self)'''
        
                    
                
        
# third window frame SAVED DATA PAGE
class SavedPage(tk.Frame): 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = t_blue)
        label = ttk.Label(self, text='Titan Lock 🐘', font='Arial 36', foreground = t_orange, background = t_blue)
        
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
        # button to show frame 2 with text
        # layout2
        backButton = ttk.Button(self, text ="Back",
                            command = lambda : controller.show_frame(StartPage))
     
        # putting the button in its place 
        # by using grid
        backButton.grid(row = 1, column = 1, padx = 10, pady = 10)
  
  
# Driver Code
app = tkinterApp()
app.mainloop()