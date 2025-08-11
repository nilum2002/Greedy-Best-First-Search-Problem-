# Tone Compass — Find the Exit
# Hint: always choose next the undispatched node with the smallest (tone, name, idx).

import sys
import collections

def read_n_tokens(n, cast=str):
    out = []
    inp = sys.stdin
    while len(out) < n:
        line = inp.readline()
        if not line:
            break
        out.extend(line.split())
    return list(map(cast, out[:n])) if cast is int else out[:n]

def gbfs_path(adj, names, tone, start_idx, exit_idx):
    frontier = [start_idx]
    discovered = {start_idx}
    parent = [-1] * len(names)
    # TODO: implement the search described in the statement:

    while frontier:
        # find the node with smallest (tone, name) 
        min_idx = 0
        for i in range(1, len(frontier)):
            curr_node = frontier[i]
            min_node = frontier[min_idx]

            # read the questions again at this position 
            # see the bolded text in the read me 
            # here I create 2 tuples to compare the nodes 
            # (tone, name)
            curr_key = (tone[curr_node], names[curr_node])
            min_key  = (tone[min_node], names[min_node])
            if (curr_key < min_key):
                min_idx = i
        # get the minimum vertex 
        vtx = frontier.pop(min_idx)

        if vtx == exit_idx:
            path = []
            idx = vtx
            while idx != -1:
                path.append(idx)
                idx = path[idx]
            path.reverse()
            return path 


        for neg in adj[vtx]:
            if neg not in discovered:
                discovered.add(neg)
                parent[neg] = vtx
                frontier.append(neg)

    
    
                        
    
    
    return None

def solve():
    input = sys.stdin.readline

    # Read N, M
    first = input().split()
    while len(first) < 2:
        first += input().split()
    N, M = map(int, first[:2])

    # Names and tones
    names = read_n_tokens(N, cast=str)
    tone  = read_n_tokens(N, cast=int)

    # Map names -> indices
    idx = {name: i for i, name in enumerate(names)}

    # Graph
    adj = [[] for _ in range(N)]
    for _ in range(M):
        u, v = input().split()
        ui, vi = idx[u], idx[v]
        adj[ui].append(vi)
        adj[vi].append(ui)

    # Start & Exit
    start_name, exit_name = input().split()
    s, t = idx[start_name], idx[exit_name]

    if s == t:
        print(start_name)
        return

    path = gbfs_path(adj, names, tone, s, t)
    print(-1 if path is None else " ".join(path))

if __name__ == "__main__":
    solve() 