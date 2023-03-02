#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 7.6
#  in conjunction with Tcl version 8.6
#    Feb 28, 2023 11:07:08 AM IST  platform: Linux

import sys
from tkinter import ttk, ANCHOR, END

import UDPclient
from DNSclient import sendDNS
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
    print("id: " + mID + "\npassword: " + mPassword)
    ans = UDPclient.send_login(('127.0.0.1', 6666), mID, mPassword)

    if ans == 'wrong_password':
        print("[!] wrong password")
    elif ans == 'wrong_id':
        print("[!] wrong id")
    else:
        print("[+] current")
        goto(controller, "MainPage")
        controller.gabai = Gabai.fromJSON(ans)


def goto_manage_gabai(controller):
    # print("password: " + controller.gabai.password)
    # if controller.gabai is None:
    #     print("[!] not have premssion")
    #     return
    # goto(controller, "ManageSyngPage")
    pass


def goto_manage_syng(controller):
    if controller.gabai is None:
        print("[!] not have premssion")
        return
    goto(controller, "ManageSyngPage")


def send_query(controller, name, nosah, city, Scrolledlistbox_query: ScrolledListBox):
    Scrolledlistbox_query.delete(0, END)
    controller.syng_list = []
    ans = UDPclient.send_by_query(('127.0.0.1', 6666), name, nosah.value, city.value)
    if ans is None:
        print("[!] dosent have much")
        return
    for iteam in ans:
        ad = Synagogue.fromJSON(iteam)
        Scrolledlistbox_query.insert(END, ad.name)
        controller.syng_list.append(ad)


def view_syng(controller, Scrolledlistbox_query):
    if controller.syng_list is None: return None
    controller.syng_to_view = None
    for x in controller.syng_list:
        if x.name == Scrolledlistbox_query.get(ANCHOR):
            controller.syng_to_view = x
            break
    if controller.syng_to_view is not None:
        goto(controller, "ViewSyngPage")


def add_syng(controller):
    controller.syng_to_view = Synagogue("", 0, Nosah.NULL, City.NULL, "", controller.gabai)
    goto(controller, "ViewSyngPage")


def del_syng(*args):
    if _debug:
        print('proj_support.del_syng')
        for arg in args:
            print('    another arg:', arg)
        sys.stdout.flush()


def edit_syng(controller, Scrolledlistbox_mngabai: ScrolledListBox):
    print(Scrolledlistbox_mngabai.get(ANCHOR))


def get_gabai(*args):
    if _debug:
        print('proj_support.get_gabai')
        for arg in args:
            print('    another arg:', arg)
        sys.stdout.flush()


def save_syng(controller, syng_to_edit):
    ans = (UDPclient.send_add_syng(('127.0.0.1', 6666), syng_to_edit))
    ans = int(ans)
    if ans != -1:
        controller.gabai.synagogue_list.append(ans)
    print(controller.gabai)
    goto(controller, "MainPage")


def diplay_syng_list(controller, Scrolledlistbox_mngsyng):
    Scrolledlistbox_mngsyng.delete(0, END)
    print(controller.gabai.synagogue_list)
    ans = UDPclient.send_request_by_ids(('127.0.0.1', 6666), controller.gabai.synagogue_list)
    if ans is None:
        print("[!] dosent have much")
        return
    for iteam in ans:
        ad = Synagogue.fromJSON(iteam)
        Scrolledlistbox_mngsyng.insert(0, ad.name)
