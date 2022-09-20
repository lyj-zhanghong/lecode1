target = int(input())
arr = input("")
num = [int(n) for n in arr.split()]
n = len(num)
for i in range(n):
    for j in range(i + 1, n):
        a= num[i]
        b= num[j]
        if a + b == target:
            print(i,j)
