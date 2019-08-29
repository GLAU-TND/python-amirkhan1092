n = int(input())
res = list(map(int, input().split()))

print(max([res.count(i) for i in res]))


