import time
import serial
from xbee import ZigBee

# Specify the serial port and baud rate for the XBee device
serial_port = '/dev/ttyUSB0'  # Adjust this to your serial port
baud_rate = 9600

# Open the serial port
ser = serial.Serial(serial_port, baud_rate)

# Create a ZigBee object for communication
xbee = ZigBee(ser)

try:
    # Send a message to the XBee device
    message = "Hello, XBee!"
    xbee.send("tx", dest_addr_long=b'\x00\x13\xA2\x00\x41\x7D\x36\x7C', data=message)

    # Wait for a response (optional)
    response = xbee.wait_read_frame()
    print("Response received:", response)

finally:
    # Close the serial port
    ser.close()
