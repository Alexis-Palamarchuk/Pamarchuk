import RPi.GPIO as g


dac = [8, 11, 7, 1, 0, 5, 12, 6]


def dec2bin(x): return [int(i) for i in bin(x)[2:].zfill(8)]


shim = 24
g.setmode(g.BCM)
g.setup(shim, g.OUT)
p = g.PWM(shim, 1000)
p.start(0)
try:
    while 1:
        a = float(input())
        p.ChangeDutyCycle(a)
        print(f"Предполагаемое напряжение в вольтах составляет: {(a / 100) * 3.3:.3}")
finally:
    p.stop()
    g.output(shim, 0)
    g.cleanup()