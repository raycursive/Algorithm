def EulerMethod(initial, aim, derivative, step):
    x = 0
    value = initial
    while x <= aim:
        x += step
        value += step * derivative(value)
    return value

print(EulerMethod(0.5, 1, lambda x: -3 * x, 0.01))


def RK4(initial, aim, derivative, step):
    x = 0
    value = initial
    while x <= aim:
        x += step
        k1 = derivative(value)
        k2 = derivative(value + step * k1 / 2)
        k3 = derivative(value + step * k2 / 2)
        k4 = derivative(value + step * k3)
        value += step * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return value

print(RK4(0.5, 1, lambda x: -3 * x, 0.01))