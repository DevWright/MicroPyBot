
from machine import Pin, PWM

class Motor(object):
    """Class for driving motors with the TB6612FNG"""

    def __init__(self, in1, in2, opwm, stdby):
        self.__in1 = Pin(in1, Pin.OUT)
        # self.__in1.value(1)
        self.__in2 = Pin(in2, Pin.OUT)
        self.__opwm = PWM(Pin(opwm))
        self.__pin_stdby = Pin(stdby, Pin.OUT)
        self.__pin_stdby.value(1)
        self.speed = 0

    def drive(self, speed):
        """Turning the motor."""
        self.speed = speed

        if self.speed < 0:
            self.__in1.value(1)
            self.__in2.value(0)
        elif self.speed > 0:
            self.__in1.value(0)
            self.__in2.value(1)
        else:
            self.__in1.value(0)
            self.__in2.value(0)

        self.__opwm.duty(abs(self.speed))
