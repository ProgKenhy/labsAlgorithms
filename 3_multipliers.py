x = int(input("Input a number x: "))
ans = set()

max_k = 0
while 3**max_k < x:
    max_k += 1

max_l = 0
while 5**max_l < x:
    max_l += 1

max_m = 0
while 7**max_m < x:
    max_m += 1

for K in range(max_k):
    for L in range(max_l):
        for M in range(max_m):
            res = 3**K*5**L*7**M
            if res <= x:
                ans.add(res)
print(sorted(ans))
