import RPi.GPIO as g


def f(x): return [int(i) for i in bin(x)[2:].zfill(8)]


dac = [8, 11, 7, 1, 0, 5, 12, 6]
g.setmode(g.BCM)
g.setup(dac, g.OUT)
try:
    while 1:
        a = input()
        if a == 'q': break
        try: k = int(a)
        except Exception:
            try:
                l = float(a)
                print("Вы ввели нецелое число")
            except Exception: print("Вы ввели не число")
            continue
        if k < 0:
            print("Вы ввели отрицательное число")
            continue
        if k > 255:
            print("Вы ввели слишком большое число")
            continue
        g.output(dac, f(int(a)))
        print(f"Предполагаемое напряжение в вольтах составляет: {(int(a) / 256) * 3.3:.3}")
finally:
    g.output(dac, 0)
    g.cleanup()