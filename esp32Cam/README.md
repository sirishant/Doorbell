# ESP32Cam Logic

#### This document is concerned only with ESP32Cam Processing.<br>
- For more info on RaspberryPi Processing, [refer here](/raspberrypi/README.md).
- For more info on ESP32Cam-RaspberryPi Communication, [refer here](/README.md).

### Problem Statement
> Have a web accessible interface to perform various functionalities through ESP32Cam,
> including ‘/login’, ‘/foto’, ‘/webcam’, ‘/verify’, ‘/logout’ etc. Be able to
> take photos and send it back to the caller. Be capable of interpreting incoming
> instructions and act accordingly.

### Goals
> Create a webpage interface for various functionalities of ESP32Cam.

### Non-Goals
> Processing of information outside of ESP32Cam.

### Proposed Solution
> Create a LAN accessible server on the ESPCam. Authenticate incoming traffic
> to the binded IP Address when they access specific URL Password. Only the bound
> IP Address can access all other functionalities of the ESPCam. Take photos when
> requested and return them accordingly. Verify instruction to actuate a servo when
> the ‘/verify’ webpage is accessed.

### High-Level Sequence Diagram
![ESP32Cam functions Sequence Diagram](/assets/ESP32Cam-Sequence_Diagram.png)

### Risks
> Inconsistent server startup, server resets after every logout.

### Alternative Solutions
> Using IR Camera instead of RGB, use different platform instead of ESPCam.
