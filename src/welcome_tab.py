import tkinter as tk
import geocoder
from geopy.geocoders import Nominatim

from tkinter import ttk


def welcome_tab(ttk, tab):
    ttk.Label(tab, 
            text = "Set Location", font=("Browallia new", 40)).pack(padx=100, pady=(0,100))


    # Create the buttons
    custom = tk.StringVar()
    locText = ttk.Label(tab, 
            text = "You Havent Set Your Location", font=("Browallia new", 16))
    locText.pack(padx=100, pady = 10)
    ttk.Button(tab, text="Use System Location", command=lambda : set_to_current(locText)).pack(padx = "100", pady = 10)
    ttk.Button(tab, text="Use Custom Location", command=lambda : set_to_custom(custom, locText)).pack(padx = "100", pady = 10)
    nty = ttk.Entry(tab, textvariable=custom, width=100)
    nty.pack(padx = "200", pady = 10)
    nty.insert(0, "City, Province/State, Country...")
    nty.config(foreground='grey')

    def on_focus_in(event):
        print(nty.cget('foreground'))
        if str(nty.cget('foreground')) == 'grey':
            nty.delete(0, tk.END)
            nty.config(foreground='black')

    def on_focus_out(event):
        if not nty.get():
            nty.insert(0, "City, Province/State, Country")
            nty.config(foreground='grey')

    nty.bind("<FocusIn>", on_focus_in)
    nty.bind("<FocusOut>", on_focus_out)

    
def set_to_current(locText):
    g = geocoder.ip('me')
    latlng = g.latlng
    if (g.latlng == None):
        locText.config(text = "Couldnt't get address")
        return
    file = open("../sunny_data/location.txt", "w")
    file.write(str(latlng[0]))
    file.write(";")
    file.write(str(latlng[1]))
    file.close();
    locText.config(text = "Location set to: " + g.address)



def set_to_custom(custom, locText):
    loc = Nominatim(user_agent="SunnySide")
    getLoc = loc.geocode(custom.get())
    if (getLoc == None):
        locText.config(text = "Couldn't set location with input: " + custom.get())
        return
    file = open("location.txt", "w")
    file.write(str(getLoc.latitude))
    file.write(";")
    file.write(str(getLoc.longitude))
    file.close();
    locText.config(text = "Location set to: " + getLoc.address)

