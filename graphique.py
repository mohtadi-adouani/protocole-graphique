import matplotlib.pyplot as plt
import random
#centre du de la figure

Cx = 0
Cy = 0

#Fonction qui affiche un tableu
#IN : un entier
#OUT : tun tableu de n entier random compris entre 0 et 1
def getTab(n):
    tab = []
    for i in range(n):
        tab.append(random.randint(0, 1))
    return tab

#Fonction qui trace les cercles
#IN : Tableau d'entier
#OUT : Protocole compose de cercles
def printTab(tab):
    temp = ''
    ct = 0
    for i in tab:
        temp = temp + ' '+str(i)
        if ct == 4:
            temp = temp + '\n'
    print(temp)

#Fonction qui affiche un tableau
#IN : Tableau d'entier
#OUT : tous les entier de ce tableau
def trace(tab):
    global Cx
    global Cy
    temp = 1
    figure, axes = plt.subplots()
    draw_circle = plt.Circle((Cx, Cy), 0.3,fill=False,  color='red')#On trace le cercle de depart
    axes.add_artist(draw_circle)
    draw_circle = plt.Circle((Cx, Cy), 0.3+temp*0.1,fill=False, color='red')#On trace le cercle qui affiche le decalage
    axes.add_artist(draw_circle)
    temp = 2
    #On commence a tracer l'information
    for i in tab:
        if(i > 0):
            draw_circle = plt.Circle((Cx, Cy), 0.3+temp*0.1,fill=False)
            axes.add_artist(draw_circle)
        temp = temp + 1


    plt.xlim(-0.5-0.1*temp,0.5+temp*0.1)
    plt.ylim(-0.5-0.1*temp,0.5+temp*0.1)
    axes.set_aspect(1)
    axes.add_artist(draw_circle)
    plt.title('Protocole Graphique')
    plt.show()



tab = getTab(128)
printTab(tab)
trace(tab)
