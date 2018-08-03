
import numpy as np
import random
from functions_conversion_criteria import *

#valeurs test
n = 4
a = np.array([70,5,12,2])
F= np.array([['maximize', 'continue',50,300 ],['maximize', 'ordinale',6 ],['minimize', 'continue', 0,20],['minimize', 'ordinale', 4]],dtype=object)

### ELECTRE PARAMETERS

p_categories = 3
w = np.random.random(n)
cut_level = random.uniform(0.5, 1)

### /!\ do not modify
h= p_categories-1
b = np.empty((h,n))
qb = np.empty((h,n))
pb = np.empty((h,n))
vb = np.empty((h,n))


q = np.absolute(b)*0.05
p = np.absolute(b)*0.1


def profiles_approximation(p,F,n):

    B = np.empty((p-1,n))

    for i in range(0, p-1):
        for j in range(0, n):
            if F[j][1] == "ordinale":
                B[i][j] = (100/p)+ (i*(100/p))
            else :
                delta = F[j][3]- F[j][2]
                B[i][j] = (delta/p) + (i*(delta/p))
    return(B)

array_profiles = profiles_approximation(3,F,4)

print(array_profiles)


    #def profile_approximation(p,F,n,b):

   # h=p-1

 #   for i in range (0,h):
  #      for j in range (0,n):
  #          if F[j][1] == "ordinale":
  #              b[i][j] = 100
  #          else




"""for i in range(0, p-1):
        for j in range(0, n):
            if F[j][1] == "ordinale":
                B[i][j] = (100/p)+ (i*(100/p))
            else :
                delta = F[j][3]- F[j][2]
                B[i][j] = (delta/p) + (i*(delta/p))

        for j in range (0,n):
            if F[j][0] == 'minimize':
                B[i][j]= B[i][j]*(-1)"""

for j in range(0, n):
    if F[j][0] == 'minimize':
        B[i][j] = B[i][j] * (-1)