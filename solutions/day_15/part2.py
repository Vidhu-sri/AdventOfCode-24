


with open('input.txt','r') as file:
    puzzle_input = file.read().split('\n\n')



def resize(string):
    res = ''
    for char in string:
        if char == '#' or char == '.':
            res+= 2*char
        elif char == 'O':
            res+= '[]'
        else:
            res+= char+'.'
    return res

x,y = None, None
grid = []
dir_map = {'^':(-1,0), '>':(0,1), 'v':(1,0), '<': (0,-1)}

for idx,line in enumerate(puzzle_input[0].split('\n')):
    line = resize(line)
    grid.append(list(line))
    if '@' in line:
        x,y = idx, line.index('@')

path = puzzle_input[1]

in_board = lambda x,y: 0<=x<len(grid) and 0<=y<len(grid[0])


def can_move_vertically(x,  y, dx):
    if(grid[x+dx][y] == '#'):
        return 1 
    if(grid[x+dx][y] == '.'):
        return 0 

    return can_move_vertically(x+dx,y,dx) + can_move_vertically(x+dx,y + 1 if grid[x+dx][y] == '[' else y-1,dx)


def move_vertically(  x:int,y:int, dx:int):

    if not in_board(x,y):
        return x,y
    
    if(grid[x+dx][y] == '[' or grid[x+dx][y] == ']'):
            move_vertically(x+dx,y + 1 if grid[x+dx][y] == '['  else  y-1,dx)
            move_vertically(x+dx,y,dx)
    
    grid[x+dx][y]=grid[x][y]
    if(grid[x][y] == '@'):
        ry=x+dx
        grid[x][y]='.'
        return ry,y
    else:
        grid[x][y]='.'
        return x,y
    


def make_move(x,y,grid, move):

    dx,dy = dir_map[move]
    fx,fy = x+dx, y+dy

    if grid[fx][fy] == '.':
        grid[x][y], grid[fx][fy] = grid[fx][fy], grid[x][y]
        return fx,fy

    if grid[fx][fy] == '[' or grid[fx][fy] == ']':

        if move == '>' or move == '<':

            temp_x, temp_y = fx,fy
            while grid[temp_x][temp_y] == '[' or grid[temp_x][temp_y] == ']':
                temp_y += dy
            if grid[temp_x][temp_y] == '.':
                if move == '>':
                    grid[x][y:temp_y+1] = ['.']+grid[x][y:temp_y]
                    return fx,fy
                if move == '<':
                    grid[x][temp_y:y+1] = grid[x][temp_y+1:y+1]+['.']
                    return fx,fy
            else:
                return x,y

        elif can_move_vertically(x,y,dx) == 0:
            return move_vertically(x,y,dx)

        else:
            return x,y
        

            
def print_grid():
    for line in grid:
        print(''.join(line))
    print('\n')

for move in path:
    if move == '\n':
        continue
    moved = make_move(x,y,grid,move)
    
    if moved:
        x,y = moved
    

print_grid()
res =0 
for i in range(len(grid)):
    for j in range(len(grid[0])):

        if grid[i][j] == '[':
            res+= 100*i+j
print(res)














