class Rectangle():
    def  __init__(self, long, larg):
        self.longeur = long
        self.largeur = larg
    def perimeter(self):
        return((self.longeur + self.largeur) * 2)
    def area(self):
        return((self.longeur * self.largeur))

class Parallelepiped(Rectangle):
    def __init__(self, long, larg, hau):
        Rectangle.__init__(long, larg)
        self.hauteur = hau
    def volume(self):
        return (self.longeur * self.largeur * self.hauteur)

g1 = Rectangle(5, 4)
print(g1.area())