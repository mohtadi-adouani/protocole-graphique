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
def trace(tab,P):
    global Cx
    global Cy
    pixel = 0.3
    temp = 1
    figure, axes = plt.subplots()
    draw_circle = plt.Circle((Cx, Cy), pixel,fill=False,  color='red')#On trace le cercle de depart
    axes.add_artist(draw_circle)
    draw_circle = plt.Circle((Cx, Cy), pixel+temp*0.1,fill=False, color='red')#On trace le cercle qui affiche le decalage
    axes.add_artist(draw_circle)
    temp = 2
    #On commence a tracer l'information
    for i in tab:
        if(i > 0):
            draw_circle = plt.Circle((Cx, Cy), pixel+temp*0.1,fill=False)
            axes.add_artist(draw_circle)
        temp = temp + 1


    plt.xlim(-0.5-0.1*temp,  0.5+temp*0.1)
    plt.ylim(-0.5-0.1*temp,  0.5+temp*0.1)
    axes.set_aspect(1)
    axes.add_artist(draw_circle)
    plt.title('Pourcentage d efficacitee: '+str(   P    )+' %')
    plt.show()

#Fonction qui converti un char en son nombre ascii
#IN : charactere
#OUT : entier
def charToAscii(char):
    return ord(char)

#Fonction qui converti un entier en un tableu contenant les bits de cet entier
#IN : eniter
#OUT : tableu d'entier correspodant aux bits
def intToBit(n,b=2,verbose=False):
    """retourne sous forme de tableau l'écriture en base b de  l'entier n écrit en base 10"""
    t = []
    if n==0:
        return [0]
    while n>0:
        quotient, reste = n//b,n%b
        if verbose:
            print("%s=%s*%s+%s"%(n,quotient,b,reste))
        t.append(reste)
        n = quotient
    #on renverse le tableau des restes successifs
    t.reverse()
    return t


        
#Fonction qui converti une chaine en un tableu contenant les bits de cette chaine
#IN : str
#OUT : tableu d'entier correspodant aux bits
def strToBit(string):
    tableu = []
    for char in string:
        tableu.extend( intToBit( charToAscii(char) ) )
    
    return tableu


#Fonction qui genere le code de hamming
#IN : tab
#OUT : str
def hamming(tab):
    d = listToString(tab)
    data=list(d)
    data.reverse()
    c,ch,j,r,h=0,0,0,0,[]

    while ((len(d)+r+1)>(pow(2,r))):
        r=r+1

    for i in range(0,(r+len(data))):
        p=(2**c)

        if(p==(i+1)):
            h.append(0)
            c=c+1

        else:
            h.append(int(data[j]))
            j=j+1

    for parity in range(0,(len(h))):
        ph=(2**ch)
        if(ph==(parity+1)):
            startIndex=ph-1
            i=startIndex
            toXor=[]

            while(i<len(h)):
                block=h[i:i+ph]
                toXor.extend(block)
                i+=2*ph

            for z in range(1,len(toXor)):
                h[startIndex]=h[startIndex]^toXor[z]
            ch+=1

    h.reverse()
    print('Hamming code generated would be:- ', end="")
    print(stringToList(h))
    return h


#Fonction qui transforme une liste en str
#IN : tab
#OUT : str
def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += str(ele)  
    
    # return string  
    return str1 

#Fonction qui transforme une str en liste
#IN : str
#OUT : tab
def stringToList(list1):
    str1 = ''.join(str(e) for e in list1)
    return str1
                

    
info = input("Entrez l'information a coder: ")

#On obtien un tab de bit
tab = strToBit(info)

#on genere le Hamming code
H = hamming(tab)
print("Code Hamming : ",H)

#on calculte l'efficacitee
efficacitee = ( len(tab)/len(H) ) * 100

#on trace la figure
trace(H,efficacitee)


print('Efficacitee du protocole : ',efficacitee,'%')




