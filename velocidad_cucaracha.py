import math
def cockroach_speed(s):
    velocidad_pasada = s * (5/18)
    velocidad_multiplicada = velocidad_pasada * 100
    velocidad_def = math.floor(velocidad_multiplicada)
    return velocidad_def



if __name__ == "__main__":
    assert cockroach_speed(1.08) == 30
    assert cockroach_speed(1.09) == 30
    assert cockroach_speed(0) == 0
    assert cockroach_speed(0.17569897570441528) == 4

