#! Python
# Opens a web browser with weather based off of your current location

import webbrowser as w
import geocoder as g


my_loc = g.ip('me').latlng
rnd_loc = [str(round(i, ndigits=2)) for i in my_loc]

w.open("https://google.com")
w.open(f"https://weather.com/weather/today/l/{','.join(rnd_loc)}")

