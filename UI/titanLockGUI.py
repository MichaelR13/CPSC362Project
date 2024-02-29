import tkinter as tk

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
            pady=80,
            padx=60
            )
        
        # Title pack
        text.pack()
        # self.iconphoto(False, tk.PhotoImage(file="bg_Titan_Lock.jpg"))
        
        #frm_buttons.pack()
        txt_edit = tk.Text(self)
        frm_buttons = tk.Frame(self, relief=tk.RAISED, bd=2)
        btn_open = tk.Button(frm_buttons, text="Open")
        btn_save = tk.Button(frm_buttons, text="Save As...")

        btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        btn_save.grid(row=1, column=0, sticky="ew", padx=5)
        #frm_buttons.grid(row=0, column=0, sticky="ns")
        #txt_edit.grid(row=0, column=1, sticky="nsew")
        
if __name__ == "__main__":
    app = Titan_Locker()
    app.mainloop()