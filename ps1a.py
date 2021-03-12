n, B = list(map(int, input().strip().split()))
T = 0

sum = 0
for i in range(1,n+1):
  if i%2 == 0:
    pi = 2**i + 1
  else:
    pi = 3**i + 1
  a = pi**(n-i)
  sum = sum + a
while sum*T <= B:
  T = T+1
print(T)

