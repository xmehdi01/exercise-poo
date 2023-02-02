class Calcul:
    
    def __init__(self,n):
        self.nombre = n
        self.facto = 1
        self.tab = []
    def fact(self):
        for i in range(self.nombre,0,-1):
            self.facto *= i
        return(self.facto)
    def listeDiviseur(self):
        for i in range(1,self.nombre):
            if (self.nombre%i == 0):
                self.tab.append(i)
        return(self.tab)
    def TestPremier(self):
        ispermier = "Premier"
        for i in range(2,(self.nombre//2)+1):
            if (self.nombre%i==0):
                ispermier = "Non Premier"
        return(ispermier)
ca1 = Calcul(4)
print("La liste diviseur du",4,"est ==>",ca1.listeDiviseur())
print("Le factorielle du",4,"est ==>",ca1.fact())
print("Le nombre",4,ca1.TestPremier())