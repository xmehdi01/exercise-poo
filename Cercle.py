pi = 3.14
import math
class Cercle:
    def __init__(self,r):
        self.rayon = r
    def aire(self):
        return(pi*pow(self.rayon, 2))
    def Perimeter(self):
        return (2 * pi * self.rayon)
    def affichage(self):
        print("L'air du rayon est :",self.aire())
        print("Le Perimeter du rayon est :",self.Perimeter())
c1 = Cercle(4)
c1.affichage()
