class Kruskal:
    """
    algorithm Kruskal(G) is
    F:= ∅
    for each v ∈ G.V do
        MAKE-SET(v)
    for each (u, v) in G.E ordered by weight(u, v), increasing do
        if FIND-SET(u) ≠ FIND-SET(v) then
            F:= F ∪ {(u, v)}
            UNION(FIND-SET(u), FIND-SET(v))
    return F
    """
    def __init__(self,n):
        self.V = n
        self.graph = []
    def add_edge(self,u,v,w):
        self.graph.append([u,v,w])

    def find_parent(self,parent_list,u):
        if parent_list[u]==u:
            return u
        return self.find_parent(parent_list,parent_list[u])

    def kruskals_algo(self):
        MST = []
        self.graph =  sorted(self.graph, key=lambda item:item[2])
        parent_list = [i for i in range(self.V)]
        i,e = 0,0

        while (e<self.V-1):
            u,v,w = self.graph[i]
            x = self.find_parent(parent_list,u)
            y = self.find_parent(parent_list,v)

            if x!=y:
                MST.append([u,v,w])
                parent_list[y] = x
                e+=1
            i+=1
        print(MST)
g = Kruskal(6)
g.add_edge(0, 1, 4)
g.add_edge(1, 0, 4)
g.add_edge(0, 2, 4)
g.add_edge(2, 0, 4)
g.add_edge(1, 2, 2)
g.add_edge(2, 1, 2)
g.add_edge(2, 3, 3)
g.add_edge(3, 2, 3)
g.add_edge(2, 5, 2)
g.add_edge(5, 2, 2)
g.add_edge(2, 4, 4)
g.add_edge(4, 2, 4)
g.add_edge(3, 4, 3)
g.add_edge(4, 3, 3)
g.add_edge(4, 5, 3)
g.add_edge(5, 4, 3)
g.kruskals_algo()