

with open('input.txt','r') as file:
    puzzle_input = file.read().split('\n\n')

grid = []
x,y = None, None

for idx,line in enumerate(puzzle_input[0].split('\n')):
    grid.append(list(line))
    if not x and '@' in line:
        x,y = idx, line.index('@')

path = puzzle_input[1]



dir_map = {'^':(-1,0), '>':(0,1), 'v':(1,0), '<': (0,-1)}

def make_move(x:int,y:int,grid:list[str], move:tuple[int,...])->tuple[int,...]:

    dx,dy = dir_map[move]
    fx,fy = x+dx, y+dy

    if grid[fx][fy] == '.':
        grid[x][y], grid[fx][fy] = grid[fx][fy], grid[x][y]
        return fx,fy
    if grid[fx][fy] == 'O':

        next_x, next_y = fx,fy

        while grid[next_x][next_y] == 'O':
            next_x+=dx
            next_y+=dy
        
        if grid[next_x][next_y] == '.':
            grid[x][y],grid[fx][fy],grid[next_x][next_y] = '.', '@','O'
            return fx,fy
        else:
            return x,y
    
    return x,y

def print_grid():
    for line in grid:
        print(''.join(line))
    print('\n')

for move in path:
    if move == '\n':
        continue
    x,y = make_move(x,y,grid,move)
    #print_grid()

print(grid)
res =0 
for i in range(len(grid)):
    for j in range(len(grid[0])):

        if grid[i][j] == 'O':
            res+= 100*i+j
print(res)






