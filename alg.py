# alg.py


def process_input(data: str) -> str:
    print(str)
    """
    Ожидает на вход строку вида:
        N M
        u1 v1
        u2 v2
        ...
        uM vM
    Возвращает:
        K
        v1 v2 ... vK
    где это компонента связности, содержащая вершину 1.
    """
    parts = data.strip().split()
    if len(parts) < 2:
        return "0\n"
    N, M = map(int, parts[:2])
    nums = list(map(int, parts[2:]))
    # строим список смежности с учётом петель и кратных рёбер
    adj = [[] for _ in range(N+1)]
    for i in range(0, 2*M, 2):
        u, v = nums[i], nums[i+1]
        adj[u].append(v)
        if u != v:
            adj[v].append(u)
    # BFS от 1
    visited = [False] * (N+1)
    q = deque([1])
    visited[1] = True
    comp = []
    while q:
        u = q.popleft()
        comp.append(u)
        for w in adj[u]:
            if not visited[w]:
                visited[w] = True
                q.append(w)
    comp.sort()
    return f"{len(comp)}\n{' '.join(map(str, comp))}"

