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
epsilon = 0.01
low = 0.0
high = 10000
T = (high + low)/2
while abs(sum*T - B) > epsilon:
  if sum*T >= B:
    high = T
    T = (high + low)/2
    if sum*T < B:
      low = T
      T = (high + low)/2
  if sum*T < B:
    low = T
    T = (high + low)/2
    if sum*T >= B:
      high = T
      T = (high + low)/2
T = int(T) + 1
print(T)

