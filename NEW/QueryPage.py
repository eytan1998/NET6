import tkinter as tk
import tkinter.ttk as ttk
from tkinter import END

import proj_support
from ScrolledListBox import ScrolledListBox
from proj_support import _style_code
from synagogue import Nosah
from synagogue import City


class QueryPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        controller.geometry("600x455+469+553")
        controller.minsize(1, 1)
        controller.maxsize(1905, 1050)
        controller.resizable(1, 1)
        self.configure(background="#f6f7f9")
        controller.configure(highlightbackground="#f6f7f9")
        controller.configure(highlightcolor="black")

        self.controller = controller
        self.comboboxNosah = tk.StringVar()
        self.comboboxCity = tk.StringVar()
        _style_code()

        self.Scrolledlistbox_query = ScrolledListBox(self)
        self.Scrolledlistbox_query.place(relx=0.033, rely=0.308, relheight=0.642
                                         , relwidth=0.943)
        self.Scrolledlistbox_query.configure(background="white")
        self.Scrolledlistbox_query.configure(cursor="xterm")
        self.Scrolledlistbox_query.configure(disabledforeground="#b9b9bb")
        self.Scrolledlistbox_query.configure(font="TkFixedFont")
        self.Scrolledlistbox_query.configure(highlightbackground="#f6f7f9")
        self.Scrolledlistbox_query.configure(highlightcolor="#778899")
        self.Scrolledlistbox_query.configure(selectbackground="#dedfe0")

        self.TCombobox_query_city = ttk.Combobox(self)
        self.TCombobox_query_city.place(relx=0.5, rely=0.176, relheight=0.046
                                        , relwidth=0.245)
        self.TCombobox_query_city.configure(textvariable=self.comboboxCity)
        self.TCombobox_query_city.configure(takefocus="")
        self.TCombobox_query_city.configure(foreground="#000000")
        self.TCombobox_query_city['values'] = City.getAll()
        self.TCombobox_query_city.set(City.NULL.name)

        self.TCombobox_query_nosah = ttk.Combobox(self)
        self.TCombobox_query_nosah.place(relx=0.15, rely=0.176, relheight=0.046, relwidth=0.212)
        self.TCombobox_query_nosah.configure(textvariable=self.comboboxNosah)
        self.TCombobox_query_nosah.configure(takefocus="")
        self.TCombobox_query_nosah.configure(foreground="#000000")
        self.TCombobox_query_nosah['values'] = Nosah.getAll()
        self.TCombobox_query_nosah.set(Nosah.NULL.name)

        self.TEntry_query_query = ttk.Entry(self)
        self.TEntry_query_query.place(relx=0.183, rely=0.066, relheight=0.046, relwidth=0.74)
        self.TEntry_query_query.configure(takefocus="")
        self.TEntry_query_query.configure(foreground="#000000")
        self.TEntry_query_query.configure(cursor="xterm")

        self.Label_query_query = tk.Label(self)
        self.Label_query_query.place(relx=0.033, rely=0.044, height=41, width=49)
        self.Label_query_query.configure(activebackground="#ffffff")
        self.Label_query_query.configure(anchor='w')
        self.Label_query_query.configure(background="#f6f7f9")
        self.Label_query_query.configure(compound='center')
        self.Label_query_query.configure(disabledforeground="#b9b9bb")
        self.Label_query_query.configure(font="-family {DejaVu Sans} -size 12")
        self.Label_query_query.configure(foreground="#778899")
        self.Label_query_query.configure(highlightbackground="#f6f7f9")
        self.Label_query_query.configure(text='''Name''')

        self.Label_query_nosah = tk.Label(self)
        self.Label_query_nosah.place(relx=0.033, rely=0.154, height=41, width=59)
        self.Label_query_nosah.configure(activebackground="#ffffff")
        self.Label_query_nosah.configure(anchor='w')
        self.Label_query_nosah.configure(background="#f6f7f9")
        self.Label_query_nosah.configure(compound='center')
        self.Label_query_nosah.configure(disabledforeground="#b9b9bb")
        self.Label_query_nosah.configure(font="-family {DejaVu Sans} -size 12")
        self.Label_query_nosah.configure(foreground="#778899")
        self.Label_query_nosah.configure(highlightbackground="#f6f7f9")
        self.Label_query_nosah.configure(text='''Nosah''')

        self.Label_query_city = tk.Label(self)
        self.Label_query_city.place(relx=0.4, rely=0.154, height=41, width=49)
        self.Label_query_city.configure(activebackground="#ffffff")
        self.Label_query_city.configure(anchor='w')
        self.Label_query_city.configure(background="#f6f7f9")
        self.Label_query_city.configure(compound='center')
        self.Label_query_city.configure(disabledforeground="#b9b9bb")
        self.Label_query_city.configure(font="-family {DejaVu Sans} -size 12")
        self.Label_query_city.configure(foreground="#778899")
        self.Label_query_city.configure(highlightbackground="#f6f7f9")
        self.Label_query_city.configure(text='''City''')

        self.Button_query_search = tk.Button(self)
        self.Button_query_search.place(relx=0.767, rely=0.176, height=43, width=113)
        self.Button_query_search.configure(activebackground="#5faeb6")
        self.Button_query_search.configure(background="#778899")
        self.Button_query_search.configure(borderwidth="2")
        self.Button_query_search.configure(command=lambda: proj_support.send_query(controller, self.TEntry_query_query.get(),
                                                                                   Nosah.__getitem__(
                                                                                       self.TCombobox_query_nosah.get()),
                                                                                   City.__getitem__(
                                                                                       self.TCombobox_query_city.get()),
                                                                                   self.Scrolledlistbox_query))
        self.Button_query_search.configure(compound='left')
        self.Button_query_search.configure(disabledforeground="#b9b9bb")
        self.Button_query_search.configure(foreground="#f6f7f9")
        self.Button_query_search.configure(highlightbackground="#778899")
        self.Button_query_search.configure(relief="flat")
        self.Button_query_search.configure(text='''Search''')

        self.Button_query_back = tk.Button(self)
        self.Button_query_back.place(relx=0.0, rely=0.0, height=33, width=52)
        self.Button_query_back.configure(activebackground="#5faeb6")
        self.Button_query_back.configure(command=lambda: proj_support.goto(controller, "MainPage"))
        self.Button_query_back.configure(background="#778899")
        self.Button_query_back.configure(borderwidth="2")
        self.Button_query_back.configure(compound='left')
        self.Button_query_back.configure(foreground="#f6f7f9")
        self.Button_query_back.configure(highlightbackground="#778899")
        self.Button_query_back.configure(relief="flat")
        self.Button_query_back.configure(text='''Back''')

        self.Button_query_View = tk.Button(self)
        self.Button_query_View.place(relx=0.417, rely=0.879, height=43
                                     , width=113)
        self.Button_query_View.configure(activebackground="#5faeb6")
        self.Button_query_View.configure(background="#778899")
        self.Button_query_View.configure(borderwidth="2")
        self.Button_query_View.configure(command=lambda: proj_support.view_syng(controller, self.Scrolledlistbox_query))
        self.Button_query_View.configure(compound='left')
        self.Button_query_View.configure(disabledforeground="#b9b9bb")
        self.Button_query_View.configure(foreground="#f6f7f9")
        self.Button_query_View.configure(highlightbackground="#778899")
        self.Button_query_View.configure(relief="flat")
        self.Button_query_View.configure(text='''View''')

    def update(self) -> None:
        self.Scrolledlistbox_query.delete(0,END)
