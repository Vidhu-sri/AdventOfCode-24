import sys

grid = [list(line.rstrip('\n')) for line in sys.stdin]
mas_dict = {'M':'S', 'S': 'M'}

def check(i,j,grid):
    return (
        grid[i][j+2] in mas_dict and
        grid[i+1][j+1] == 'A' and
        grid[i+2][j+2] == mas_dict[grid[i][j]] and
        grid[i+2][j] == mas_dict[grid[i][j+2]]
        )


res = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] in mas_dict and (j<=len(grid[0])-3 and i<=len(grid)-3):
            if check(i,j,grid):
                res+=1

print(res)



