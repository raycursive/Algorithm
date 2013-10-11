def ShanksTransform(s, n):
    assert isinstance(s, list)
    if n < 3:
        return s
    else:
        s2 = []
        for i in range(1, n - 1):
            s2.append(
                (s[i + 1] * s[i - 1] - s[i] ** 2) / (s[i + 1] - 2 * s[i] + s[i - 1]))
            COUNT += 1
        del s
        return ShanksTransform(s2, n - 2)

k = lambda n: 4 * sum([(-1) ** n / (2 * i + 1) for i in range(n + 1)])

ShanksTransform([k(i) for i in range(7)], 7)
