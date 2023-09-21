import sys, uselect
from machine import UART

uart_port = 2
uart_speed = 9600

uart = UART(uart_port, uart_speed)

usb = uselect.poll()
usb.register(sys.stdin, uselect.POLLIN)

print("ESP32 USB <-> UART <-> UART <-> ESP32 USB program")
print("Remember to connect TX1 -> RX2 and RX1 <- TX2")
print("Hallo")

while True:
    if uart.any() > 0:
        string = uart.read().decode()
        print(string)
        
    if usb.poll(0):
        ch = sys.stdin.read(1)
        uart.write(ch)
        if ch == '\n':
            print()