from time import sleep
from pymata4 import pymata4

s = lambda data: print(f"Distance: {data[2]} cm")
try:
    board = pymata4.Pymata4()
    board.set_pin_mode_sonar(12, 11, s)
    while True:
        sleep(0.1)
        board.sonar_read(12)
except RuntimeError: print('Sir, see if Arduino board might not be connected with pc.')
