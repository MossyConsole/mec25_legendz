import tkinter as tk

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
        self.label_text.set("Button clicked!")

if __name__ == "__main__":
    root = tk.Tk()
    root.minsize(600, 400) 
    app = MyTkinterApp(root)
    root.mainloop()