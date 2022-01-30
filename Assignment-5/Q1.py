import math

m = 70
sum = 0.
for i in range(1, m):
    sum += math.log(1 + (i / m)**2)
ans = math.log(2)/(2*m) + (1 / m) * sum
print(f"I_num: {ans}")
