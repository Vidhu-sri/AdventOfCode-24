import sys
from functools import cache

num_map  = {
    '7': (0, 0), '8': (0, 1), '9': (0, 2),
    '4': (1, 0), '5': (1, 1), '6': (1, 2),
    '1': (2, 0), '2': (2, 1), '3': (2, 2),
                    '0': (3, 1), 'A': (3, 2),
}
op_map = {
                    '^': (0, 1), 'A': (0, 2),
    '<': (1, 0), 'v': (1, 1), '>': (1, 2),
}


def sequence(code,keypad):
    
    invalid_coords = (3,0) if keypad == num_map else (0,0)
    current = keypad['A']
    valid = set(keypad.values())
    res = ''
    for num in code:
        
        x1,y1 = current
        x2,y2 = keypad[num]
        path = '<' * (y1 - y2) +  'v' * (x2 - x1) + '^' * (x1 - x2) + '>' * (y2 - y1)
        if invalid_coords == (x1, y2) or invalid_coords == (x2, y1):
            path = path[::-1]
        res+=path
            
        current = keypad[num]
        res+='A'
    return res




with open("input.txt",'r') as file:
        puzzle_input = file.read()
#part1
def main():

    
    res =0
    for code in puzzle_input.split('\n'):
        code = code.rstrip('\n')
        print(code)

        inter = sequence(code,num_map)
        print(inter)
        inter_1 = sequence(inter,op_map)
        print(inter_1)
        inter_2 = sequence(inter_1,op_map)
        print(inter_2)
        
        #print(inter)
        #print(inter_1)
        res+= len(inter_2)*int(code[:-1])
        print(len(inter_2), int(code[:-1]))
    print(res)


def part2():
    res = 0
    for code in puzzle_input.split('\n'):
        res+=int(code[:-1])*get_length(code,26,True)
    print(res)

#part2
@cache
def get_length(code,i,first_iter=False):
    
    if i==0:
        return len(code)
    prev = 'A'
    res = 0
    keypad = num_map if first_iter else op_map
    invalid_coords = (3,0) if keypad == num_map else (0,0)

    for num in code:
        x1,y1 = keypad[prev]
        x2,y2 = keypad[num]
        path = '<' * (y1 - y2) +  'v' * (x2 - x1) + '^' * (x1 - x2) + '>' * (y2 - y1)
        if invalid_coords == (x1, y2) or invalid_coords == (x2, y1):
            path = path[::-1]
        res+= get_length(path+'A',i-1)
        prev = num
    return res


part2()

