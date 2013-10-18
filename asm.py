import math
from functools import partial


def asm(func, a, b, epsilon):

    def simpson(width, a, b, c):
        return (a + b + 4 * c) * width / 6

    def _asm(func, a, b, epsilon, area):
        c = (a + b) / 2
        leftarea = simpson(c - a, func(a), func(c), func((c + a) / 2))
        rightarea = simpson(b - c, func(c), func(b), func((b + c) / 2))
        if abs(leftarea + rightarea - area) <= 15 * epsilon:
            return leftarea + rightarea + (leftarea + rightarea - area) / 15
        return _asm(func, a, c, epsilon / 2, leftarea) + _asm(func, c, b, epsilon / 2, rightarea)

    return _asm(func, a, b, epsilon, simpson(b - a, func(a), func(b), func((a + b) / 2)))


def normaldistributionpdf(x, mu=0, sigma=1):
    return 1 / (sigma * math.sqrt(2 * math.pi)) * math.exp(-(x - mu) ** 2 / (2 * sigma ** 2))


def normaldistributioncdf(x, mu=0, sigma=1):
    return asm(lambda t:normaldistributionpdf(t,mu,sigma), -99999, x, 0.0000000001)

print(normaldistributioncdf(0,mu=1,sigma=3))
