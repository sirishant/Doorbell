# Access the ESP32-CAM after getting password and attempts
# to get 5 images from server, and calls /verify to actuate servo

from PIL import Image
import requests
from io import BytesIO
import time
import server
import urllib.request

def getCreds():
    pw, conf = server.getPassword()
    addr, _ = conf
    time.sleep(.5)
    return (addr, pw)

def accessCam(addr, pw):
        print("Trying to log in accessCam...")
        #time.sleep(.5)
        login = requests.get(f"http://{addr}/login/{pw}")
        print("Logged in! Geting images..")
        for i in range(5):
                response = requests.get(f"http://{addr}/foto")
                img = BytesIO(response.content)

                with open(f"output{i}.jpeg", "wb") as f:
                        f.write(img.getbuffer())
                
                # Rotate image
                im = Image.open(f"output{i}.jpeg")
                im = im.rotate(270, expand=True)
                im.save(f'output{i}.jpeg')

                time.sleep(.25)

def openLock(addr, pw):
    login = requests.get(f"http://{addr}/login/{pw}")
    time.sleep(.5)
    try:
        verify = urllib.request.urlopen(url=f"http://{addr}/verify")
        return
    except Exception:
        return

