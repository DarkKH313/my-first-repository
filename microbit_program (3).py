from microbit import *
import radio
radio.config(group=5)
radio.on()
while True:
    message = radio.receive()
    if message == 'I AM SENDING':
        display.scroll(I recieved)
