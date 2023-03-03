import tkinter as tk
from tkinter import ttk, END

import proj_support
from gabai import Gabai
from proj_support import _style_code


class ViewGabaiPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        controller.geometry("600x453+1122+393")
        controller.minsize(1, 1)
        controller.maxsize(1905, 1050)
        controller.resizable(1, 1)
        self.configure(background="#f6f7f9")

        self.Label_viewsgabai_name = tk.Label(self)
        self.Label_viewsgabai_name.place(relx=0.067, rely=0.132, height=31
                                         , width=49)
        self.Label_viewsgabai_name.configure(activebackground="#ffffff")
        self.Label_viewsgabai_name.configure(anchor='w')
        self.Label_viewsgabai_name.configure(background="#f6f7f9")
        self.Label_viewsgabai_name.configure(compound='center')
        self.Label_viewsgabai_name.configure(disabledforeground="#b9b9bb")
        self.Label_viewsgabai_name.configure(font="-family {DejaVu Sans} -size 12")
        self.Label_viewsgabai_name.configure(foreground="#778899")
        self.Label_viewsgabai_name.configure(highlightbackground="#f6f7f9")
        self.Label_viewsgabai_name.configure(text='''Name''')
        _style_code()

        self.TEntry_viewgabai_name = ttk.Entry(self)
        self.TEntry_viewgabai_name.place(relx=0.3, rely=0.132, relheight=0.046
                                         , relwidth=0.623)
        self.TEntry_viewgabai_name.configure(takefocus="")
        self.TEntry_viewgabai_name.configure(cursor="fleur")
        self.TEntry_viewgabai_name.configure(foreground="black")

        self.Label_viewgabai_ID = tk.Label(self)
        self.Label_viewgabai_ID.place(relx=0.083, rely=0.243, height=41
                                      , width=59)
        self.Label_viewgabai_ID.configure(activebackground="#ffffff")
        self.Label_viewgabai_ID.configure(anchor='w')
        self.Label_viewgabai_ID.configure(background="#f6f7f9")
        self.Label_viewgabai_ID.configure(compound='center')
        self.Label_viewgabai_ID.configure(disabledforeground="#b9b9bb")
        self.Label_viewgabai_ID.configure(font="-family {DejaVu Sans} -size 12")
        self.Label_viewgabai_ID.configure(foreground="#778899")
        self.Label_viewgabai_ID.configure(highlightbackground="#f6f7f9")
        self.Label_viewgabai_ID.configure(text='''ID''')

        self.Label_viewgabai_pass = tk.Label(self)
        self.Label_viewgabai_pass.place(relx=0.05, rely=0.375, height=41
                                        , width=89)
        self.Label_viewgabai_pass.configure(activebackground="#ffffff")
        self.Label_viewgabai_pass.configure(anchor='w')
        self.Label_viewgabai_pass.configure(background="#f6f7f9")
        self.Label_viewgabai_pass.configure(compound='center')
        self.Label_viewgabai_pass.configure(disabledforeground="#b9b9bb")
        self.Label_viewgabai_pass.configure(font="-family {DejaVu Sans} -size 12")
        self.Label_viewgabai_pass.configure(foreground="#778899")
        self.Label_viewgabai_pass.configure(highlightbackground="#f6f7f9")
        self.Label_viewgabai_pass.configure(text='''Password''')

        self.Label_viewgabai_phone = tk.Label(self)
        self.Label_viewgabai_phone.place(relx=0.067, rely=0.508, height=41
                                         , width=109)
        self.Label_viewgabai_phone.configure(activebackground="#ffffff")
        self.Label_viewgabai_phone.configure(anchor='w')
        self.Label_viewgabai_phone.configure(background="#f6f7f9")
        self.Label_viewgabai_phone.configure(compound='center')
        self.Label_viewgabai_phone.configure(disabledforeground="#b9b9bb")
        self.Label_viewgabai_phone.configure(font="-family {DejaVu Sans} -size 12")
        self.Label_viewgabai_phone.configure(foreground="#778899")
        self.Label_viewgabai_phone.configure(highlightbackground="#f6f7f9")
        self.Label_viewgabai_phone.configure(text='''Phone''')

        self.TEntry_viewgabai_phone = ttk.Entry(self)
        self.TEntry_viewgabai_phone.place(relx=0.3, rely=0.53, relheight=0.046
                                          , relwidth=0.623)
        self.TEntry_viewgabai_phone.configure(takefocus="")
        self.TEntry_viewgabai_phone.configure(cursor="fleur")
        self.TEntry_viewgabai_phone.configure(foreground="black")

        self.Button_viewgabai_save = tk.Button(self)
        self.Button_viewgabai_save.place(relx=0.417, rely=0.883, height=43
                                         , width=113)
        self.Button_viewgabai_save.configure(activebackground="#5faeb6")
        self.Button_viewgabai_save.configure(background="#778899")
        self.Button_viewgabai_save.configure(borderwidth="2")
        self.Button_viewgabai_save.configure(command=lambda: proj_support.save_gabai(controller, Gabai(
            name=self.TEntry_viewgabai_name.get(),
            gabai_id=self.controller.gabai_to_view.gabai_id,
            password=self.TEntry_viewgabai_pass.get()
            , phone=self.TEntry_viewgabai_phone.get(),
            synagogue_list=self.controller.gabai_to_view.synagogue_list)))
        self.Button_viewgabai_save.configure(disabledforeground="#b9b9bb")
        self.Button_viewgabai_save.configure(foreground="#f6f7f9")
        self.Button_viewgabai_save.configure(highlightbackground="#778899")
        self.Button_viewgabai_save.configure(relief="flat")
        self.Button_viewgabai_save.configure(text='''Save''')



        self.TEntry_viewgabai_pass = ttk.Entry(self)
        self.TEntry_viewgabai_pass.place(relx=0.3, rely=0.397, relheight=0.046
                                         , relwidth=0.623)
        self.TEntry_viewgabai_pass.configure(takefocus="")
        self.TEntry_viewgabai_pass.configure(cursor="fleur")
        self.TEntry_viewgabai_pass.configure(foreground="black")

        self.TEntry_viewgabai_ID = ttk.Entry(self)
        self.TEntry_viewgabai_ID.place(relx=0.3, rely=0.265, relheight=0.046
                                       , relwidth=0.623)
        self.TEntry_viewgabai_ID.configure(takefocus="")
        self.TEntry_viewgabai_ID.configure(cursor="fleur")
        self.TEntry_viewgabai_ID.configure(foreground="black")

        self.Button_viewgabai_back = tk.Button(self)
        self.Button_viewgabai_back.place(relx=0.0, rely=0.0, height=33, width=52)
        self.Button_viewgabai_back.configure(command=lambda: proj_support.goto(self.controller, "ManageGabaiPage"))
        self.Button_viewgabai_back.configure(background="#f6f7f9")
        self.Button_viewgabai_back.configure(relief='flat', highlightthickness=0)
        self.photo = tk.PhotoImage(file=r"ic_back.png")
        self.Button_viewgabai_back.configure(text='Back', image=self.photo)

    def update(self) -> None:
        x = self.controller.gabai_to_view
        if x is None: return

        self.TEntry_viewgabai_ID.configure(state='normal')

        self.TEntry_viewgabai_name.delete(0, END)
        self.TEntry_viewgabai_name.insert(0, x.name)
        self.TEntry_viewgabai_ID.delete(0, END)
        self.TEntry_viewgabai_ID.insert(0, x.gabai_id)
        self.TEntry_viewgabai_pass.delete(0, END)
        self.TEntry_viewgabai_pass.insert(0, x.password)
        self.TEntry_viewgabai_phone.delete(0, END)
        self.TEntry_viewgabai_phone.insert(0, x.phone)

        self.TEntry_viewgabai_ID.configure(state='disabled')
