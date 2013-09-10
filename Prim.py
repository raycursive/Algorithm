import heapq

#file read
#file = open("edges.txt")
#n_vertices,n_edges = tuple(map(int,file.readline().rsplit()))
#V = {i for i in range(1,n_vertices+1)}
#E = {}
#for line in file:
#    i,j,v = tuple(map(int,line.rsplit()))
#    E[(i,j)] = v

#Edges:{(u,v):weight}
#Vertices:{vertex}


def prim(V,E,start = 1):
        X = {start}
        T = {}
        key = {i:(999999,(0,0)) for i in V}
        for i in E:
                u, v = i
                value = E[i]
                tmpweight, tmpedge = key[u]
                if u == start and tmpweight > value:
                        key[v] = (value,i)
                tmpweight, tmpedge = key[v]
                if v == start and tmpweight > value:
                        key[u] = (value,i)
        heap = list(key.values())
        heapq.heapify(heap)
        while X != V:
                value_to_append, edge = heapq.heappop(heap)
                u, v = edge
                v_add = u if v in X else v
                if not v_add in X:
                        for i in V:
                                value=key[i][0]
                                if (v_add, i) in E and not(i in X):
                                        if E[(v_add,i)] < value:
                                                heapq.heappush(heap,(E[(v_add,i)], (v_add,i)))
                                if (i, v_add) in E and not(i in X):
                                        if E[(i,v_add)] < value:
                                                heapq.heappush(heap,(E[(i,v_add)], (i,v_add)))
                        X.add(v_add)
                        T[edge] = value_to_append
        return T

print(sum(prim(V,E).values()))
