
from machine import Pin, PWM
from motor import Motor

class MicroPyBotMove(object):
    """MicroPyBot move class. Handles all the movement for the PyBot"""

    def __init__(self):
        self.__motor_l = Motor(0, 4, 5, 15)
        self.__motor_r = Motor(12, 13, 14, 15)

        self.__motor_l_speed = None
        self.__motor_r_speed = None

        self.__motor_l_turn = None
        self.__motor_r_turn = None

    def drive(self, speed, turn):
        """Sets motors accordingly depending on speed and turning."""
        speed_l = speed
        speed_r = speed
        if turn < 0:
            speed_l *= -1
        elif turn > 0:
            speed_r *= -1

        self.__motor_l.drive(speed_l)
        self.__motor_r.drive(speed_r)


class MicroPyBotBuzzer(object):
    """Class for PyBot buzzer"""

    def __init__(self, pin):
        self.__buzzer = PWM(Pin(pin))
        self.__buzzer.freq(0)

    def freq(self, freq):
        """Set buzzer frequency"""
        self.__buzzer.freq(freq)

    def vol(self, vol):
        """Set buzzer volume"""
        if vol > 100:
            vol = 100
        elif vol < 0:
            vol = 0

        duty_cycle = vol * 512 / 100
        self.__buzzer.duty(duty_cycle)
