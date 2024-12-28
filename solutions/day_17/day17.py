import re
from itertools import count

with open('input.txt','r') as file:
    puzzle_input = file.read()

pattern = re.compile(r'[\d,?]+')
data = pattern.findall(puzzle_input)
A,B,C = map(int,data[:3])
program = list(map(int,data[-1].split(',')))



def get_combo(val:int):

    if val<=3:
        return val
    match val:
        case 4: return A
        case 5: return B
        case 6: return C



def perform_op(op_code,operand,output):
    global A,B,C

    if op_code == 0:
        A = A//(2**get_combo(operand))
        return

    if op_code == 1:
        B = B^operand
        return
    if op_code == 2:
        B = get_combo(operand)%8
        return
    if op_code == 3:
        if not A:
            return
        return operand  #ip = operand
    if op_code == 4:
        B = B^C
        return
    if op_code == 5:
        output.append(get_combo(operand)%8)
    if op_code == 6:
        B = A//(2**get_combo(operand))
        return
    C = A//(2**get_combo(operand))


def prog(program,a):
    output = []
    
    ip = 0
    global A
    A = a
    while ip < len(program)-1:

        print(A,B,C)

        opcode,oper = program[ip],program[ip+1]
        flag = True

        res =  perform_op(opcode,oper,output)
        if res != None:
            ip = res
            flag = False
        if flag:
            ip+=2
    return output


#part2

'''
a = a%8
b = b^2
c = a>>b
b = b^c
b = b^3
a = a>>3
if a !=0: jump 0

2,4,1,2,7,5,4,7,1,3,5,5,0,3,3,0
'''
print(program)

def find(program,ans):

    if program == []:return ans

    for t in range(8):
        a = (ans << 3)|t
        b = a%8
        b = b^2
        c = a>>b
        b = b^c
        b = b^3
        if b%8 == program[-1]:
            sub = find(program[:-1],a)
            if sub is None: continue
            return sub
print(find(program,0))
        







    
# print(','.join(map(str,output))) part 1


    




        


