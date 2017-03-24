def shanksTransform(f, n):
    seq = [f(i) for i in range(n)]
    def _shanksTransform(s, n):
        if n < 3:
            return s
        else:
            s2 = []
            for i in range(1, n - 1):
                s2.append(
                    (s[i+1] * s[i-1] - s[i] ** 2) / (s[i+1] - 2 * s[i] + s[i-1]))
            del s
            return _shanksTransform(s2, n - 2)
    return _shanksTransform(seq,n)[0]

k = lambda n: 4 * sum([((-1) ** i) / (2 * i + 1) for i in range(n + 1)])

print("original convergence: %.20f" % k(20))
print("after transformation: %.20f" % shanksTransform(k, 20))
