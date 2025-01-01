def solve():
    D = [x.split() for x in open("input.txt").read().split("\n\n")]
    L = {"#":[], ".":[]}
    for t in [["".join(a[i] for a in d) for i in range(5)] for d in D]:
        L[t[0][0]].append([len(s) - len(s.strip("#")) - 1 for s in t])
    print(sum(all(x+y <= 5 for x,y in zip(l,k)) for l in L["#"] for k in L["."]))

solve()