import tkinter as tk
from tkinter import ttk
import geocoder
from api_caller import Meteo_Caller, WeatherBit_Caller
from welcome_tab import welcome_tab

class MyTkinterApp:
    def __init__(self, root):
        self.root = root
        root.title("Weather App")

        tabControl = ttk.Notebook(root)

        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)

        tabControl.add(tab1, text ='Welcome')
        tabControl.add(tab2, text ='Tab 2')
        tabControl.pack(expand = 1, fill ="both")

        welcome_tab(ttk, tab1)

        ttk.Label(tab2,
            text ="Lets dive into the\
            world of computers").grid(column = 0,
                                    row = 0, 
                                    padx = 30,
                                    pady = 30)

        # self.label_text = tk.StringVar()
        # self.label_text.set("Natural Disaster Detector")

        # self.label = tk.Label(root, textvariable=self.label_text, font=("Arial", 16))
        # self.label.pack(pady=20)


    def on_button_click(self):
        api = Meteo_Caller()
        g = geocoder.ip('me')
        latlng = g.latlng
        self.label_text.set(api.request(latlng[0], latlng[1]))

if __name__ == "__main__":
    root = tk.Tk()
    root.minsize(600, 400) 
    app = MyTkinterApp(root)
    root.mainloop()