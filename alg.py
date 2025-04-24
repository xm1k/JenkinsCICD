# alg.py

from collections import deque
from dfs import dfs

def process_input(data: str) -> str:
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
    st = dfs(N,M,nums)
    return st

