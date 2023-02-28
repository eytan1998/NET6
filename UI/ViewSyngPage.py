import tkinter as tk
import tkinter.ttk as ttk
from UI import proj_support
from UI.ScrolledListBox import ScrolledText
from UI.proj_support import _style_code


class ViewSyngPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        controller.geometry("600x453+1122+393")
        controller.minsize(1, 1)
        controller.maxsize(1905, 1050)
        controller.resizable(1, 1)
        self.configure(background="#f6f7f9")

        self.combobox = tk.StringVar()

        self.Label_viewsyng_name = tk.Label(self)
        self.Label_viewsyng_name.place(relx=0.067, rely=0.044, height=41
                                       , width=49)
        self.Label_viewsyng_name.configure(activebackground="#ffffff")
        self.Label_viewsyng_name.configure(anchor='w')
        self.Label_viewsyng_name.configure(background="#f6f7f9")
        self.Label_viewsyng_name.configure(compound='center')
        self.Label_viewsyng_name.configure(disabledforeground="#b9b9bb")
        self.Label_viewsyng_name.configure(font="-family {DejaVu Sans} -size 12")
        self.Label_viewsyng_name.configure(foreground="#778899")
        self.Label_viewsyng_name.configure(highlightbackground="#f6f7f9")
        self.Label_viewsyng_name.configure(text='''Name''')
        _style_code()
        self.TEntry_viewsyng_name = ttk.Entry(self)
        self.TEntry_viewsyng_name.place(relx=0.267, rely=0.066, relheight=0.046
                                        , relwidth=0.69)
        self.TEntry_viewsyng_name.configure(takefocus="")
        self.TEntry_viewsyng_name.configure(cursor="fleur")
        self.Label_viewsyng_nosah = tk.Label(self)
        self.Label_viewsyng_nosah.place(relx=0.067, rely=0.132, height=41
                                        , width=49)
        self.Label_viewsyng_nosah.configure(activebackground="#ffffff")
        self.Label_viewsyng_nosah.configure(anchor='w')
        self.Label_viewsyng_nosah.configure(background="#f6f7f9")
        self.Label_viewsyng_nosah.configure(compound='center')
        self.Label_viewsyng_nosah.configure(cursor="fleur")
        self.Label_viewsyng_nosah.configure(disabledforeground="#b9b9bb")
        self.Label_viewsyng_nosah.configure(font="-family {DejaVu Sans} -size 12")
        self.Label_viewsyng_nosah.configure(foreground="#778899")
        self.Label_viewsyng_nosah.configure(highlightbackground="#f6f7f9")
        self.Label_viewsyng_nosah.configure(text='''Nosah''')
        self.Label_viewsyng_city = tk.Label(self)
        self.Label_viewsyng_city.place(relx=0.067, rely=0.223, height=41
                                       , width=49)
        self.Label_viewsyng_city.configure(activebackground="#ffffff")
        self.Label_viewsyng_city.configure(anchor='w')
        self.Label_viewsyng_city.configure(background="#f6f7f9")
        self.Label_viewsyng_city.configure(compound='center')
        self.Label_viewsyng_city.configure(disabledforeground="#b9b9bb")
        self.Label_viewsyng_city.configure(font="-family {DejaVu Sans} -size 12")
        self.Label_viewsyng_city.configure(foreground="#778899")
        self.Label_viewsyng_city.configure(highlightbackground="#f6f7f9")
        self.Label_viewsyng_city.configure(text='''City''')
        self.Label_viewsyng_gabainame = tk.Label(self)
        self.Label_viewsyng_gabainame.place(relx=0.067, rely=0.311, height=41
                                            , width=109)
        self.Label_viewsyng_gabainame.configure(activebackground="#ffffff")
        self.Label_viewsyng_gabainame.configure(anchor='w')
        self.Label_viewsyng_gabainame.configure(background="#f6f7f9")
        self.Label_viewsyng_gabainame.configure(compound='center')
        self.Label_viewsyng_gabainame.configure(disabledforeground="#b9b9bb")
        self.Label_viewsyng_gabainame.configure(font="-family {DejaVu Sans} -size 12")
        self.Label_viewsyng_gabainame.configure(foreground="#778899")
        self.Label_viewsyng_gabainame.configure(highlightbackground="#f6f7f9")
        self.Label_viewsyng_gabainame.configure(text='''Gabai name''')
        self.Label_viewsyng_gabaiphone = tk.Label(self)
        self.Label_viewsyng_gabaiphone.place(relx=0.067, rely=0.422, height=41
                                             , width=109)
        self.Label_viewsyng_gabaiphone.configure(activebackground="#ffffff")
        self.Label_viewsyng_gabaiphone.configure(anchor='w')
        self.Label_viewsyng_gabaiphone.configure(background="#f6f7f9")
        self.Label_viewsyng_gabaiphone.configure(compound='center')
        self.Label_viewsyng_gabaiphone.configure(disabledforeground="#b9b9bb")
        self.Label_viewsyng_gabaiphone.configure(font="-family {DejaVu Sans} -size 12")
        self.Label_viewsyng_gabaiphone.configure(foreground="#778899")
        self.Label_viewsyng_gabaiphone.configure(highlightbackground="#f6f7f9")
        self.Label_viewsyng_gabaiphone.configure(text='''Gabai phone''')
        self.Label_viewsyng_prayers = tk.Label(self)
        self.Label_viewsyng_prayers.place(relx=0.067, rely=0.53, height=41
                                          , width=109)
        self.Label_viewsyng_prayers.configure(activebackground="#ffffff")
        self.Label_viewsyng_prayers.configure(anchor='w')
        self.Label_viewsyng_prayers.configure(background="#f6f7f9")
        self.Label_viewsyng_prayers.configure(compound='center')
        self.Label_viewsyng_prayers.configure(disabledforeground="#b9b9bb")
        self.Label_viewsyng_prayers.configure(font="-family {DejaVu Sans} -size 12")
        self.Label_viewsyng_prayers.configure(foreground="#778899")
        self.Label_viewsyng_prayers.configure(highlightbackground="#f6f7f9")
        self.Label_viewsyng_prayers.configure(text='''Prayers''')
        self.TCombobox_viewsyng_nosah = ttk.Combobox(self)
        self.TCombobox_viewsyng_nosah.place(relx=0.367, rely=0.157
                                            , relheight=0.046, relwidth=0.595)
        self.TCombobox_viewsyng_nosah.configure(textvariable=self.combobox)
        self.TCombobox_viewsyng_nosah.configure(takefocus="")
        self.TCombobox_viewsyng_city = ttk.Combobox(self)
        self.TCombobox_viewsyng_city.place(relx=0.367, rely=0.245
                                           , relheight=0.046, relwidth=0.595)
        self.TCombobox_viewsyng_city.configure(textvariable=self.combobox)
        self.TCombobox_viewsyng_city.configure(takefocus="")
        self.TEntry_viewsyng_gabainame = ttk.Entry(self)
        self.TEntry_viewsyng_gabainame.place(relx=0.333, rely=0.333
                                             , relheight=0.046, relwidth=0.623)
        self.TEntry_viewsyng_gabainame.configure(takefocus="")
        self.TEntry_viewsyng_gabainame.configure(cursor="fleur")
        self.TEntry_viewsyng_gabaiphone = ttk.Entry(self)
        self.TEntry_viewsyng_gabaiphone.place(relx=0.333, rely=0.422
                                              , relheight=0.046, relwidth=0.623)
        self.TEntry_viewsyng_gabaiphone.configure(takefocus="")
        self.TEntry_viewsyng_gabaiphone.configure(cursor="fleur")
        self.Scrolledtext1 = ScrolledText(self)
        self.Scrolledtext1.place(relx=0.25, rely=0.532, relheight=0.338
                                 , relwidth=0.72)
        self.Scrolledtext1.configure(background="white")
        self.Scrolledtext1.configure(font="TkTextFont")
        self.Scrolledtext1.configure(highlightbackground="#778899")
        self.Scrolledtext1.configure(insertborderwidth="3")
        self.Scrolledtext1.configure(selectbackground="#dedfe0")
        self.Scrolledtext1.configure(wrap="none")
        self.Button_viewsyng_save = tk.Button(self)
        self.Button_viewsyng_save.place(relx=0.417, rely=0.883, height=43
                                        , width=113)
        self.Button_viewsyng_save.configure(activebackground="#5faeb6")
        self.Button_viewsyng_save.configure(background="#778899")
        self.Button_viewsyng_save.configure(borderwidth="2")
        self.Button_viewsyng_save.configure(command=proj_support.save_syng)
        self.Button_viewsyng_save.configure(compound='left')
        self.Button_viewsyng_save.configure(disabledforeground="#b9b9bb")
        self.Button_viewsyng_save.configure(foreground="#f6f7f9")
        self.Button_viewsyng_save.configure(highlightbackground="#778899")
        self.Button_viewsyng_save.configure(relief="flat")
        self.Button_viewsyng_save.configure(text='''Save''')

        self.Button_viewsyng_back = tk.Button(self)
        self.Button_viewsyng_back.place(relx=0.0, rely=0.0, height=33, width=52)
        self.Button_viewsyng_back.configure(activebackground="#5faeb6")
        self.Button_viewsyng_back.configure(command=lambda: proj_support.goto(controller, "QuertPage"))
        self.Button_viewsyng_back.configure(background="#778899")
        self.Button_viewsyng_back.configure(borderwidth="2")
        self.Button_viewsyng_back.configure(compound='left')
        self.Button_viewsyng_back.configure(cursor="fleur")
        self.Button_viewsyng_back.configure(foreground="#f6f7f9")
        self.Button_viewsyng_back.configure(highlightbackground="#778899")
        self.Button_viewsyng_back.configure(relief="flat")
        self.Button_viewsyng_back.configure(text='''Back''')