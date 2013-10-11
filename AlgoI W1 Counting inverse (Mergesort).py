def merge(a, b, countinverse=False):
    s = []
    p, q = len(a), len(b)
    i = j = count = 0
    while(i < p and j < q):
        if a[i] < b[j]:
            s.append(a[i])
            i += 1
        else:
            s.append(b[j])
            j += 1
            if countinverse == True:
                count += len(a[i:])
    if i < p:
        s = s + a[i:]
    else:
        s = s + b[j:]
    if countinverse == False:
        return s
    else:
        return count


def mergesort(s):
    n = len(s)
    if n <= 1:
        return s
    else:
        return merge(mergesort(s[:n // 2]), mergesort(s[n // 2:]))


def count(s):
    n = len(s)
    if n <= 1:
        return 0
    else:
        x = count(s[:n // 2])
        y = count(s[n // 2:])
        a = mergesort(s[:n // 2])
        b = mergesort(s[n // 2:])
        z = merge(a, b, countinverse=True)
        return x + y + z



