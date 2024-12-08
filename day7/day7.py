import sys
import itertools
from tqdm import tqdm
import operator


ops = {
    '+': operator.add,
    '*': operator.mul
}


def calc(op, rhs):
   
    res = rhs[0]
    for i in range(len(rhs) - 1):
        if op[i] == '|': 
            res = int(str(res) + str(rhs[i + 1]))
        else: 
            res = ops[op[i]](res, rhs[i + 1])
    return res


def calibrate(lhs, rhs):
    symbols = ['+', '*', '|']  #no '|' in part 1
    for combo in itertools.product(symbols, repeat=len(rhs) - 1):
        if int(lhs) == calc(combo, rhs):
            return True
    return False


lines = [line for line in sys.stdin]

res = 0


for line in tqdm(lines, desc="Processing equations", unit="line", ncols=80):
    eqn = line.split(':')
    lhs = int(eqn[0])
    rhs = list(map(int,eqn[1].strip().split(' ')))

    if calibrate(lhs, rhs):
        res += int(lhs)

print(res)
