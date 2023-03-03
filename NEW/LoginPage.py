import tkinter as tk  # python 3
from tkinter import ttk, PhotoImage

import proj_support
from proj_support import _style_code


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        controller.configure(highlightcolor="black")

        controller.geometry("600x450+945+434")
        controller.minsize(1, 1)
        controller.maxsize(1905, 1050)
        controller.resizable(1, 1)
        self.configure(background="#f6f7f9")

        self.Label_login_title = tk.Label(self)
        self.Label_login_title.place(relx=0.417, rely=0.111, height=41
                                     , width=319)
        self.Label_login_title.configure(activebackground="#ffffff")
        self.Label_login_title.configure(anchor='w')
        self.Label_login_title.configure(background="#f6f7f9")
        self.Label_login_title.configure(compound='center')
        self.Label_login_title.configure(disabledforeground="#b9b9bb")
        self.Label_login_title.configure(font="-family {DejaVu Sans} -size 24")
        self.Label_login_title.configure(foreground="#778899")
        self.Label_login_title.configure(highlightbackground="#f6f7f9")
        self.Label_login_title.configure(text='''Login''')

        self.Label_ID = tk.Label(self)
        self.Label_ID.place(relx=0.117, rely=0.244, height=41, width=169)
        self.Label_ID.configure(activebackground="#ffffff")
        self.Label_ID.configure(anchor='w')
        self.Label_ID.configure(background="#f6f7f9")
        self.Label_ID.configure(compound='center')
        self.Label_ID.configure(disabledforeground="#b9b9bb")
        self.Label_ID.configure(font="-family {DejaVu Sans} -size 12")
        self.Label_ID.configure(foreground="#778899")
        self.Label_ID.configure(highlightbackground="#f6f7f9")
        self.Label_ID.configure(text='''ID''')

        self.Label_Password = tk.Label(self)
        self.Label_Password.place(relx=0.117, rely=0.356, height=41, width=169)
        self.Label_Password.configure(activebackground="#ffffff")
        self.Label_Password.configure(anchor='w')
        self.Label_Password.configure(background="#f6f7f9")
        self.Label_Password.configure(compound='center')
        self.Label_Password.configure(disabledforeground="#b9b9bb")
        self.Label_Password.configure(font="-family {DejaVu Sans} -size 12")
        self.Label_Password.configure(foreground="#778899")
        self.Label_Password.configure(highlightbackground="#f6f7f9")
        self.Label_Password.configure(text='''Password''')
        _style_code()

        self.TEntry_login_ID = ttk.Entry(self)
        self.TEntry_login_ID.place(relx=0.467, rely=0.267, relheight=0.069
                                   , relwidth=0.423)
        self.TEntry_login_ID.configure(takefocus="")
        self.TEntry_login_ID.configure(cursor="xterm")
        self.TEntry_login_ID.configure(foreground="black")

        self.TEntry_login_Password = ttk.Entry(self)
        self.TEntry_login_Password.place(relx=0.467, rely=0.378, relheight=0.069
                                         , relwidth=0.423)
        self.TEntry_login_Password.configure(takefocus="")
        self.TEntry_login_Password.configure(cursor="xterm")
        self.TEntry_login_Password.configure(foreground="black")
        self.TEntry_login_Password.configure(show="*")

        self.Button_login_gabai = tk.Button(self)
        self.Button_login_gabai.place(relx=0.583, rely=0.556, height=43
                                      , width=113)
        self.Button_login_gabai.configure(activebackground="#5faeb6")
        self.Button_login_gabai.configure(background="#778899")
        self.Button_login_gabai.configure(borderwidth="2")
        self.Button_login_gabai.configure(
            command=lambda: proj_support.login_gabai(controller, self.TEntry_login_ID.get(),
                                                     self.TEntry_login_Password.get()))
        self.Button_login_gabai.configure(compound='left')
        self.Button_login_gabai.configure(disabledforeground="#b9b9bb")
        self.Button_login_gabai.configure(foreground="#f6f7f9")
        self.Button_login_gabai.configure(highlightbackground="#778899")
        self.Button_login_gabai.configure(relief="flat")
        self.Button_login_gabai.configure(text='''Login as gabai''')
        self.menubar = tk.Menu(controller, font="TkMenuFont", bg='#d9d9d9', fg='#000000')
        controller.configure(menu=self.menubar)

        self.Button_login_guest = tk.Button(self)
        self.Button_login_guest.place(relx=0.25, rely=0.556, height=43
                                      , width=113)
        self.Button_login_guest.configure(activebackground="#5faeb6")
        self.Button_login_guest.configure(background="#778899")
        self.Button_login_guest.configure(borderwidth="2")
        self.Button_login_guest.configure(command=lambda: proj_support.login_guest(controller))
        self.Button_login_guest.configure(compound='left')
        self.Button_login_guest.configure(disabledforeground="#b9b9bb")
        self.Button_login_guest.configure(foreground="#f6f7f9")
        self.Button_login_guest.configure(highlightbackground="#778899")
        self.Button_login_guest.configure(relief="flat")
        self.Button_login_guest.configure(text='''Login as guest''')

        self.Button_login_back = tk.Button(self)
        self.Button_login_back.place(relx=0.0, rely=0.0, height=33, width=52)
        self.Button_login_back.configure(command=lambda: proj_support.goto(controller, "SetUpPage"))
        self.Button_login_back.configure(background="#f6f7f9")
        self.Button_login_back.configure(relief='flat', highlightthickness=0)
        self.photo = PhotoImage(file=r"ic_back.png")
        self.Button_login_back.configure(text='Back', image=self.photo)
