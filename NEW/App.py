import tkinter as tk  # python 3
from tkinter import font as tkfont  # python 3

from UI.LoginPage import LoginPage
from UI.MainPage import MainPage
from UI.ManageGabaiPage import ManageGabaiPage
from UI.ManageSyngPage import ManageSyngPage
from UI.QueryPage import QueryPage
from UI.SetUpPage import SetUpPage
from UI.ViewGabaiPage import ViewGabaiPage
from UI.ViewSyngPage import ViewSyngPage


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.connection = None

        self.gabai = None
        self.syng_list = None
        self.gabai_list = None
        self.syng_to_view = None
        self.gabai_to_view = None
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (
                ViewSyngPage, ManageSyngPage, ManageGabaiPage, QueryPage, MainPage, LoginPage, SetUpPage,
                ViewGabaiPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("SetUpPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        if page_name in ("MainPage", "ManageSyngPage", "ViewSyngPage", "ManageGabaiPage", "ViewGabaiPage", "QueryPage"):
            frame.update()
        frame.tkraise()


def close_window():
    try:
        app.connection.close()
    except:pass
    app.destroy()
    print("App closed")


if __name__ == "__main__":
    app = App()
    app.protocol("WM_DELETE_WINDOW", close_window)
    app.configure(bg="#f6f7f9")
    app.title("App")
    try:
        app.mainloop()
    except:
        close_window()
