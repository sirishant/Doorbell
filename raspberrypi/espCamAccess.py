# Access the ESP32-CAM after getting password and attempts
# to get 5 images from server, and calls /verify to actuate servo

from PIL import Image
import requests
from io import BytesIO
import time
import server
import urllib.request

def accessCam():
        pw, conf = server.getPassword()
        addr, _ = conf
        time.sleep(.5)
        login = requests.get(f"http://{addr}/login/{pw}")
        time.sleep(.5)

        for i in range(5):
                response = requests.get(f"http://{addr}/foto")
                img = BytesIO(response.content)

                with open(f"output{i}.jpeg", "wb") as f:
                        f.write(img.getbuffer())

                time.sleep(1)

        print("hellooooooooooo")
        try:
                verify = urllib.request.urlopen(url=f"http://{addr}/verify")
                return
        except Exception:
                return
