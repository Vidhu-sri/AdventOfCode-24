from functools import lru_cache
with open('input.txt','r') as file:
    input_lines = file.read()

grid = [list(line) for line in input_lines.split('\n')]

in_board = lambda x,y : 0<=x<len(grid) and 0<=y<len(grid[0])



def find_trails(i,j,visited,part):

    

    if grid[i][j] == '9':
        if part == 1:
            if (i,j) not in visited:
                visited.add((i,j))
                return 1
            return 0
        else:
            return 1
    neighbors = [(i,j+1), (i,j-1),(i+1,j),(i-1,j)]

    res = 0
    flag = False
    for neighbor in neighbors:
        x,y = neighbor

        if in_board(x,y) and grid[x][y] == str(int(grid[i][j])+1):
            flag = True
            res += find_trails(x,y,visited,part)
    
    return res if flag else 0
    
res = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '0':
            visited = set()
            plus= find_trails(i,j,visited,2)
            res+= plus
            
print(res)







