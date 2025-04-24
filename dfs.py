def dfs(N,M,nums):
    U = {
        1: []
    }

    for _ in range(0,M*2-1,2):
        a,b = (nums[_]), (nums[_+1])
        if U.get(a) == None:
            U[a] = []
        if b!=a:
            U[a].append(b)
        if U.get(b) == None:
            U[b] = []
        if a!=b:
            U[b].append(a)


    visited = set()
    next = set([1])

    while(len(next)>0):
        x = next.pop()
        visited.add(x)
        lis = U[x]
        for el in lis:
            if el not in visited:
                next.add(el)

    return f"{len(visited)}\n{' '.join(map(str, visited))}"

def main():
    N, M = map(int, input().split())
    nums = []
    for _ in range(M):
        a, b = map(int, input().split())
        nums.append(a)
        nums.append(b)
    print(dfs(N, M, nums))

if __name__ == "__main__":
    main()


