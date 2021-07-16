class BFS:

    def __init__(self,working):
        self.working = working


    def bfs_active(self):
        if self.working == True:
            print("in progress")
        else:
            print("BFS")

bfs = BFS(working = True)
bfs.bfs_active()