# RaspberryPi Processing

#### This document is concerned only with RaspberryPi Processing.<br>
- For more info on ESP32Cam Processing, [refer here](/esp32Cam/README.md).
- For more info on ESP32Cam-RaspberryPi Communications, [refer here](/README.md).

### Solution Description
> Receive connection from an ESP32Cam on the network through TCP. Authenticate
> by receiving password from the ESP32Cam client and subsequently invoke functions
> to get 5 images from the ESP32Cam, and save it locally. Later, call the
> face recognition module and run the '/verify' command on ESP32 if the face
> matches local trained data.  

### High-Level Sequence Diagram
![Sequence Diagram of RaspberryPi functions](/assets/RPi-Sequence_Diagram.png)
