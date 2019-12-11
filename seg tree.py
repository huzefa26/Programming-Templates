t=[None]*2*7
inf=10**9+7
def build_generator(a, v, start, end):
    if start == end:
        t[v] = a[start]
    else:
        mid = (start + end) / 2
        next(build_generator(a, v * 2, start, mid))
        next(build_generator(a, v * 2 + 1, mid + 1, end))
        t[v] = min(t[2 * v], t[2 * v + 1])
    yield t



def range_minimum_query_generator(node,segx,segy,qx,qy):
    if qx > segy or qy < segx:
        yield inf
    elif segx >= qx and segy <= qy:
        yield t[node]
    else:
        min_ = min(
            next(range_minimum_query_generator(node*2,segx,(segx+segy)/2,qx,qy)),
            next(range_minimum_query_generator(node*2+1,((segx+segy)/2)+1,segy,qx,qy))
        )
        yield min_


n,k = map(int,raw_input().split())
a = map(int,raw_input().split())
next(build_generator(a,1,0,n-1))
q = 0
for i in range(n):
    for j in range(i,n):
        if a[i] + a[j] <k:
            x = next(range_minimum_query_generator(1, 1, n, i+1, j+1))
            if a[i] + a[j] + x <=k:
                q+=1
print q
print xz