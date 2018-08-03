
from functions_conversion_criteria import *
import numpy as np
import os



def profiles_approximation(p,F,n):
    """ approximation des profils (uniformes). la fonction retorune les profils approximés dans un array B[h][n] :
            où  h est le nb de profils (un profil de moins que de catégories définies)
                n est le nombre de critères
            e.g B = [ [g1(b1), .., gj(b1), .., gn(b1)],
                      ...
                      [g1(bh), .., gn(bh)]]
        PARAMETRES :
            p : integer, nb. de catégories définies
            n : nb. de critères
            F : (array of lists) chaque liste contient la description d'un critère de la forme suivante :
                ('maximize/minimize', 'continue', min, max) ou ('maximize/minimize', 'ordinale', nb_rank)
                e.g F= np.array([['maximize', 'continue',50,300 ],['maximize', 'ordinale',6 ],['minimize', 'continue', 0,20],['minimize', 'ordinale', 4]],dtype=object)"""

    B = np.empty((p-1,n))

    for i in range(0, p-1):
        for j in range(0, n):
            if F[j][1] == "ordinale":
                if F[j][0] == 'minimize':
                    B[i][j] = -100+((100/p)+ (i*(100/p)))
                else:
                    B[i][j] = (100/p)+ (i*(100/p))
            else:
                delta = F[j][3] - F[j][2]
                if F[j][0] == 'minimize':
                    B[i][j] = ((-1)*delta)+((delta / p) + (i * (delta / p)))
                else:
                    B[i][j] = (delta / p) + (i * (delta / p))

    return B



def veto_approximation(p,F,n):
    """ approximation du seuil de veto (indépendant de g(bh). veto lorsque g(b)-g(a)> 80% de l'intervalle de valueur défini pour le critère"""

    v = np.empty((p-1,n))
    for i in range(0, p - 1):
        for j in range(0, n):
            if F[j][1] == "ordinale":
                v[i][j] = 100*0.8
            else:
                delta = F[j][3] - F[j][2]
                v[i][j] = delta*0.8

    return v



#### test fonction ####
if __name__ == "__main__":

    n = 4

    F = np.array([['maximize', 'continue', 50, 300], ['maximize', 'ordinale', 6], ['minimize', 'continue', 0, 20],
                  ['minimize', 'ordinale', 4]], dtype=object)

    p_categories = 4


    B= profiles_approximation(p_categories,F,n)
    print(B,"\n")
    for i in range(0,(p_categories-1)):
        print(B[i] ,"\n")

    qb = np.absolute(B) * 0.05
    pb = np.absolute(B) * 0.1


    print(qb,"\n")
    print(pb,"\n")

    veto = veto_approximation(p_categories,F,n)
    print(veto)


    os.system("pause")
