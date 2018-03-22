X = int(input())
N = int(input())

rollover = 0

for i in range(N):
    P = int(input())
    diff = X - P
    rollover += diff

print(X + rollover)
