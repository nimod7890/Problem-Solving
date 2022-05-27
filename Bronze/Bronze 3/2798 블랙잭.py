from itertools import combinations

n, m = map(int, input().split())
ans = 0
for nums in list(combinations(sorted(list(map(int, input().split()))), 3)):
    hap = sum(nums)
    if ans < hap <= m:
        ans = hap
print(ans)
