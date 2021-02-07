class BFS:
    def __init__(self,n):
        self.color = ['white']*n
        self.graph = {0:[1], 1:[0, 2], 2: [1, 3],
		3: [2, 4, 5], 4: [3, 5, 7], 5: [3, 4, 6, 7], 6: [5, 7], 7:[4, 5, 6]}
        self.dist = [0]*n
        self.pred = [-1]*n

    def bfs(self,s):
        queue = []
        queue.append(s)
        self.dist[s]=0
        self.color[s]='gray'

        while queue:
            curr = queue.pop(0)
            print('current vertex: ', curr)
            for i,adj in enumerate(self.graph[curr]):
                if self.color[adj] == 'white':
                    self.color[adj]='gray'
                    self.dist[adj] = self.dist[curr]+1
                    self.pred[i] = curr
                    queue.append(adj)
            self.color[curr] = 'black'


b = BFS(8)
b.bfs(2)


