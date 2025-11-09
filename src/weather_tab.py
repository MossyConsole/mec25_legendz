import tkinter as tk
from tkinter import ttk
import json

mock_alert_json = '''{
    "alerts":[
        {
            "description":"* WHAT...Flooding caused by excessive rainfall is expected. * WHERE...A portion of east central Florida, including the following counties, Lake, Orange and Seminole.  * WHEN...Until 615 PM EDT.  * IMPACTS...Minor flooding in low-lying and poor drainage areas.  * ADDITIONAL DETAILS... - At 419 PM EDT, Doppler radar indicated heavy rain due to thunderstorms. Minor flooding is ongoing or expected to begin shortly in the advisory area. Between 1.5 and 3 inches of rain have fallen. - Additional rainfall amounts of 1 to 2 inches are expected over the area. This additional rain will result in minor flooding. - Some locations that will experience flooding include... Orlando, Sanford, Apopka, Altamonte Springs, Winter Springs, Casselberry, Maitland, Lake Mary, Longwood, Lockhart, Mount Plymouth, Cassia, Zellwood, Pine Hills, Wekiwa Springs State Park, Wekiva Springs, Forest City, Fern Park, Sorrento and Fairview Shores. - http://www.weather.gov/safety/flood",
            "effective_local":"2024-08-22T16:19:00",
            "effective_utc":"2024-08-22T20:19:00",
            "ends_local":"2024-08-22T18:15:00",
            "ends_utc":"2024-08-22T22:15:00",
            "expires_local":"2024-08-22T18:15:00",
            "expires_utc":"2024-08-22T22:15:00",
            "onset_local":"2024-08-22T16:19:00",
            "onset_utc":"2024-08-22T20:19:00",
            "regions":[
            "Lake, FL",
            " Orange, FL",
            " Seminole, FL"
            ],
            "severity":"Advisory",
            "title":"Flood Advisory issued August 22 at 4:19PM EDT until August 22 at 6:15PM EDT by NWS Melbourne FL",
            "uri":"https://api.weather.gov/alerts/urn:oid:2.49.0.1.840.0.9079ecdac4135d19817f4fd0647a7493256e5c34.001.1"
        }
    ],
    "city_name":"Orlando",
    "country_code":"US",
    "lat":28.5384,
    "lon":-81.3789,
    "state_code":"FL",
    "timezone":"America/New_York"
}'''

def weather_tab(ttk, tab):

    # Grab JSON Data from API
    json_data = mock_alert_json
    
    # Load JSON Data from API return
    data = json.loads(json_data)
    # print(data["alerts"])

    # Parse and deal with data
    ttk.Label(tab, text = f"{data["city_name"]}, {data["country_code"]}", 
              font = ("Brownallia New", 16, "bold")).pack(padx=10, pady=10)
    ttk.Label(tab, text = "Alerts:", font = ("Browallia New", 16, "bold")).pack(padx=10, pady=10)

    alerts = data["alerts"] 
    if (len(alerts) != 0):
        for alert in alerts:

            # Pre-process regions to a good string
            regions_str = ""
            for region in alert["regions"]:
                regions_str += f"\n\t\t{region.strip()}"

            # Pro-process desc to a good string
            desc = alert["description"]
            desc = desc.split("*")
            for str_index in range(len(desc)):
                string = desc[str_index]
                lim = 200
                if len(string) >= lim:
                    space_lim = string.rfind(" ", 0, lim)
                    desc.insert(str_index, string[0:space_lim])
                    desc[str_index+1] = string[lim+1:]

            desc_str = ""
            for desc_str_part in desc:
                desc_str += f"\t{desc_str_part}\n"

            show_str = f"""
                        {alert["title"]}\n
                        Severity: {alert["severity"]}\n
                        Regions:{regions_str}
                        {desc_str}"""
        
            ttk.Label(tab, text = show_str).pack(padx=10, pady=10)

    else:
        ttk.Label(tab, text = "None. Have a Sunny Day.").pack(padx=10, pady=10)
    