class graph:
    def __init__(self,size):
        self.adjMatrix = [[0 for i in range(size)] for j in range(size)]
    def make_graph(self,u1,u2):
        self.adjMatrix[u1][u2] = 1
        self.adjMatrix[u2][u1] = 1
    def delete_edge(self,u1,u2):
        self.adjMatrix[u1][u2] = 0
        self.adjMatrix[u2][u1] = 0
    def show_graph(self):
        for row in self.adjMatrix:
            print(row)
g = graph(4)
g.make_graph(1,2)
g.make_graph(3,2)
g.make_graph(2,0)
g.show_graph()
print('******************')
g.delete_edge(2,0)
g.show_graph()
