import numpy as np


#create A

#A: 10x10
A = np.random.randint(0, 101, (10, 10)) 

#B: 2x10
B = np.random.randint(0, 20, (2, 10))

#C : 10x2
C = np.random.randint(0, 20, (10, 2))

#a) calculate  
print("-------------------- a ---------------------")
a = A + A.T + C.dot(B) + (B.T).dot(C.T)
print("a = \n", a)

#b) calculate
print("-------------------- b ---------------------")
b = [0]
print("A = \n", A)
for i in range(10, 20):
    for j in range(1, 11):
        b = b + (A/i)**j
np.array(b)  
print("b = \n", b)

print("-------------------- c ---------------------")

# Save odd rows of the A A into a new A, and print the resultant A to 
# the screen

c = A[0:10:2, :]
print(A)
print(" c = \n",c)

print("-------------------- d ---------------------")

d = A[A%2 != 0]
print(A)
np.array(d)

print("d = \n",d)

print("-------------------- e ---------------------")
# Save prime numbers in the A A into a new vector, and print the resultant 
# vector to the screen


def isPrime(n):
  if n <= 1:
    return False
  for i in range(2, int(n**0.5)+1):
    if n % i == 0:
      return False
  return True

e = []
for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        if ( isPrime (A[i, j]) == True ):
            e.append(A[i, j])


print(A)
np.array(e)
print("e = \n", e)




print("-------------------- f ---------------------")
# Given a A , reverse elements in the odd rows of the A D, and 
# print the resultant A to the screen.
#  A_rev.append(np.flip(A[i], axis = -1))

D = C.dot(B)
print(" D = \n ", D)

D_rev = []
for i in range(D.shape[0]):
        if ((i == 0) or (i % 2 == 0)):
            D_rev.append(np.flip(D[i], axis = -1))
        else:
            D_rev.append(D[i])

res = np.array(D_rev)
print(res)



print("-------------------- g ---------------------")
#  Regarding the A A, find the rows which have maximum count of prime 
# numbers, and print the rows to the screen.

maxCount = 0
resultant = []
for row in A:
    count = 0
    print("row: ", row)
    for num in row:
        if( isPrime(num) == True ):
            count += 1

   
    if (count > maxCount):
        maxCount = count
        resultant = [row]
    elif ( count == maxCount ):
        resultant.append(row)

print("Rows with maximum count of prime numbers:")
np.array(resultant)
for row in resultant:
    print(row)


print("----------------------------- h -----------------------------")
#  Regarding the A A, find the rows which have the longest contiguous odd
# numbers sequence, and print the rows to the screen.

   

print("A \n", A)


maxCount = 0
results = []
for i in range (A.shape[0]):
    count = 0
    for j in range (A.shape[1] - 1):
        if (A[i, j + 1] is None):
            continue
        elif( ( A[i, j] % 2 != 0  ) and ( A[i, j + 1] % 2 != 0  ) ):
            count += 1

    if (count > maxCount):
        maxCount = count
        results = [A[i]]
    elif(count == maxCount):
        results.append(A[i])

np.array(results)
print("the rows which have the longest contiguous odd numbers sequence: ")
for row in results:
    print(row)



    
