#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.6
#  in conjunction with Tcl version 8.6
#    Feb 28, 2023 11:05:26 AM IST  platform: Linux

import sys
import tkinter as tk
import tkinter.ttk as ttk
import os.path

_script = sys.argv[0]
_location = os.path.dirname(_script)

import proj_support

_bgcolor = '#778899'  # X11 color: '{light slate gray}'
_fgcolor = '#f6f7f9'  # Closest X11 color: 'gray97'
_compcolor = '#f9f8f7' # Closest X11 color: 'gray97'
_ana1color = '#f7f7f9' # Closest X11 color: 'gray97'
_ana2color = 'beige' # X11 color: #f5f5dc
_tabfg1 = 'black' 
_tabfg2 = 'black' 
_tabbg1 = 'grey75' 
_tabbg2 = 'grey89' 
_bgmode = 'light' 

_style_code_ran = 0
def _style_code():
    global _style_code_ran
    if _style_code_ran:
       return
    style = ttk.Style()
    if sys.platform == "win32":
       style.theme_use('winnative')
    style.configure('.',background=_bgcolor)
    style.configure('.',foreground=_fgcolor)
    style.configure('.',font='TkDefaultFont')
    style.map('.',background =
       [('selected', _compcolor), ('active',_ana2color)])
    if _bgmode == 'dark':
       style.map('.',foreground =
         [('selected', 'white'), ('active','white')])
    else:
       style.map('.',foreground =
         [('selected', 'black'), ('active','black')])
    style.configure('Vertical.TScrollbar',  background=_bgcolor,arrowcolor= _fgcolor)

    style.configure('Horizontal.TScrollbar',  background=_bgcolor,arrowcolor= _fgcolor)
    _style_code_ran = 1

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("600x450+945+434")
        top.minsize(1, 1)
        top.maxsize(1905, 1050)
        top.resizable(1,  1)
        top.name("setup")
        top.configure(background="#f6f7f9")
        top.configure(highlightbackground="#f6f7f9")
        top.configure(highlightcolor="black")

        self.top = top

        self.Button_setup_connect = tk.Button(self.top)
        self.Button_setup_connect.place(relx=0.417, rely=0.578, height=43
                , width=113)
        self.Button_setup_connect.configure(activebackground="#5faeb6")
        self.Button_setup_connect.configure(background="#778899")
        self.Button_setup_connect.configure(borderwidth="2")
        self.Button_setup_connect.configure(command=proj_support.connect)
        self.Button_setup_connect.configure(compound='left')
        self.Button_setup_connect.configure(disabledforeground="#b9b9bb")
        self.Button_setup_connect.configure(foreground="#f6f7f9")
        self.Button_setup_connect.configure(highlightbackground="#778899")
        self.Button_setup_connect.configure(relief="flat")
        self.Button_setup_connect.configure(text='''Connect''')
        self.Label_setup_title = tk.Label(self.top)
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
        self.Label_DHCP_adress = tk.Label(self.top)
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
        self.Label_DHCP_adress.configure(text='''DHCP server adress''')
        _style_code()
        self.TEntry_DHCP_addres = ttk.Entry(self.top)
        self.TEntry_DHCP_addres.place(relx=0.45, rely=0.356, relheight=0.069
                , relwidth=0.423)
        self.TEntry_DHCP_addres.configure(takefocus="")
        self.TEntry_DHCP_addres.configure(cursor="xterm")
        self.Log_setup = tk.Text(self.top)
        self.Log_setup.place(relx=0.117, rely=0.756, relheight=0.209
                , relwidth=0.793)
        self.Log_setup.configure(background="white")
        self.Log_setup.configure(font="TkTextFont")
        self.Log_setup.configure(highlightbackground="#778899")
        self.Log_setup.configure(selectbackground="#dedfe0")
        self.Log_setup.configure(wrap="none")

class LoginPage:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("600x450+378+103")
        top.minsize(1, 1)
        top.maxsize(1905, 1050)
        top.resizable(1,  1)
        top.name("login")
        top.configure(background="#f6f7f9")
        top.configure(highlightbackground="#f6f7f9")
        top.configure(highlightcolor="black")

        self.top = top

        self.Label_login_title = tk.Label(self.top)
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
        self.Label_ID = tk.Label(self.top)
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
        self.Label_Password = tk.Label(self.top)
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
        self.TEntry_login_ID = ttk.Entry(self.top)
        self.TEntry_login_ID.place(relx=0.467, rely=0.267, relheight=0.069
                , relwidth=0.423)
        self.TEntry_login_ID.configure(takefocus="")
        self.TEntry_login_ID.configure(cursor="xterm")
        self.TEntry_login_Password = ttk.Entry(self.top)
        self.TEntry_login_Password.place(relx=0.467, rely=0.378, relheight=0.069
                , relwidth=0.423)
        self.TEntry_login_Password.configure(takefocus="")
        self.TEntry_login_Password.configure(cursor="xterm")
        self.Button_login_gabai = tk.Button(self.top)
        self.Button_login_gabai.place(relx=0.583, rely=0.556, height=43
                , width=113)
        self.Button_login_gabai.configure(activebackground="#5faeb6")
        self.Button_login_gabai.configure(background="#778899")
        self.Button_login_gabai.configure(borderwidth="2")
        self.Button_login_gabai.configure(command=proj_support.connect)
        self.Button_login_gabai.configure(compound='left')
        self.Button_login_gabai.configure(disabledforeground="#b9b9bb")
        self.Button_login_gabai.configure(foreground="#f6f7f9")
        self.Button_login_gabai.configure(highlightbackground="#778899")
        self.Button_login_gabai.configure(relief="flat")
        self.Button_login_gabai.configure(text='''Login as gabai''')
        self.menubar = tk.Menu(top,font="TkMenuFont",bg='#d9d9d9',fg='#000000')
        top.configure(menu = self.menubar)

        self.Button_login_guest = tk.Button(self.top)
        self.Button_login_guest.place(relx=0.25, rely=0.556, height=43
                , width=113)
        self.Button_login_guest.configure(activebackground="#5faeb6")
        self.Button_login_guest.configure(background="#778899")
        self.Button_login_guest.configure(borderwidth="2")
        self.Button_login_guest.configure(command=proj_support.login_guest)
        self.Button_login_guest.configure(compound='left')
        self.Button_login_guest.configure(disabledforeground="#b9b9bb")
        self.Button_login_guest.configure(foreground="#f6f7f9")
        self.Button_login_guest.configure(highlightbackground="#778899")
        self.Button_login_guest.configure(relief="flat")
        self.Button_login_guest.configure(text='''Login as guest''')
        self.Log_login = tk.Text(self.top)
        self.Log_login.place(relx=0.133, rely=0.756, relheight=0.209
                , relwidth=0.793)
        self.Log_login.configure(background="white")
        self.Log_login.configure(font="TkTextFont")
        self.Log_login.configure(highlightbackground="#778899")
        self.Log_login.configure(selectbackground="#dedfe0")
        self.Log_login.configure(wrap="none")

class MainPage:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("600x450+1215+115")
        top.minsize(1, 1)
        top.maxsize(1905, 1050)
        top.resizable(1,  1)
        top.name("main")
        top.configure(background="#f6f7f9")
        top.configure(highlightbackground="#f6f7f9")
        top.configure(highlightcolor="black")

        self.top = top

        self.Button_main_query = tk.Button(self.top)
        self.Button_main_query.place(relx=0.367, rely=0.178, height=43
                , width=143)
        self.Button_main_query.configure(activebackground="#5faeb6")
        self.Button_main_query.configure(background="#778899")
        self.Button_main_query.configure(borderwidth="2")
        self.Button_main_query.configure(command=proj_support.send_query)
        self.Button_main_query.configure(compound='left')
        self.Button_main_query.configure(disabledforeground="#b9b9bb")
        self.Button_main_query.configure(foreground="#f6f7f9")
        self.Button_main_query.configure(highlightbackground="#778899")
        self.Button_main_query.configure(relief="flat")
        self.Button_main_query.configure(text='''Query''')
        self.Button_main_manage_syn = tk.Button(self.top)
        self.Button_main_manage_syn.place(relx=0.367, rely=0.333, height=43
                , width=143)
        self.Button_main_manage_syn.configure(activebackground="#5faeb6")
        self.Button_main_manage_syn.configure(background="#778899")
        self.Button_main_manage_syn.configure(borderwidth="2")
        self.Button_main_manage_syn.configure(command=proj_support.manage_syng)
        self.Button_main_manage_syn.configure(compound='left')
        self.Button_main_manage_syn.configure(disabledforeground="#b9b9bb")
        self.Button_main_manage_syn.configure(foreground="#f6f7f9")
        self.Button_main_manage_syn.configure(highlightbackground="#778899")
        self.Button_main_manage_syn.configure(relief="flat")
        self.Button_main_manage_syn.configure(text='''Manage synagogue''')
        self.Button_main_manag_gab = tk.Button(self.top)
        self.Button_main_manag_gab.place(relx=0.367, rely=0.489, height=43
                , width=143)
        self.Button_main_manag_gab.configure(activebackground="#5faeb6")
        self.Button_main_manag_gab.configure(background="#778899")
        self.Button_main_manag_gab.configure(borderwidth="2")
        self.Button_main_manag_gab.configure(command=proj_support.manage_gabai)
        self.Button_main_manag_gab.configure(compound='left')
        self.Button_main_manag_gab.configure(disabledforeground="#b9b9bb")
        self.Button_main_manag_gab.configure(foreground="#f6f7f9")
        self.Button_main_manag_gab.configure(highlightbackground="#778899")
        self.Button_main_manag_gab.configure(relief="flat")
        self.Button_main_manag_gab.configure(text='''Manage gabaies''')

class QueryPage:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("600x455+469+553")
        top.minsize(1, 1)
        top.maxsize(1905, 1050)
        top.resizable(1,  1)
        top.name("query")
        top.configure(background="#f6f7f9")
        top.configure(highlightbackground="#f6f7f9")
        top.configure(highlightcolor="black")

        self.top = top
        self.combobox = tk.StringVar()

        _style_code()
        self.Scrolledlistbox_query = ScrolledListBox(self.top)
        self.Scrolledlistbox_query.place(relx=0.033, rely=0.308, relheight=0.642
                , relwidth=0.943)
        self.Scrolledlistbox_query.configure(background="white")
        self.Scrolledlistbox_query.configure(cursor="xterm")
        self.Scrolledlistbox_query.configure(disabledforeground="#b9b9bb")
        self.Scrolledlistbox_query.configure(font="TkFixedFont")
        self.Scrolledlistbox_query.configure(highlightbackground="#f6f7f9")
        self.Scrolledlistbox_query.configure(highlightcolor="#778899")
        self.Scrolledlistbox_query.configure(selectbackground="#dedfe0")
        self.TCombobox_query_city = ttk.Combobox(self.top)
        self.TCombobox_query_city.place(relx=0.5, rely=0.176, relheight=0.046
                , relwidth=0.245)
        self.TCombobox_query_city.configure(textvariable=self.combobox)
        self.TCombobox_query_city.configure(takefocus="")
        self.TCombobox_query_nosah = ttk.Combobox(self.top)
        self.TCombobox_query_nosah.place(relx=0.15, rely=0.176, relheight=0.046
                , relwidth=0.212)
        self.TCombobox_query_nosah.configure(textvariable=self.combobox)
        self.TCombobox_query_nosah.configure(takefocus="")
        self.TEntry_query_query = ttk.Entry(self.top)
        self.TEntry_query_query.place(relx=0.183, rely=0.066, relheight=0.046
                , relwidth=0.74)
        self.TEntry_query_query.configure(takefocus="")
        self.TEntry_query_query.configure(cursor="xterm")
        self.Label_query_query = tk.Label(self.top)
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
        self.Label_query_nosah = tk.Label(self.top)
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
        self.Label_query_city = tk.Label(self.top)
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
        self.Button_query_search = tk.Button(self.top)
        self.Button_query_search.place(relx=0.767, rely=0.176, height=43
                , width=113)
        self.Button_query_search.configure(activebackground="#5faeb6")
        self.Button_query_search.configure(background="#778899")
        self.Button_query_search.configure(borderwidth="2")
        self.Button_query_search.configure(command=proj_support.send_query)
        self.Button_query_search.configure(compound='left')
        self.Button_query_search.configure(disabledforeground="#b9b9bb")
        self.Button_query_search.configure(foreground="#f6f7f9")
        self.Button_query_search.configure(highlightbackground="#778899")
        self.Button_query_search.configure(relief="flat")
        self.Button_query_search.configure(text='''Search''')

class ManageSyngPage:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("600x450+718+577")
        top.minsize(1, 1)
        top.maxsize(1905, 1050)
        top.resizable(1,  1)
        top.name("manage synagogue")
        top.configure(background="#f6f7f9")

        self.top = top

        _style_code()
        self.Scrolledlistbox_mngsyng = ScrolledListBox(self.top)
        self.Scrolledlistbox_mngsyng.place(relx=0.083, rely=0.111
                , relheight=0.551, relwidth=0.827)
        self.Scrolledlistbox_mngsyng.configure(background="white")
        self.Scrolledlistbox_mngsyng.configure(cursor="xterm")
        self.Scrolledlistbox_mngsyng.configure(disabledforeground="#b9b9bb")
        self.Scrolledlistbox_mngsyng.configure(font="TkFixedFont")
        self.Scrolledlistbox_mngsyng.configure(highlightbackground="#f6f7f9")
        self.Scrolledlistbox_mngsyng.configure(highlightcolor="#778899")
        self.Scrolledlistbox_mngsyng.configure(selectbackground="#dedfe0")
        self.Button_mngsyng_add = tk.Button(self.top)
        self.Button_mngsyng_add.place(relx=0.1, rely=0.778, height=43, width=143)

        self.Button_mngsyng_add.configure(activebackground="#5faeb6")
        self.Button_mngsyng_add.configure(background="#778899")
        self.Button_mngsyng_add.configure(borderwidth="2")
        self.Button_mngsyng_add.configure(command=proj_support.add_syng)
        self.Button_mngsyng_add.configure(compound='left')
        self.Button_mngsyng_add.configure(disabledforeground="#b9b9bb")
        self.Button_mngsyng_add.configure(foreground="#f6f7f9")
        self.Button_mngsyng_add.configure(highlightbackground="#778899")
        self.Button_mngsyng_add.configure(relief="flat")
        self.Button_mngsyng_add.configure(text='''Add''')
        self.Button_mngsyng_edit = tk.Button(self.top)
        self.Button_mngsyng_edit.place(relx=0.383, rely=0.778, height=43
                , width=143)
        self.Button_mngsyng_edit.configure(activebackground="#5faeb6")
        self.Button_mngsyng_edit.configure(background="#778899")
        self.Button_mngsyng_edit.configure(borderwidth="2")
        self.Button_mngsyng_edit.configure(command=proj_support.edit_syng)
        self.Button_mngsyng_edit.configure(compound='left')
        self.Button_mngsyng_edit.configure(disabledforeground="#b9b9bb")
        self.Button_mngsyng_edit.configure(foreground="#f6f7f9")
        self.Button_mngsyng_edit.configure(highlightbackground="#778899")
        self.Button_mngsyng_edit.configure(relief="flat")
        self.Button_mngsyng_edit.configure(text='''Edit''')
        self.Button_mngsyng_del = tk.Button(self.top)
        self.Button_mngsyng_del.place(relx=0.667, rely=0.778, height=43
                , width=143)
        self.Button_mngsyng_del.configure(activebackground="#5faeb6")
        self.Button_mngsyng_del.configure(background="#778899")
        self.Button_mngsyng_del.configure(borderwidth="2")
        self.Button_mngsyng_del.configure(command=proj_support.del_syng)
        self.Button_mngsyng_del.configure(compound='left')
        self.Button_mngsyng_del.configure(cursor="fleur")
        self.Button_mngsyng_del.configure(disabledforeground="#b9b9bb")
        self.Button_mngsyng_del.configure(foreground="#f6f7f9")
        self.Button_mngsyng_del.configure(highlightbackground="#778899")
        self.Button_mngsyng_del.configure(relief="flat")
        self.Button_mngsyng_del.configure(text='''Del''')

class ViewSungPage:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("600x453+1122+393")
        top.minsize(1, 1)
        top.maxsize(1905, 1050)
        top.resizable(1,  1)
        top.name("view synagogue")
        top.configure(background="#f6f7f9")

        self.top = top
        self.combobox = tk.StringVar()

        self.Label_viewsyng_name = tk.Label(self.top)
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
        self.TEntry_viewsyng_name = ttk.Entry(self.top)
        self.TEntry_viewsyng_name.place(relx=0.267, rely=0.066, relheight=0.046
                , relwidth=0.69)
        self.TEntry_viewsyng_name.configure(takefocus="")
        self.TEntry_viewsyng_name.configure(cursor="fleur")
        self.Label_viewsyng_nosah = tk.Label(self.top)
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
        self.Label_viewsyng_city = tk.Label(self.top)
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
        self.Label_viewsyng_gabainame = tk.Label(self.top)
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
        self.Label_viewsyng_gabaiphone = tk.Label(self.top)
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
        self.Label_viewsyng_prayers = tk.Label(self.top)
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
        self.TCombobox_viewsyng_nosah = ttk.Combobox(self.top)
        self.TCombobox_viewsyng_nosah.place(relx=0.367, rely=0.157
                , relheight=0.046, relwidth=0.595)
        self.TCombobox_viewsyng_nosah.configure(textvariable=self.combobox)
        self.TCombobox_viewsyng_nosah.configure(takefocus="")
        self.TCombobox_viewsyng_city = ttk.Combobox(self.top)
        self.TCombobox_viewsyng_city.place(relx=0.367, rely=0.245
                , relheight=0.046, relwidth=0.595)
        self.TCombobox_viewsyng_city.configure(textvariable=self.combobox)
        self.TCombobox_viewsyng_city.configure(takefocus="")
        self.TEntry_viewsyng_gabainame = ttk.Entry(self.top)
        self.TEntry_viewsyng_gabainame.place(relx=0.333, rely=0.333
                , relheight=0.046, relwidth=0.623)
        self.TEntry_viewsyng_gabainame.configure(takefocus="")
        self.TEntry_viewsyng_gabainame.configure(cursor="fleur")
        self.TEntry_viewsyng_gabaiphone = ttk.Entry(self.top)
        self.TEntry_viewsyng_gabaiphone.place(relx=0.333, rely=0.422
                , relheight=0.046, relwidth=0.623)
        self.TEntry_viewsyng_gabaiphone.configure(takefocus="")
        self.TEntry_viewsyng_gabaiphone.configure(cursor="fleur")
        self.Scrolledtext1 = ScrolledText(self.top)
        self.Scrolledtext1.place(relx=0.25, rely=0.532, relheight=0.338
                , relwidth=0.72)
        self.Scrolledtext1.configure(background="white")
        self.Scrolledtext1.configure(font="TkTextFont")
        self.Scrolledtext1.configure(highlightbackground="#778899")
        self.Scrolledtext1.configure(insertborderwidth="3")
        self.Scrolledtext1.configure(selectbackground="#dedfe0")
        self.Scrolledtext1.configure(wrap="none")
        self.Button_viewsyng_save = tk.Button(self.top)
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

class ManageGabaiPage:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("600x450+745+485")
        top.minsize(1, 1)
        top.maxsize(1905, 1050)
        top.resizable(1,  1)
        top.name("manage gabai")
        top.configure(background="#f6f7f9")

        self.top = top

        _style_code()
        self.Scrolledlistbox_mngabai = ScrolledListBox(self.top)
        self.Scrolledlistbox_mngabai.place(relx=0.083, rely=0.089, relheight=0.64
                , relwidth=0.843)
        self.Scrolledlistbox_mngabai.configure(background="white")
        self.Scrolledlistbox_mngabai.configure(cursor="xterm")
        self.Scrolledlistbox_mngabai.configure(disabledforeground="#b9b9bb")
        self.Scrolledlistbox_mngabai.configure(font="TkFixedFont")
        self.Scrolledlistbox_mngabai.configure(highlightbackground="#f6f7f9")
        self.Scrolledlistbox_mngabai.configure(highlightcolor="#778899")
        self.Scrolledlistbox_mngabai.configure(selectbackground="#dedfe0")
        self.Button_mngabai_add = tk.Button(self.top)
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
        self.Button_mngabai_del = tk.Button(self.top)
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

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''
    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledText(AutoScroll, tk.Text):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

class ScrolledListBox(AutoScroll, tk.Listbox):
    '''A standard Tkinter Listbox widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)
    def size_(self):
        sz = tk.Listbox.size(self)
        return sz

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')
def start_up():
    proj_support.main()

if __name__ == '__main__':
    proj_support.main()




