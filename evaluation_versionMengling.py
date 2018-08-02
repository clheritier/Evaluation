from functions_electre import *
from input_checking import *
from functions_profiles import *
from functions_conversion_criteria import *
from functions_contribution import *
import numpy as np
import random

""" Electre tri with with pessimistic procedure: assign 'a' to one of the p predefined categories (delimited with profiles bh)
    In this version parameters may be provided directly (no input fct used). 
    Parameters to provide depend on the nb of categories and then nb of profiles. 
    /!\ performance on criteria is supposed to be croissant (if not, the performance gj must be negative)
    Parameters are the following:
        p = nb of predefined categories                     int>1
        n = nb of criteria                                  int>0
        cut_level = cutting level                           float in [0.5,1]
        w = weight vector                                   w = np.array([w1, ..., wj, ..., wn]
        a = performance vector of 'a'                       a = np.array([g1(a), ..., gj(a), ..., gn(a)])
      For all h in {1,..p-1}
        b[h] = performance vector of profile 'bh'           B[h] = np.array([g1(bh), ..., gj(bh), ..., gn(bh)])
        qb[h] = vector of indifference threshold  for bh    qb[h] = np.array([q(g1(bh)), ....., q(gn(bh))])
        pb[h] = vector of preference threshold  for bh      pb[h] = np.array([p(g1(bh)), ....., p(gn(bh))])
        vb[h] = vector of veto threshold  for bh            vb[h] = np.array([v(g1(bh)), ....., v(gn(bh))])
        """

### USER INPUTS

n = 4                                       #n : nb of criteria
a = np.array([70,5,12,2])                   #a : performance vector of mission 'a'
F = np.array([['maximize', 'continue',50,300 ],['maximize', 'ordinale',6 ],['minimize', 'continue', 0,20],['minimize', 'ordinale', 4]],dtype=object)


### ELECTRE PARAMETERS

p = 3                                       #p : nb of predefined categories. Fixed here
w = np.random.random(n)                     #w = weight vector. Normally supposed to be inferred, here randomly generated   valeurs comprises entre [0,1[, pas normalisées, elles le sont après
cut_level = random.uniform(0.5, 1)          #cut_level : cutting level lambda. Normally supposed to be inferred, here randomly generated " "veleur entre [0,1[ exclus ?

### /!\ do not modify
h= p-1
#b = np.empty((h,n))
#qb = np.empty((h,n))
#pb = np.empty((h,n))
#vb = np.empty((h,n))

a_convert = Conversion_score(n,a,F)
b = profiles_approximation(p,F,n)           # b[h][n]
qb = np.absolute(b)*0.05                    # qb[h][n]
pb = np.absolute(b)*0.1                     # pb[h][n]
v = veto_approximation(p,F,n)               # v[h][n]


###
approx = True                               # par defaut ici on utilisera l'approximation pour le calcul de cj

cj_ab = np.empty((0, n))
C_ab = []
dj_ab = np.empty((0, n))
rho_ab = []
ab=[]


print('#criteres :',n,'\n')
for i in range (0,n):
    print('Famille de critères, definitions :\n g\t{} :\t{}'.format(i+1,F[i]))
print(
        'Poids : \n',w,'\n',
        '#categories :',p,'\n',
        'Profils :\n',b,'\n',
        'Seuils preference :\n',qb,'\n',
        'Seuils indifference :\n',pb,'\n',
        'Seuils veto (independant de g(bh)) :\n',v,'\n',
        'Seuil de coupe :\n',cut_level,'\n',
        'Score de alternative à evaluer (brut):\n',a,'\n'
        'Score de alternative à evaluer (après conversion):\n',a_convert,'\n'
    )



### 1|Use function electre_3 to compute partial concordance,comprehensive concordance, discordance, credibility,
# outranking for pairs (a,bh) for all h in {1,..,p-1}

for i in range(0,h,1):
    abi = electre_3(a,b[i],qb[i],pb[i],v[i],w,cut_level,approx)
    ab.append(abi)

for i in range(0,h,1):
        print("\n # Partial concordance indices:\n "
              "\t c(a,b{0})={1}\n "
              "# Comprehensive concordance index: \n"
              "\t C(a,b{0})={2}\n "
              " # Discordance indices: \n "
              "\t d(a,b{0})={3}\n "
              "# Credibility index: \n "
              "\t rho(a,b{0})={4}\n "
              "# Outranking with lambda ={5}\n"
              "\t aSb{0} = {6}\n"
              "_________________________________"
              .format((i+1),ab[i][0],ab[i][1],ab[i][2], ab[i][3], cut_level, ab[i][4]))

        # indices 0 to 4, allow to gat the 5 elements contained in the list returned with function electre_3
        #note: if h=2, results are expected for (a,b1) and (a,b2), thus list ab has the following form:
        # ab = [[array1], [array2]]
        # ab = [[[cj(a,b1)], C(a,b1), [dj(a,b1)], rho(a,b1), boolean],
        #       [[cj(a,b2)], C(a,b2), [dj(a,b2)], rho(a,b2), boolean]]]
        # boolean => true means aSb, False means not(aSb)

### 2| Assignment procedure (pessimistic)

for i in range(h,0,-1):
    if ab[i-1][4] == True:   #return boolean S(a,bh) True/false
        print("\n The pessimistic procedure assigns 'a' to category C{}".format((i+1)))
        r = i-1 # return index of profile br such as aSbr
        break
else:
    print("The pessimistic procedure assigns 'a' to category C1 \n") ## on supppose que a surclasse forcement b0
    r=0
    # , et par defaut assigne a la moins bonne des cate c0

### 3| Contribution

