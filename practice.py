

""" simple DFS example"""

def dfs(grid,i,j):
    
    if grid[i][j] == "1":
        
        grid[i][j] = 0
        
        if i+1 < len(grid):
            dfs(grid,i+1,j)
        if j+1 < len(grid[0]):
            dfs(grid,i,j+1)
        if i-1 >-1:
            dfs(grid,i-1,j)
        if j-1 >-1:
            dfs(grid,i,j-1)
                        
    return grid
