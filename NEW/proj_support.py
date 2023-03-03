#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 7.6
#  in conjunction with Tcl version 8.6
#    Feb 28, 2023 11:07:08 AM IST  platform: Linux

import sys
from tkinter import ttk, ANCHOR, END, messagebox

import UDPclient
from ScrolledListBox import ScrolledListBox
from gabai import Gabai
from synagogue import Synagogue, Nosah, City

_debug = True  # False to eliminate debug printing from callback functions.

_bgcolor = '#778899'  # X11 color: '{light slate gray}'
_fgcolor = '#f6f7f9'  # Closest X11 color: 'gray97'
_compcolor = '#f9f8f7'  # Closest X11 color: 'gray97'
_ana1color = '#f7f7f9'  # Closest X11 color: 'gray97'
_ana2color = 'beige'  # X11 color: #f5f5dc
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
    style.configure('.', background=_bgcolor)
    style.configure('.', foreground=_fgcolor)
    style.configure('.', font='TkDefaultFont')
    style.map('.', background=
    [('selected', _compcolor), ('active', _ana2color)])
    if _bgmode == 'dark':
        style.map('.', foreground=
        [('selected', 'white'), ('active', 'white')])
    else:
        style.map('.', foreground=
        [('selected', 'black'), ('active', 'black')])
    style.configure('Vertical.TScrollbar', background=_bgcolor,
                    arrowcolor=_fgcolor)
    style.configure('Horizontal.TScrollbar', background=_bgcolor, arrowcolor=_fgcolor)
    _style_code_ran = 1


def goto(controller, to):
    controller.show_frame(to)


def connect(controller, domain):
    # ans = sendDNS(domain)
    # if ans is None:
    #     return
    # else:
    goto(controller, "LoginPage")


def login_guest(controller):
    controller.gabai = None
    goto(controller, "MainPage")


def login_gabai(controller, mID, mPassword):
    # print("id: " + mID + "\npassword: " + mPassword)
    ans = UDPclient.send_login(('127.0.0.1', 6666), mID, mPassword)
    if ans is None:
        messagebox.showinfo("Warning", "[!] bad connection")
    elif ans == 'wrong_password' or ans == 'wrong_id':
        messagebox.showinfo("Warning", "[!] wrong id or password")
    else:
        print("[+] current")
        controller.gabai = Gabai.fromJSON(ans)
        goto(controller, "MainPage")


def goto_manage_gabai(controller):
    if controller.gabai is None or controller.gabai.gabai_id != 1:
        messagebox.showinfo("Warning", "[!] only for admin")
        return
    goto(controller, "ManageGabaiPage")
    pass


def goto_manage_syng(controller):
    if controller.gabai is None:
        messagebox.showinfo("Warning", "[!] only for gabai")
        return
    goto(controller, "ManageSyngPage")


def send_query(controller, name, nosah, city, Scrolledlistbox_query: ScrolledListBox):
    Scrolledlistbox_query.delete(0, END)
    controller.syng_list = []
    ans = UDPclient.send_by_query(('127.0.0.1', 6666), name, nosah.value, city.value)
    if ans is None:
        messagebox.showinfo("Warning", "[!] No result")
        return
    for iteam in ans:
        ad = Synagogue.fromJSON(iteam)
        Scrolledlistbox_query.insert(END, str(ad.id_synagogue) + ":" + ad.name)
        controller.syng_list.append(ad)


def view_syng(controller, Scrolledlistbox_query):
    if controller.syng_list is None: return None
    controller.syng_to_view = None
    for x in controller.syng_list:
        if x.id_synagogue == int(Scrolledlistbox_query.get(ANCHOR).split(':')[0]):
            controller.syng_to_view = x
            break
    if controller.syng_to_view is not None:
        goto(controller, "ViewSyngPage")


def add_syng(controller):
    controller.syng_to_view = Synagogue("", 0, Nosah.NULL, City.NULL, "", controller.gabai)
    goto(controller, "ViewSyngPage")


def add_gabai(controller):
    controller.gabai_to_view = Gabai("", 0, "", "", [])
    goto(controller, "ViewGabaiPage")


def del_syng(controller, Scrolledlistbox_mngabai: ScrolledListBox):
    syng_to_del = None
    for x in controller.syng_list:
        if x.id_synagogue == int(Scrolledlistbox_mngabai.get(ANCHOR).split(':')[0]):
            syng_to_del = x
            syng_to_del.name = ""
            break
    ans = (UDPclient.send_edit_syng(('127.0.0.1', 6666), syng_to_del))
    ans = int(ans)
    if ans == 0:
        Scrolledlistbox_mngabai.delete(ANCHOR)
        controller.gabai.synagogue_list.remove(syng_to_del.id_synagogue)
        messagebox.showinfo("Message", "[!] Successful delete")
    if ans == -1:
        messagebox.showinfo("Warning", "[!] Failed delete")


def del_gabai(controller, Scrolledlistbox_mngabai):
    gabai_to_del = None
    for x in controller.gabai_list:
        if x.gabai_id == int(Scrolledlistbox_mngabai.get(ANCHOR).split(':')[0]):
            gabai_to_del = x
            gabai_to_del.name = ""
            break
    ans = (UDPclient.send_edit_gabai(('127.0.0.1', 6666), gabai_to_del))
    ans = int(ans)
    if ans == 0:
        Scrolledlistbox_mngabai.delete(ANCHOR)
        messagebox.showinfo("Message", "[!] Successful delete")
    if ans == -1:
        messagebox.showinfo("Warning", "[!] Failed delete")


def edit_syng(controller, Scrolledlistbox_mngabai: ScrolledListBox):
    controller.syng_to_view = None
    for x in controller.syng_list:
        if x.id_synagogue == int(Scrolledlistbox_mngabai.get(ANCHOR).split(':')[0]):
            controller.syng_to_view = x
            break
    goto(controller, "ViewSyngPage")


def edit_gabai(controller, Scrolledlistbox_mngabai):
    controller.gabai_to_view = None
    for x in controller.gabai_list:
        if x.gabai_id == int(Scrolledlistbox_mngabai.get(ANCHOR).split(':')[0]):
            controller.gabai_to_view = x
            break
    goto(controller, "ViewGabaiPage")


def save_syng(controller, syng_to_edit: Synagogue):
    ans = (UDPclient.send_edit_syng(('127.0.0.1', 6666), syng_to_edit))
    ans = int(ans)
    if ans != -1 and ans != 0:
        if ans not in controller.gabai.synagogue_list:
            controller.gabai.synagogue_list.append(ans)
    goto(controller, "MainPage")


def save_gabai(controller, gabai_to_edit: Gabai):
    if gabai_to_edit.gabai_id == 1:
        messagebox.showinfo("Warning", "[!] cant edit admin")
        return
    ans = (UDPclient.send_edit_gabai(('127.0.0.1', 6666), gabai_to_edit))
    ans = int(ans)
    # if ans != -1 and ans != 0:
    # controller.gabai.synagogue_list.append(ans)
    goto(controller, "MainPage")


def display_syng_list(controller, Scrolledlistbox_mngsyng):
    Scrolledlistbox_mngsyng.delete(0, END)
    # print(controller.gabai.synagogue_list)
    ans = UDPclient.send_request_by_ids(('127.0.0.1', 6666), controller.gabai.synagogue_list)
    controller.syng_list = []
    if ans is None:
        messagebox.showinfo("Warning", "[!] No result")
        return
    for item in ans:
        ad = Synagogue.fromJSON(item)
        Scrolledlistbox_mngsyng.insert(END, str(ad.id_synagogue) + ":" + ad.name)
        controller.syng_list.append(ad)


def display_gabai_list(controller, Scrolledlistbox_mngabai):
    Scrolledlistbox_mngabai.delete(0, END)
    # print(controller.gabai.synagogue_list)
    ans = UDPclient.send_request_all_gabai(('127.0.0.1', 6666))
    controller.gabai_list = []
    if ans is None:
        messagebox.showinfo("Warning", "[!] No result")
        return
    for item in ans:
        ad = Gabai.fromJSON(item)
        if ad.gabai_id == 1: continue
        Scrolledlistbox_mngabai.insert(END, str(ad.gabai_id) + ":" + ad.name)
        controller.gabai_list.append(ad)
