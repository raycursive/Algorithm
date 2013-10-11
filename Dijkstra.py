import heapq

# Graph:             dict <- {vertex:{dict of adjacent vertex:value}}    [G]
# distance           dict <- {vertex:distance}                           [d]
# previous           dict <- {vertex:previous vertex}                    [previous]
# explored_vertex    dict <- {vertex:1}                                  [S]
# other_vertex       heap <- {(d[v],vertex)}                             [Q]


def dijkstra(G, start):
    d = {v: 99999 for v in G}
    d[start] = 0
    previous = {v: None for v in G}
    S = {}
    Q = [(d[v], v) for v in G]
    heapq.heapify(Q)
    while Q != []:
        value, vertex = heapq.heappop(Q)
        S[vertex] = 1
        for adjvertex in G[vertex]:
            if not adjvertex in S:
                if d[adjvertex] > d[vertex] + G[vertex][adjvertex]:
                    d[adjvertex] = d[vertex] + G[vertex][adjvertex]
                    heapq.heappush(Q, (d[adjvertex], adjvertex))
                    previous[adjvertex] = vertex
    return (d, previous)
