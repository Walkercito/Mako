import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

from ui import MakacoUI

import sv_ttk


class SplashScreen:
    def __init__(self, parent):
        self.parent = parent
        self.splash = tk.Toplevel(parent)
        self.splash.title("Makaco - Cargando")
        self.splash.geometry("1220x660")
        self.splash.resizable(False, False)

        self.label = ttk.Label(self.splash, text="SaverDuo", font=("YouTube Sans", 40, "bold"), foreground="cyan")
        self.label.pack(pady=150, expand = True)

        self.progress = ttk.Progressbar(self.splash, orient = "horizontal", length = 350, mode = "indeterminate", style = "Custom.Horizontal.TProgressbar",)
        self.progress.pack(pady=30, side = 'bottom')
        self.progress.start(10)

        self.thread = threading.Thread(target=self.check_internet)
        self.thread.start()

        self.parent.withdraw()

    def check_internet(self):
        try:
            urllib.request.urlopen("http://google.com")
            self.label.configure(text="Makaco")
        except:
            self.label.configure(text="No hay conexión a Internet", foreground = 'red')

        self.progress.stop()
        self.progress.destroy()
        self.splash.after(2000, self.close_splash)

    def close_splash(self):
        self.splash.destroy()
        self.parent.deiconify()


class Makaco:
    def __init__(self, master):
        self.master = master
        self.master.title('Makaco')
        self.master.iconbitmap('')
        self.master.minsize(1220, 660)
        sv_ttk.set_theme('dark')

        self.ui = MakacoUI(self.master)
        self.ui.pack()

        self.my_font = Font(family="YouTube Sans")
        self.version_label()

    def version_label(self):
        self.my_font.configure(family="YouTube Sans", size=13)
        version = ttk.Label(self.master, text = 'v0.1-alpha', padding = 10, font = self.my_font, style = "Version.TLabel")
        version.place(relx=1.0, rely=1.0, anchor="se", bordermode="outside")


if __name__ == '__main__':
    import threading
    import urllib.request

    root = tk.Tk()
    splash = SplashScreen(root)
    app = Makaco(root)
    root.mainloop()