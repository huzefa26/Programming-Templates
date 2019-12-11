# for multiple queries in O(logn)
import math as mt
MAXN = 100001
spf = [0 for i in range(MAXN)]
def sieve():
	spf[1] = 1
	for i in range(2, MAXN):
		spf[i] = i
	for i in range(4, MAXN, 2):
		spf[i] = 2
	for i in range(3, mt.ceil(mt.sqrt(MAXN))):
		if (spf[i] == i):
			for j in range(i * i, MAXN, i):
				if (spf[j] == j):
					spf[j] = i

def getFactorization(x):
	ret = list()
	while (x != 1):
		ret.append(spf[x])
		x = x // spf[x]
	return ret

sieve()
x = 12246
p = getFactorization(x)

# in O(root n)
import math 
def primeFactors(n): 
	while n % 2 == 0: 
		print 2, 
		n = n / 2
	for i in range(3,int(math.sqrt(n))+1,2): 
		while n % i== 0: 
			print i, 
			n = n / i 
	if n > 2: 
		print n 

n = 315
primeFactors(n)