import RPi.GPIO as g
import time as t


dac = [8, 11, 7, 1, 0, 5, 12, 6]


def dec2bin(x): return [int(i) for i in bin(x)[2:].zfill(8)]


g.setmode(g.BCM)
g.setup(dac, g.OUT)
try:
    T = (float(input()) / 256)
    while 1:
        for i in range(256):
            g.output(dac, dec2bin(i))
            t.sleep(T)
        for i in range(255, 1, -1):
            g.output(dac, dec2bin(i))
            t.sleep(T)
finally:
    g.output(dac, 0)
    g.cleanup()