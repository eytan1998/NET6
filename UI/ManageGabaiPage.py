import tkinter as tk

from UI import proj_support
from UI.proj_support import _style_code
from UI.ScrolledListBox import ScrolledListBox


class ManageGabaiPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        controller.geometry("600x450+745+485")
        controller.minsize(1, 1)
        controller.maxsize(1905, 1050)
        controller.resizable(1, 1)
        self.configure(background="#f6f7f9")

        self.controller = controller

        _style_code()
        self.Scrolledlistbox_mngabai = ScrolledListBox(self)
        self.Scrolledlistbox_mngabai.place(relx=0.083, rely=0.089, relheight=0.64
                                           , relwidth=0.843)
        self.Scrolledlistbox_mngabai.configure(background="white")
        self.Scrolledlistbox_mngabai.configure(cursor="xterm")
        self.Scrolledlistbox_mngabai.configure(disabledforeground="#b9b9bb")
        self.Scrolledlistbox_mngabai.configure(font="TkFixedFont")
        self.Scrolledlistbox_mngabai.configure(highlightbackground="#f6f7f9")
        self.Scrolledlistbox_mngabai.configure(highlightcolor="#778899")
        self.Scrolledlistbox_mngabai.configure(selectbackground="#dedfe0")
        self.Button_mngabai_add = tk.Button(self)
        self.Button_mngabai_add.place(relx=0.167, rely=0.822, height=43
                                      , width=143)
        self.Button_mngabai_add.configure(activebackground="#5faeb6")
        self.Button_mngabai_add.configure(background="#778899")
        self.Button_mngabai_add.configure(borderwidth="2")
        self.Button_mngabai_add.configure(command=proj_support.get_gabai)
        self.Button_mngabai_add.configure(compound='left')
        self.Button_mngabai_add.configure(disabledforeground="#b9b9bb")
        self.Button_mngabai_add.configure(foreground="#f6f7f9")
        self.Button_mngabai_add.configure(highlightbackground="#778899")
        self.Button_mngabai_add.configure(relief="flat")
        self.Button_mngabai_add.configure(text='''Add''')
        self.Button_mngabai_del = tk.Button(self)
        self.Button_mngabai_del.place(relx=0.6, rely=0.822, height=43, width=143)

        self.Button_mngabai_del.configure(activebackground="#5faeb6")
        self.Button_mngabai_del.configure(background="#778899")
        self.Button_mngabai_del.configure(borderwidth="2")
        self.Button_mngabai_del.configure(command=proj_support.get_gabai)
        self.Button_mngabai_del.configure(compound='left')
        self.Button_mngabai_del.configure(disabledforeground="#b9b9bb")
        self.Button_mngabai_del.configure(foreground="#f6f7f9")
        self.Button_mngabai_del.configure(highlightbackground="#778899")
        self.Button_mngabai_del.configure(relief="flat")
        self.Button_mngabai_del.configure(text='''Del''')

        self.Button_mngabai_back = tk.Button(self)
        self.Button_mngabai_back.place(relx=0.0, rely=0.0, height=33, width=52)
        self.Button_mngabai_back.configure(command=lambda: proj_support.goto(controller, "MainPage"))
        self.Button_mngabai_back.configure(activebackground="#5faeb6")
        self.Button_mngabai_back.configure(background="#778899")
        self.Button_mngabai_back.configure(borderwidth="2")
        self.Button_mngabai_back.configure(compound='left')
        self.Button_mngabai_back.configure(foreground="#f6f7f9")
        self.Button_mngabai_back.configure(highlightbackground="#778899")
        self.Button_mngabai_back.configure(relief="flat")
        self.Button_mngabai_back.configure(text='''Back''')
