import numpy as np
import matplotlib.pyplot as plt

def generate_points(n,range1=0,range2=10,farver =["red","blue"],test=False):
    points = []
    for i in range(n):
        id = i
        x = np.random.randint(range1,range2)
        y = np.random.randint(range1,range2)
        j = i
        while j > len(farver)-1:
            j -= len(farver)
        color = farver[j]
        if test:
            id = "TESTPUNKT"

        points.append([x,y,color,id])
    return points

def plot_points(points):
    for i in points:
        x = i[0]
        y = i[1]
        color = i[2]
        plt.plot(x,y,'o',color=color)
        plt.text(x,y,i[3])
    plt.show()

def distance(point1,point2):
    x1 = point1[0]
    y1 = point1[1]
    x2 = point2[0]
    y2 = point2[1]
    return np.sqrt((x1-x2)**2 + (y1-y2)**2)

def allDist(points,testpunkt):
    afstande = []
    for point in points:
        
        afstande.append([distance(point,testpunkt[0]),point[2],point[3]])
    return afstande

def bubbleSort(A):
    for i in range(1,len(A)):
        for j in range(0,len(A)-i):
            if A[j][0] > A[j+1][0]:
                tempAj = A[j]
                A[j] = A[j+1]
                A[j+1] = tempAj                   

    return A

def afstande(points,testpunkt):
    dists= []
    for point in range(len(points)):
        dists[point] = [distance(points[point],testpunkt[0]),points[2],points[3]]
    return dists

def nærmesteKPunkter(points,testpunkt,k):
    dists = allDist(points,testpunkt)
    sorteddists = bubbleSort(dists)
    nearK = sorteddists[0:k]
    return nearK

#Denne funktion finder ud af, hvilken farve et givet testpunkt skal være.
#Det gør den ud fra farverne på de k nærmeste naboer i datasættet points.
def hvaFarve(points,testpunkt,k):
    #Der tjekkes om k er et ulige heltal.
    if k%2 != 1:
        print("How du, k skal være et ulige heltal!!!")
        return
    #Der tjekkes om k er for stort.
    elif k > len(points):
        print("hov du, k må ikke være større end mængden af naboer")
        return
    # testpunktets k nærmeste naboer findes.
    bob = nærmesteKPunkter(points,testpunkt,k)
    #print(f"bob er {bob}")
    # dictionariet bobdict oprettes
    bobdict= {}
    # for alle k naboer køres dette loop.
    for i in range(0,k):
        #Vi forsøger at inkrementere værdien til keyen bob[i][1] (bob[i]'s farve) i bobdict.
        try:
            bobdict[bob[i][1]]+=1
        #Hvis det ikke er muligt (f.eks. hvis den key ikke eksisterer), opretter vi en key med det navn.
        except:
            bobdict[bob[i][1]]=1
   
    farve = list(bobdict.keys())[0]
    for key in bobdict.keys():
        if bobdict[key] > bobdict[farve]:
            farve = key
    return farve

def skiftFarve(points,testpoint,k):
    farve = hvaFarve(points,testpoint,k)
    testpoint[0][2] = farve

testPunkter = generate_points(11)
punktK = generate_points(1,farver="green",test=True)



skiftFarve(testPunkter,punktK,3)

plot_points(testPunkter+punktK)