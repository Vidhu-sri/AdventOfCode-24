
from collections import defaultdict

with open('input.txt','r') as file:
    puzzle_input = file.read()

graph =  defaultdict(set)

for edge in puzzle_input.split('\n'):
    c1,c2 = edge.split('-')
    graph[c1].add(c2)
    graph[c2].add(c1)

candidates = [k for k in graph.keys() if k.startswith('t')]
res = 0
seen = set()
for c in candidates:
    for a in graph[c]:
        for b in graph[a]:
            if b in graph[c]:
                sorted_triplet = tuple(sorted((a, b, c)))
                if sorted_triplet not in seen:
                    seen.add(sorted_triplet)
                    res += 1


#part2

def bron_kerbosch(selected, candidates, excluded):
        if not candidates and not excluded:
            return selected
        
        max_clique = set()
        for v in candidates.copy():
            clique = bron_kerbosch(
                selected.union({v}), 
                candidates.intersection(graph[v]), 
                excluded.intersection(graph[v])
            )
            max_clique = max(max_clique, clique, key=len)
            candidates.remove(v)
            excluded.add(v)

        return max_clique
max_clique = bron_kerbosch(set(),set(graph),set())
print(','.join(sorted(max_clique)))

