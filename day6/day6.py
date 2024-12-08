

#part1 (to be optimized)
with open('input.txt','r') as f:
    input_lines = f.read().split('\n')


grid = [list(line.rstrip('\n')) for line in input_lines]

m,n = len(grid), len(grid[0])
rot_map = {'^':(0,1), '>':(1,0), 'v': (0,-1), '<': (-1,0)}
dir_map = {'^':(-1,0), '>':(0,1), 'v': (1,0), '<': (0,-1)}
rotate = {'^':'>', '>':'v', 'v':'<', '<': '^'}


in_board = lambda x,y : 0<=x<m and 0<=y<n
obstacle = lambda x,y: grid[x][y] == '#'
invalid = lambda x,y : not in_board(x,y) or obstacle(x,y)

def stuck(i:int, j:int)->bool:

    dx,dy = dir_map[grid[i][j]]
    forward_x, forward_y =  i+dx, j+dy
    dx, dy = rot_map[grid[i][j]]
    right_x, right_y = i+dx, j+dy

    return ( 
        invalid(forward_x,forward_y) and invalid(right_x,right_y)
    )


curr_x, curr_y = 0,0
for i in range(m):
    if '^' in grid[i]:
        curr_x,curr_y = i, grid[i].index('^')
        break

visited = set()
#visited.add((curr_x,curr_y))

while True:
    forward = dir_map[grid[curr_x][curr_y]]
    right = rot_map[grid[curr_x][curr_y]]
    if not obstacle(curr_x + forward[0], curr_y + forward[1]):
        dir_x, dir_y = forward
        to_change = grid[curr_x][curr_y]
    elif not invalid(curr_x + right[0], curr_y + right[1]):
        dir_x, dir_y = right
        to_change = rotate[grid[curr_x][curr_y]]
    else:
        break
    grid[curr_x][curr_y] = 'X'
    curr_x += dir_x
    curr_y += dir_y
    
    grid[curr_x][curr_y] = to_change

    visited.add((curr_x,curr_y))

    if stuck(curr_x,curr_y):
        break


print(len(visited))

    
    









