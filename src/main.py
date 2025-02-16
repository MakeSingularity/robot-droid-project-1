# main.py

import sys
from communication.pi_communication import initialize_communication
from ai.base_ai import BaseAI
from hardware.raspberry_pi import RaspberryPi

def main():
    # Initialize communication with the development laptop
    if not initialize_communication():
        print("Failed to establish communication with the development laptop.")
        sys.exit(1)

    # Initialize the Raspberry Pi hardware
    raspberry_pi = RaspberryPi()
    raspberry_pi.setup()

    # Initialize the AI system
    ai_system = BaseAI()
    ai_system.initialize()

    print("Robot droid is ready and running!")

if __name__ == "__main__":
    main()