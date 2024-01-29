# RaspberryPi - ESP32Cam Communications

#### This document is concerned only with ESP32Cam-RPi communication.<br>
- For more info on RaspberryPi Processing, [refer here](/raspberrypi/README.md).
- For more info on ESP32Cam Processing, [refer here](/esp32Cam/README.md).

### Problem Statement
> Have a method to accept incoming communications from an ESP32Cam,
> and process information to manipulate the ESP32Cam accordingly.

### Goals
> Bind the ESP32Cam and access images to run facial recognition and
> authenticate the system accordingly.

### Non-Goals
> Actual dispensing of the machine, interaction with ESP32 non-cams of
> any machine, actual working of ESPCam.

### Proposed Solution
> Send IP Address and Port number of ESP32Cam to the static RaspberryPi
> server. Then bind the server to the ESP32Cam client. The Cam client
> then sends a response when a button is pressed. The RPi server then
> requests 5 images from the Cam, which is then saved on the server and
> facial recognition processing is done. 
> <br><br>
> The results of the facial recognition then allows for ‘verify’ to run
> when a face is matched. If no face matches, then it returns the Cam to
> original state without verification.

### High-Level Sequence Diagram
![ESP32Cam-RaspberryPi Communications Sequence Diagram](/assets/ESP32Cam-RPi-Sequence_Diagram.png)
