import tkinter as tk
import threading
import urllib.request

class SplashScreen:
    def __init__(self, parent):
        self.parent = parent
        self.splash = tk.Toplevel(parent)
        self.splash.title("Logo")
        self.splash.geometry("300x200")
        self.splash.resizable(False, False)
        
        # Agregar aquí el contenido de la pantalla de carga
        self.label = tk.Label(self.splash, text="Logo", font=("Arial", 24))
        self.label.pack(pady=50)
        
        # Verificar la conexión a Internet en segundo plano
        self.thread = threading.Thread(target=self.check_internet)
        self.thread.start()
        
        self.parent.withdraw()
    
    def check_internet(self):
        try:
            urllib.request.urlopen("http://youtube.com")
            self.label.config(text="Conexión exitosa")
        except:
            self.label.config(text="No hay conexión a Internet")
        
        self.splash.after(2000, self.close_splash)
    
    def close_splash(self):
        self.splash.destroy()
        self.parent.deiconify()

class App:
    def __init__(self, master):
        self.master = master
        self.master.title('Mi programa')
        self.master.geometry("500x500")
        
        # Agregar aquí el contenido de la ventana principal
        label = tk.Label(self.master, text="¡Hola, mundo!", font=("Arial", 24))
        label.pack(pady=50)

if __name__ == '__main__':
    root = tk.Tk()
    splash = SplashScreen(root)
    app = App(root)
    root.mainloop()