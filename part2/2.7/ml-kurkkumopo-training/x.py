import random

n = 1000

in_a = 0

for _ in range(n):
	x = random.random() * 2
	y = random.random() * 4
	if y > x*x:
		in_a += 1

print(in_a)