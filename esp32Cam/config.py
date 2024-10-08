
#-camera configuration int keys ** DONT EDIT **---------------
PIN_PWDN    = const(0) # power-down 
PIN_RESET   = const(1) # reset
PIN_XCLK    = const(2)
PIN_SIOD    = const(3) #  SDA
PIN_SIOC    = const(4) #  SCL

PIN_D7      = const(5)
PIN_D6      = const(6)
PIN_D5      = const(7)
PIN_D4      = const(8)
PIN_D3      = const(9)
PIN_D2      = const(10)
PIN_D1      = const(11)
PIN_D0      = const(12)
PIN_VSYNC   = const(13)
PIN_HREF    = const(14)
PIN_PCLK    = const(15)

XCLK_MHZ    = const(16)  #  camera machine clock
PIXFORMAT   = const(17)  #  pixel format
FRAMESIZE   = const(18)  #  framesize
JPEG_QUALITY= const(19)
FB_COUNT    = const(20)  #  framebuffer count > 1 continuous mode (JPEG only)

#-------------------------------------------------------------

# OV2640 Boards configuration below (can edit - add your board)

# AI-Thinker esp32-cam board
ai_thinker = {PIN_PWDN:32,
              PIN_RESET:-1,
              PIN_XCLK:0,
              PIN_SIOD:26,
              PIN_SIOC:27,
              PIN_D7:35,
              PIN_D6:34,
              PIN_D5:39,
              PIN_D4:36,
              PIN_D3:21,
              PIN_D2:19,
              PIN_D1:18,
              PIN_D0:5,
              PIN_VSYNC:25,
              PIN_HREF:23,
              PIN_PCLK:22,
              XCLK_MHZ:16,
              PIXFORMAT:5,
              FRAMESIZE:10,
              JPEG_QUALITY:10,
              FB_COUNT:1, 
}


def configure(cam, config):
    for key, val in config.items():
        # print(key, val)
        cam.conf(key, val)

