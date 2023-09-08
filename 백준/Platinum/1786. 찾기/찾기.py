def kmp(parent, pattern):
    m, n = len(pattern), len(parent)
    table = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    j = 0
    loc = []
    for i in range(n):
        while j > 0 and parent[i] != pattern[j]:
            j = table[j - 1]
        if parent[i] == pattern[j]:
            if j == m - 1:
                loc.append(i - m + 2)
                j = table[j]
            else:
                j += 1
    print(len(loc))
    print(*loc)

t = input()
p = input()
kmp(t, p)