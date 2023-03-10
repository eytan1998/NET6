import tkinter as tk

from Frontend import proj_support
from Frontend.ScrolledListBox import ScrolledListBox
from Frontend.proj_support import _style_code


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
        self.Scrolledlistbox_mngabai.place(relx=0.083, rely=0.111, relheight=0.551, relwidth=0.827)
        self.Scrolledlistbox_mngabai.configure(background="white")
        self.Scrolledlistbox_mngabai.configure(cursor="xterm")
        self.Scrolledlistbox_mngabai.configure(disabledforeground="#b9b9bb")
        self.Scrolledlistbox_mngabai.configure(font="TkFixedFont")
        self.Scrolledlistbox_mngabai.configure(highlightbackground="#f6f7f9")
        self.Scrolledlistbox_mngabai.configure(highlightcolor="#778899")
        self.Scrolledlistbox_mngabai.configure(selectbackground="#dedfe0")

        self.Button_mngabai_add = tk.Button(self)
        self.Button_mngabai_add.place(relx=0.1, rely=0.822, height=43, width=143)

        self.Button_mngabai_add.configure(activebackground="beige")
        self.Button_mngabai_add.configure(background="#778899")
        self.Button_mngabai_add.configure(borderwidth="2")
        self.Button_mngabai_add.configure(command=lambda: proj_support.add_gabai(controller))
        self.Button_mngabai_add.configure(compound='left')
        self.Button_mngabai_add.configure(disabledforeground="#b9b9bb")
        self.Button_mngabai_add.configure(foreground="#f6f7f9")
        self.Button_mngabai_add.configure(highlightbackground="#778899")
        self.Button_mngabai_add.configure(relief="flat")
        self.Button_mngabai_add.configure(text='''Add''')

        self.Button_mngabai_del = tk.Button(self)
        self.Button_mngabai_del.place(relx=0.667, rely=0.822, height=43, width=143)
        self.Button_mngabai_del.configure(activebackground="beige")
        self.Button_mngabai_del.configure(background="#778899")
        self.Button_mngabai_del.configure(borderwidth="2")
        self.Button_mngabai_del.configure(
            command=lambda: proj_support.del_gabai(controller, self.Scrolledlistbox_mngabai))
        self.Button_mngabai_del.configure(compound='left')
        self.Button_mngabai_del.configure(disabledforeground="#b9b9bb")
        self.Button_mngabai_del.configure(foreground="#f6f7f9")
        self.Button_mngabai_del.configure(highlightbackground="#778899")
        self.Button_mngabai_del.configure(relief="flat")
        self.Button_mngabai_del.configure(text='''Del''')

        self.Button_mngabai_edit = tk.Button(self)
        self.Button_mngabai_edit.place(relx=0.383, rely=0.822, height=43, width=143)
        self.Button_mngabai_edit.configure(activebackground="beige")
        self.Button_mngabai_edit.configure(background="#778899")
        self.Button_mngabai_edit.configure(borderwidth="2")
        self.Button_mngabai_edit.configure(
            command=lambda: proj_support.edit_gabai(controller, self.Scrolledlistbox_mngabai))
        self.Button_mngabai_edit.configure(compound='left')
        self.Button_mngabai_edit.configure(disabledforeground="#b9b9bb")
        self.Button_mngabai_edit.configure(foreground="#f6f7f9")
        self.Button_mngabai_edit.configure(highlightbackground="#778899")
        self.Button_mngabai_edit.configure(relief="flat")
        self.Button_mngabai_edit.configure(text='''Edit''')

        self.Button_mngabai_back = tk.Button(self)
        self.Button_mngabai_back.place(relx=0.0, rely=0.0, height=33, width=52)
        self.Button_mngabai_back.configure(command=lambda: proj_support.goto(controller, "MainPage"))
        self.Button_mngabai_back.configure(background="#f6f7f9")
        self.Button_mngabai_back.configure(relief='flat', highlightthickness=0)
        self.photo = tk.PhotoImage(file=r"Frontend/ic_back.png")
        self.Button_mngabai_back.configure(text='Back', image=self.photo)

    def update(self) -> None:
        proj_support.display_gabai_list(self.controller, self.Scrolledlistbox_mngabai)
