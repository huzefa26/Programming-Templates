from numpy import matmul
mat = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 1, 0, 0], [4, 0, 1, 0,0], [0, 0, 0, 0, 0]]
sums = [sum(i) for i in mat]
for i in range(len(mat)):
	for j in range(len(mat)):
		if mat[i][j]:
			mat[i][j] /= sums[i]
rank = [1/len(mat)]*len(mat)
print(mat, rank)
for i in range(10):
	rank = matmul(mat, rank)
	print(rank)
print(rank)