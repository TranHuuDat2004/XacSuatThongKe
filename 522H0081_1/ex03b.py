import itertools

Books = {'M1', 'M2', 'M3', 'M4', 'P1', 'P2', 'P3', 'C1', 'C2', 'E1'}
U10 = list(itertools.permutations(Books, 10))
result = []
count = 0
for u in U10:
    name = ''.join([i[0] for i in u])
    if(('M'*4 in name) and ('P'*3 in name) and ('C'*2 in name)):
        count +=  1
print ("count = ",count)