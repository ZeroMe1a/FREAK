from math import gcd, lcm
from time import perf_counter_ns as counter


def simp(f):

	t = counter()

	g = gcd(f[0], f[1])

	f[0] = f[0] // g
	f[1] = f[1] // g

	return [f[0], f[1], counter()-t]


def add(f1, f2):

	t = counter()

	if f1[1] == f2[1]:
		return [f1[0]+f2[0], f1[1], counter()-t]
	
	else:
		mmc = lcm(f1[1], f2[1])

		f1[0] = mmc//f1[1]*f1[0]
		f2[0] = mmc//f2[1]*f2[0]
		
		return [f1[0]+f2[0], mmc, counter()-t]


def sub(f1, f2):

	t = counter()

	if f1[1] == f2[1]:

		if max(f1[0], f2[0]) - min(f1[0], f2[0]) <= 0:
			return [1, f1[1], counter()-t]

		else:
			return [max(f1[0], f2[0])-min(f1[0], f2[0]), f1[1], counter()-t]

	elif f1[1] != f2[1]:
		mmc = lcm(f1[1], f2[1])

		f1[0] = mmc//f1[1]*f1[0]
		f2[0] = mmc//f2[1]*f2[0]

		if max(f1[0], f2[0]) - min(f1[0], f2[0]) <= 0:
			return [1, mmc, counter()-t]
		else:
			return [max(f1[0], f2[0]) - min(f1[0], f2[0]), mmc, counter()-t]


def mul(f1, f2):
	t = counter()
	return [f1[0]*f2[0], f1[1]*f2[1], counter()-t]
