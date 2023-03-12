import tkinter as tk  # python 3
from tkinter import ttk

from Frontend import proj_support
from Frontend.proj_support import _style_code


class SetUpPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        controller.configure(highlightcolor="black")

        controller.geometry("600x450+945+434")
        controller.minsize(1, 1)
        controller.maxsize(1905, 1050)
        controller.resizable(0, 0)
        self.configure(background="#f6f7f9")


        self.Label_setup_title = tk.Label(self)
        self.Label_setup_title.place(relx=0.25, rely=0.089, height=41, width=319)

        self.Label_setup_title.configure(activebackground="#ffffff")
        self.Label_setup_title.configure(anchor='w')
        self.Label_setup_title.configure(background="#f6f7f9")
        self.Label_setup_title.configure(compound='center')
        self.Label_setup_title.configure(disabledforeground="#b9b9bb")
        self.Label_setup_title.configure(font="-family {DejaVu Sans} -size 24")
        self.Label_setup_title.configure(foreground="#778899")
        self.Label_setup_title.configure(highlightbackground="#f6f7f9")
        self.Label_setup_title.configure(text='''Set up connection''')

        self.Label_DHCP_adress = tk.Label(self)
        self.Label_DHCP_adress.place(relx=0.117, rely=0.356, height=41
                                     , width=169)
        self.Label_DHCP_adress.configure(activebackground="#ffffff")
        self.Label_DHCP_adress.configure(anchor='w')
        self.Label_DHCP_adress.configure(background="#f6f7f9")
        self.Label_DHCP_adress.configure(compound='center')
        self.Label_DHCP_adress.configure(disabledforeground="#b9b9bb")
        self.Label_DHCP_adress.configure(font="-family {DejaVu Sans} -size 12")
        self.Label_DHCP_adress.configure(foreground="#778899")
        self.Label_DHCP_adress.configure(highlightbackground="#f6f7f9")
        self.Label_DHCP_adress.configure(text='''server domain''')
        _style_code()

        self.TEntry_DHCP_addres = ttk.Entry(self)
        self.TEntry_DHCP_addres.place(relx=0.45, rely=0.356, relheight=0.069
                                      , relwidth=0.423)
        self.TEntry_DHCP_addres.configure(takefocus="")
        self.TEntry_DHCP_addres.configure(cursor="xterm")
        self.TEntry_DHCP_addres.configure(foreground="black")

        self.Log_setup = tk.Text(self)
        self.Log_setup.place(relx=0.117, rely=0.756, relheight=0.209
                             , relwidth=0.793)
        self.Log_setup.configure(background="white")
        self.Log_setup.configure(font="TkTextFont")
        self.Log_setup.configure(highlightbackground="#778899")
        self.Log_setup.configure(selectbackground="#dedfe0")
        self.Log_setup.configure(wrap="none")

        self.Button_setup_connect = tk.Button(self)
        self.Button_setup_connect.place(relx=0.417, rely=0.578, height=43
                                        , width=113)
        self.Button_setup_connect.configure(activebackground="#5faeb6")
        self.Button_setup_connect.configure(background="#778899")
        self.Button_setup_connect.configure(borderwidth="2")
        self.Button_setup_connect.configure(
            command=lambda: proj_support.connect(controller, self.TEntry_DHCP_addres.get(),self.Log_setup))
        self.Button_setup_connect.configure(compound='left')
        self.Button_setup_connect.configure(disabledforeground="#b9b9bb")
        self.Button_setup_connect.configure(foreground="#f6f7f9")
        self.Button_setup_connect.configure(highlightbackground="#778899")
        self.Button_setup_connect.configure(relief="flat")
        self.Button_setup_connect.configure(text='''Connect''')

