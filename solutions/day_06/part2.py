

with open('input.txt', 'r') as file:
    input_lines = file.read().split('\n')

grid = [list(line.rstrip('\n')) for line in input_lines]

m,n = len(grid), len(grid[0])

in_board = lambda x,y : 0<=x<m and 0<=y<n
obstacle = lambda x,y: grid[x][y] == '#'

for i in range(m):
    if '^' in grid[i]:
        curr_x,curr_y = i, grid[i].index('^')
        break

def loop(i,j):

    dx,dy = -1,0    
    seen = set()

    while True:

        seen.add((i,j,dx,dy))

        if not in_board(i+dx,j+dy):
            return False

        if obstacle(i+dx,j+dy):
            dx,dy = dy,-dx
        
        else:
            i+=dx
            j+=dy
        
        if (i,j,dx,dy) in seen:
            return True
    
res = 0
for i in range(m):
    for j in range(n):
        if grid[i][j] == '.':
            grid[i][j] = '#'
            res+= loop(curr_x,curr_y)
            grid[i][j] = '.'
print(res)
        






