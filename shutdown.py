#!/usr/bin/python3

import RPi.GPIO as GPIO
import subprocess
from time import sleep

def main():
    setup_pins()
    wait_for_short()


def setup_pins():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(5, GPIO.IN)


def wait_for_short():
    GPIO.wait_for_edge(5, GPIO.FALLING)
    print("shutting down, have a nice day!")
    sleep(1)
    subprocess.call(['shutdown', 'now'], shell=False)


if __name__ == "__main__":
    main()
