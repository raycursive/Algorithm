import random

# init variables(list)
edge = []
minnum = 10000000000000

# functions


def findedge(s, edge):
    for elem in s:
        for i in range(1, len(elem)):
            if not ((elem[0], elem[i]) in edge or (elem[i], elem[0]) in edge):
                tmp = [elem[0], elem[i]]
                tmp.sort()
                edge.append(tuple(tmp))


def contract(a, b, edge):
    n = len(edge)
    i = 0
    while(i < n):
        x, y = edge[i]
        if y == b:
            if x == a:
                del edge[i]
                n -= 1
                i -= 1
            else:
                tmp = [x, a]
                tmp.sort()
                edge[i] = tuple(tmp)
        elif x == b:
            tmp = [a, y]
            tmp.sort()
            edge[i] = tuple(tmp)

        i += 1

# init data
file = open("kargerMinCut.txt")
array = [line.split('\t') for line in file]
for i in array:
    i.pop()
    for j in i:
        i.insert(0, int(i.pop()))
findedge(array, edge)
edge_copy = edge[:]

# main
for i in range(100000):
    edge = edge_copy[:]
    n = 200
    while(n > 2):
        u, v = random.choice(edge)
        contract(u, v, edge)
        n -= 1
    if len(edge) <= minnum:
        minnum = len(edge)
        print(edge)
        print(minnum)

# output
print(minnum)
