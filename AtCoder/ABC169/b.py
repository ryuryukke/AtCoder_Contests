import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
ans = 1
if 0 in a:
    print(0)
    exit()
for i in a:
    ans *= i
    if ans > 10**18:
        print("-1")
        exit()
print(ans)

