import tkinter as tk
import geocoder
from api_caller import Api_Caller

class MyTkinterApp:
    def __init__(self, master):
        self.master = master
        master.title("Weather App")

        self.label_text = tk.StringVar()
        self.label_text.set("Natural Disaster Detector")

        self.label = tk.Label(master, textvariable=self.label_text, font=("Arial", 16))
        self.label.pack(pady=20)

        self.button = tk.Button(master, text="Click Me", command=self.on_button_click)
        self.button.pack(pady=10)

    def on_button_click(self):
        api = Api_Caller()
        g = geocoder.ip('me')
        latlng = g.latlng
        self.label_text.set(api.request(latlng[0], latlng[1]))

if __name__ == "__main__":
    root = tk.Tk()
    root.minsize(600, 400) 
    app = MyTkinterApp(root)
    root.mainloop()