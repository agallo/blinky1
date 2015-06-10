#!/usr/bin/python

__author__ = 'agallo'

from time import sleep
import wiringpi2 as wiringpi


# define some pins:

OneW = 3
OneB = 5
OneG = 7
OneY = 11
OneR = 13
TwoW = 19
TwoB = 21
TwoG = 23
TwoY = 15
TwoR = 25

# some wiringPi vars to make reading the code easier to read

LOW = 0
HIGH = 1
OUTPUT = 1

def setup():
    wiringpi.wiringPiSetupPhys()
    wiringpi.pinMode(OneW, OUTPUT)
    wiringpi.pinMode(OneB, OUTPUT)
    wiringpi.pinMode(OneG, OUTPUT)
    wiringpi.pinMode(OneY, OUTPUT)
    wiringpi.pinMode(OneR, OUTPUT)
    wiringpi.pinMode(TwoW, OUTPUT)
    wiringpi.pinMode(TwoB, OUTPUT)
    wiringpi.pinMode(TwoG, OUTPUT)
    wiringpi.pinMode(TwoY, OUTPUT)
    wiringpi.pinMode(TwoR, OUTPUT)

def AllBlink(repeat):
    count = 0
    while count <= repeat:
        wiringpin.digitalWrite(OneW, LOW)
        wiringpin.digitalWrite(OneB, LOW)
        wiringpin.digitalWrite(OneG, LOW)
        wiringpin.digitalWrite(OneY, LOW)
        wiringpin.digitalWrite(OneR, LOW)
        wiringpin.digitalWrite(TwoW, LOW)
        wiringpin.digitalWrite(TwoB, LOW)
        wiringpin.digitalWrite(TwoG, LOW)
        wiringpin.digitalWrite(TwoY, LOW)
        wiringpin.digitalWrite(TwoR, LOW)
        sleep(1)
        wiringpin.digitalWrite(OneW, HIGH)
        wiringpin.digitalWrite(OneB, HIGH)
        wiringpin.digitalWrite(OneG, HIGH)
        wiringpin.digitalWrite(OneY, HIGH)
        wiringpin.digitalWrite(OneR, HIGH)
        wiringpin.digitalWrite(TwoW, HIGH)
        wiringpin.digitalWrite(TwoB, HIGH)
        wiringpin.digitalWrite(TwoG, HIGH)
        wiringpin.digitalWrite(TwoY, HIGH)
        wiringpin.digitalWrite(TwoR, HIGH)
        sleep(1)
        count =+ 1


def cleanup():
    wiringpin.digitalWrite(OneW, LOW)
    wiringpin.digitalWrite(OneB, LOW)
    wiringpin.digitalWrite(OneG, LOW)
    wiringpin.digitalWrite(OneY, LOW)
    wiringpin.digitalWrite(OneR, LOW)
    wiringpin.digitalWrite(TwoW, LOW)
    wiringpin.digitalWrite(TwoB, LOW)
    wiringpin.digitalWrite(TwoG, LOW)
    wiringpin.digitalWrite(TwoY, LOW)
    wiringpin.digitalWrite(TwoR, LOW)


def main():
    setup()
    AllBlink(5)
    cleanup()

main()