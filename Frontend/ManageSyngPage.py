import tkinter as tk

from Frontend import proj_support
from Frontend.ScrolledListBox import ScrolledListBox
from Frontend.proj_support import _style_code


class ManageSyngPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        controller.geometry("600x450+718+577")
        controller.minsize(1, 1)
        controller.maxsize(1905, 1050)
        controller.resizable(1, 1)
        self.configure(background="#f6f7f9")

        self.controller = controller

        _style_code()
        self.Scrolledlistbox_mngsyng = ScrolledListBox(self)
        self.Scrolledlistbox_mngsyng.place(relx=0.083, rely=0.111, relheight=0.551, relwidth=0.827)
        self.Scrolledlistbox_mngsyng.configure(background="white")
        self.Scrolledlistbox_mngsyng.configure(cursor="xterm")
        self.Scrolledlistbox_mngsyng.configure(disabledforeground="#b9b9bb")
        self.Scrolledlistbox_mngsyng.configure(font="TkFixedFont")
        self.Scrolledlistbox_mngsyng.configure(highlightbackground="#f6f7f9")
        self.Scrolledlistbox_mngsyng.configure(highlightcolor="#778899")
        self.Scrolledlistbox_mngsyng.configure(selectbackground="#dedfe0")

        self.Button_mngsyng_add = tk.Button(self)
        self.Button_mngsyng_add.place(relx=0.1, rely=0.778, height=43, width=143)
        self.Button_mngsyng_add.configure(activebackground="#5faeb6")
        self.Button_mngsyng_add.configure(background="#778899")
        self.Button_mngsyng_add.configure(borderwidth="2")
        self.Button_mngsyng_add.configure(command=lambda: proj_support.add_syng(controller))
        self.Button_mngsyng_add.configure(compound='left')
        self.Button_mngsyng_add.configure(disabledforeground="#b9b9bb")
        self.Button_mngsyng_add.configure(foreground="#f6f7f9")
        self.Button_mngsyng_add.configure(highlightbackground="#778899")
        self.Button_mngsyng_add.configure(relief="flat")
        self.Button_mngsyng_add.configure(text='''Add''')
        self.Button_mngsyng_edit = tk.Button(self)
        self.Button_mngsyng_edit.place(relx=0.383, rely=0.778, height=43, width=143)
        self.Button_mngsyng_edit.configure(activebackground="#5faeb6")
        self.Button_mngsyng_edit.configure(background="#778899")
        self.Button_mngsyng_edit.configure(borderwidth="2")
        self.Button_mngsyng_edit.configure(
            command=lambda: proj_support.edit_syng(controller, self.Scrolledlistbox_mngsyng))
        self.Button_mngsyng_edit.configure(compound='left')
        self.Button_mngsyng_edit.configure(disabledforeground="#b9b9bb")
        self.Button_mngsyng_edit.configure(foreground="#f6f7f9")
        self.Button_mngsyng_edit.configure(highlightbackground="#778899")
        self.Button_mngsyng_edit.configure(relief="flat")
        self.Button_mngsyng_edit.configure(text='''Edit''')
        self.Button_mngsyng_del = tk.Button(self)
        self.Button_mngsyng_del.place(relx=0.667, rely=0.778, height=43, width=143)
        self.Button_mngsyng_del.configure(activebackground="#5faeb6")
        self.Button_mngsyng_del.configure(background="#778899")
        self.Button_mngsyng_del.configure(borderwidth="2")
        self.Button_mngsyng_del.configure(
            command=lambda: proj_support.del_syng(controller, self.Scrolledlistbox_mngsyng))
        self.Button_mngsyng_del.configure(compound='left')
        self.Button_mngsyng_del.configure(cursor="fleur")
        self.Button_mngsyng_del.configure(disabledforeground="#b9b9bb")
        self.Button_mngsyng_del.configure(foreground="#f6f7f9")
        self.Button_mngsyng_del.configure(highlightbackground="#778899")
        self.Button_mngsyng_del.configure(relief="flat")
        self.Button_mngsyng_del.configure(text='''Del''')

        self.Button_mngsyng_back = tk.Button(self)
        self.Button_mngsyng_back.place(relx=0.0, rely=0.0, height=33, width=52)
        self.Button_mngsyng_back.configure(command=lambda: proj_support.goto(controller, "MainPage"))
        self.Button_mngsyng_back.configure(background="#f6f7f9")
        self.Button_mngsyng_back.configure(relief='flat', highlightthickness=0)
        self.photo = tk.PhotoImage(file=r"Frontend/ic_back.png")
        self.Button_mngsyng_back.configure(text='Back', image=self.photo)

    def update(self) -> None:
        proj_support.display_syng_list(self.controller, self.Scrolledlistbox_mngsyng)
