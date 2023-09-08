n, k = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * (k+1)

for weight, value in items:
    for j in range(k, weight-1, -1):
        dp[j] = max(dp[j], dp[j - weight] + value)

print(dp[k])