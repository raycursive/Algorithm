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



class Union_find():
	def __init__(self,G):
		self.id={i:i for i in G}

	def getfather(self,vertex):
		if self.id[vertex]==vertex:
			return vertex
		else:
			self.id[vertex]=self.getfather(self.id[vertex])
			return self.id[vertex]

	def union(self,u,v):
		u,v=self.getfather(u),self.getfather(v)
		if not u==v:
			self.id[v]=self.id[u]

	def connected(self,u,v):
		return self.getfather(u)==self.getfather(v)


def Kruskal(V,E):
	T={}
	E_sorted=sorted(list(E.items()),key=lambda x:x[1])
	union=Union_find(V)
	for edge,value in E_sorted:
		u,v=edge
		if not union.connected(u,v):
			T[(u,v)]=value
			union.union(u,v)
	return T

print(sum(Kruskal(V,E).values()))




