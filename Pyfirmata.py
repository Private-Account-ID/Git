from pyfirmata import Arduino, SERVO
from time import sleep

try:
    board = Arduino("COM3")
    board.digital[10].mode = SERVO          # Pin for servo motor
    led = board.get_pin('d:13:o')           # Pin for blink led
    def Led(txt):
        if 'on' in txt: 
            led.write(1)
            return "Turned on Led on pin 13"
        else: 
            led.write(0)
            return "Turned off Led on pin 13"

    def MoveServo(txt):
        for i in txt: 
            if i.isnumeric():
                board.digital[10].write(int(i))
                sleep(0.5) # Alway use delay and put delay atleast of 0.5 for proper rotation    
                print(f"Angle is {i} degree")
        return 
except Exception: print('Sir, check if Arduino board is connected to pc?')

                        

