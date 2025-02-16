# Raspberry Pi Hardware Interface

This file contains functions to interface with the hardware components of the Raspberry Pi. It includes methods for controlling GPIO pins and other hardware-related tasks.

import RPi.GPIO as GPIO
import time

class RaspberryPi:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)  # Use Broadcom pin numbering
        self.pins = {}

    def setup_pin(self, pin_number, direction):
        """Setup a GPIO pin."""
        if direction not in [GPIO.IN, GPIO.OUT]:
            raise ValueError("Direction must be GPIO.IN or GPIO.OUT")
        GPIO.setup(pin_number, direction)
        self.pins[pin_number] = direction

    def write_pin(self, pin_number, value):
        """Write a value to a GPIO pin."""
        if pin_number not in self.pins or self.pins[pin_number] != GPIO.OUT:
            raise ValueError("Pin not set up for output")
        GPIO.output(pin_number, value)

    def read_pin(self, pin_number):
        """Read a value from a GPIO pin."""
        if pin_number not in self.pins or self.pins[pin_number] != GPIO.IN:
            raise ValueError("Pin not set up for input")
        return GPIO.input(pin_number)

    def cleanup(self):
        """Clean up GPIO settings."""
        GPIO.cleanup()