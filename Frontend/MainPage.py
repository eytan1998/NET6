import tkinter as tk  # python 3

from Frontend import proj_support


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        controller.geometry("600x450+1215+115")
        controller.minsize(1, 1)
        controller.maxsize(1905, 1050)
        controller.resizable(1, 1)
        self.configure(background="#f6f7f9")
        controller.configure(highlightbackground="#f6f7f9")
        controller.configure(highlightcolor="black")

        self.controller = controller

        self.Button_main_query = tk.Button(self)
        self.Button_main_query.place(relx=0.367, rely=0.178, height=43, width=143)
        self.Button_main_query.configure(activebackground="#5faeb6")
        self.Button_main_query.configure(background="#778899")
        self.Button_main_query.configure(borderwidth="2")
        self.Button_main_query.configure(command=lambda: proj_support.goto(controller, "QueryPage"))
        self.Button_main_query.configure(compound='left')
        self.Button_main_query.configure(disabledforeground="#b9b9bb")
        self.Button_main_query.configure(foreground="#f6f7f9")
        self.Button_main_query.configure(highlightbackground="#778899")
        self.Button_main_query.configure(relief="flat")
        self.Button_main_query.configure(text='''Query''')
        self.Button_main_manage_syn = tk.Button(self)
        self.Button_main_manage_syn.place(relx=0.367, rely=0.333, height=43, width=143)
        self.Button_main_manage_syn.configure(activebackground="#5faeb6")
        self.Button_main_manage_syn.configure(background="#778899")
        self.Button_main_manage_syn.configure(borderwidth="2")
        self.Button_main_manage_syn.configure(command=lambda: proj_support.goto_manage_syng(controller))
        self.Button_main_manage_syn.configure(compound='left')
        self.Button_main_manage_syn.configure(disabledforeground="#b9b9bb")
        self.Button_main_manage_syn.configure(foreground="#f6f7f9")
        self.Button_main_manage_syn.configure(highlightbackground="#778899")
        self.Button_main_manage_syn.configure(relief="flat")
        self.Button_main_manage_syn.configure(text='''Manage synagogue''')
        self.Button_main_manag_gab = tk.Button(self)
        self.Button_main_manag_gab.place(relx=0.367, rely=0.489, height=43, width=143)
        self.Button_main_manag_gab.configure(activebackground="#5faeb6")
        self.Button_main_manag_gab.configure(background="#778899")
        self.Button_main_manag_gab.configure(borderwidth="2")
        self.Button_main_manag_gab.configure(command=lambda: proj_support.goto_manage_gabai(controller))
        self.Button_main_manag_gab.configure(compound='left')
        self.Button_main_manag_gab.configure(disabledforeground="#b9b9bb")
        self.Button_main_manag_gab.configure(foreground="#f6f7f9")
        self.Button_main_manag_gab.configure(highlightbackground="#778899")
        self.Button_main_manag_gab.configure(relief="flat")
        self.Button_main_manag_gab.configure(text='''Manage gabaies''')

        self.Label_setup_name = tk.Label(self)
        self.Label_setup_name.place(relx=0.05, rely=0.867, height=41, width=539)
        self.Label_setup_name.configure(activebackground="#ffffff")
        self.Label_setup_name.configure(anchor='w')
        self.Label_setup_name.configure(background="#f6f7f9")
        self.Label_setup_name.configure(compound='center')
        self.Label_setup_name.configure(disabledforeground="#b9b9bb")
        self.Label_setup_name.configure(font="-family {DejaVu Sans} -size 16")
        self.Label_setup_name.configure(foreground="#778899")
        self.Label_setup_name.configure(highlightbackground="#f6f7f9")
        self.Label_setup_name.configure(text='''Current user: Guest''')

        self.Button_main_back = tk.Button(self)
        self.Button_main_back.place(relx=0.0, rely=0.0, height=33, width=52)
        self.Button_main_back.configure(command=lambda: proj_support.goto(controller, "LoginPage"))
        self.Button_main_back.configure(background="#f6f7f9")
        self.Button_main_back.configure(relief='flat', highlightthickness=0)
        self.photo = tk.PhotoImage(file=r"Frontend/ic_back.png")
        self.Button_main_back.configure(text='Back', image=self.photo)

    def update(self) -> None:
        try:
            self.Label_setup_name.configure(text='''Current user: ''' + self.controller.gabai.name)
        except:
            self.Label_setup_name.configure(text='''Current user: Guest''')