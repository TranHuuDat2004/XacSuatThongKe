import itertools

E = {'a', 'b', 'c', 'd'}
k = 3
# Print all the k-combinations of E
n = len(E)
choose_k = list(itertools.combinations(E,k)) # to hop C(so_duoi, so_tren)
print("%i-combinations of %s: " %(k,E))
for i in choose_k:
    print(i)

print("Number of combinations = %i!/(%i!(%i-%i)!) = %i" %(n,k,n,k,len(choose_k))) #truyen tham so lan luot vao
# Number of combinations = 4!/(3!(4-3)!) = 4