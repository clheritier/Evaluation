import numpy as np
import os

def Conversion_ordinaleScale(nb_rank, selected_rank):
    """ Permet, dans le cas d'une échelle ordinale, la conversion des niveaux sur l'intervalle [0-100]
        nb_rank :  (integer in [2,6] est le nombre de niveaux (entre 2 et 6) définis pour l'echelle
        selected_rank : (integer in [2,6]) est l'évaluation faite sur cette echelle pour une alternative
        retourne la valeur convertie  """


    mid_interval = 100/(nb_rank*2)
    converted_scale = np.empty((0,nb_rank))
    converted_scale = np.append(converted_scale, mid_interval)
    for i in range(1, nb_rank):
        niveau = mid_interval + ( 2*i * mid_interval )
        converted_scale = np.append(converted_scale, niveau)
        i+=1

    converted_selected_rank = converted_scale[(selected_rank-1)]
    #(converted_scale)
    #print(converted_selected_rank)
    return converted_selected_rank





def Conversion_score(n,a,F):
    """permet de convertir le vector de score de a en fonction de la définition des critères i.e. type echelle ordinale/continue, sens de variation.
    la première boucle for converti le score gj(a) sur une echelle [0-100] si le critère j a une echelle ordinale
    la seconde boucle for teste si sur le critère j le score doit etre maximisé ou minimisé, s'il doit être minimisé alors gj(a) = (-1)*gj(a)

    n : (integer) nombre de critères dans le famille de critères F
    a : (np array) score de l'alternative a sur les critères
    F : (array of lists) chaque liste contient la description d'un critère de la forme suivante :
                ('maximize/minimize', 'continue', min, max) ou ('maximize/minimize', 'ordinale', nb_rank)
                e.g F= np.array([['maximize', 'continue',50,300 ],['maximize', 'ordinale',6 ],['minimize', 'continue', 0,20],['minimize', 'ordinale', 4]],dtype=object)"""

    a_converted = a
    for i in range (0,n):
        if F[i][1] == 'ordinale':
            a_converted[i]= Conversion_ordinaleScale(F[i][2],a[i])

    for i in range (0,n):
        if F[i][0] == 'minimize':
            a_converted[i]= a[i]*(-1)

    return a_converted







#### test des fonctions ####
if __name__ == "__main__":


    converted_rank = Conversion_ordinaleScale(4,2)
    print(converted_rank)

    F = np.array([['maximize', 'continue', 50, 300], ['maximize', 'ordinale', 6], ['minimize', 'continue', 0, 20],
                  ['minimize', 'ordinale', 4]], dtype=object)

    evaluation_mission = np.array([70, 5, 12, 2])

    mission_converti = Conversion_score(4, evaluation_mission, F)
    print(mission_converti)
    print(evaluation_mission)

    os.system("pause")