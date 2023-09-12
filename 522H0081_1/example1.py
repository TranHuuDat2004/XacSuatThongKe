import itertools

E = {'a', 'b', 'c', 'd'}
k = 3

# Print all the k-permutations of E
n = len(E)
permute_k = list(itertools.permutations(E, k))  # chinh hop P(so_duoi, so_tren)
print("%i-permutations of %s: " %(k,E))
for i in permute_k:
    print(i)

print("Size = ", "%i!/(%i-%i)! = " %(n,n,k), len(permute_k)) #"Size = ", "%i!/(%i-%i)! = " %(n,n,k) truyen tham so lan luot vao
# Size =  4!/(4-3)! =  24