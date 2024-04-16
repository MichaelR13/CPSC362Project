import tkinter as tk
from tkinter import ttk

  
 

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
        button1 = ttk.Button(self, text ="ADD",
                            command = lambda : controller.show_frame(AddPage))
        
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text ="Saved",
                            command = lambda : controller.show_frame(SavedPage))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
  
          
# second window frame page1 
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
        # putting the button in its place 
        # by using grid
        backButton.grid(row = 1, column = 1)
        btn = tk.Button(self, text = 'SUBMIT',font= 'Arial 12',  width= '10', height= '1', bd = '5') 
        user = tk.Label(self, text="User: ", bg= t_blue, fg='white')
        userEntry = tk.Entry(self, width ='25')
        pw = tk.Label(self, text="Password: ", bg= t_blue, fg='white')
        pwEntry = tk.Entry(self, width ='25')
        link = tk.Label(self, text="Link: ", bg= t_blue, fg='white')
        linkEntry = tk.Entry(self, width ='25')
        
        
        # Set the position of button 
        user.grid(row = 2, column = 4)
        userEntry.grid(row = 3, column = 4)
        
        

  
  
# third window frame page2
class SavedPage(tk.Frame): 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = t_blue)
        label = ttk.Label(self, text='Titan Lock 🐘', font='Arial 36', foreground = t_orange, background = t_blue)
        
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Back",
                            command = lambda : controller.show_frame(StartPage))
     
        # putting the button in its place 
        # by using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
  
# Driver Code
app = tkinterApp()
app.mainloop()