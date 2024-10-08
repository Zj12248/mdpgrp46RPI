# STM32 BOARD SERIAL CONNECTION
# to get connected serial devices: ls /dev/serial/by-id/
SERIAL_PORT = "/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0002-if00-port0"  # stm32
BAUD_RATE = 115200

# API DETAILS
API_IP = '192.168.46.26'  # IP address of laptop
API_PORT = 5000

# ROBOT SETTINGS
OUTDOOR_BIG_TURN = False
