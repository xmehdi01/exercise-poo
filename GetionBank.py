class GestionB:
    def __init__(self, ncompte, nomclient, ns):
        self.ncompte = ncompte
        self.nomclient = nomclient
        self.ns = ns
    def Versement(self,v):
        self.ns = self.ns + v
        return self.ns
    
    def Retrait(self,r):
        if r<=self.ns :
            self.ns = self.ns - r
            return self.ns
        #else:
            #self.ns = ("Solde insuffisant")

    def afficher(self):
        print("Le numero de compte est :", self.ncompte)
        print("Le nom de client est :", self.nomclient)
        print("Le solde est :", self.ns)
    # Better way to represent an object is using __str__ or __repr__
    def __str__(cls):
        return "Mr. "+self.nomclient+" n° de compte: "+self.ncompte+" votre solde "+str(self.ns)+" MAD."
"""
g1 = GestionB("5133131331","Simohamed",5000)
g1.Versement(300)
g1.Retrait(1000)
g1.afficher()
"""
g1 = GestionB("5133131331","Mehdi",99999999)
print(g1) #"Mr. Mehdi n° de compte: 5133131331 votre solde 99999999 MAD."
g1.Versement(1)
print(g1) #"Mr. Mehdi n° de compte: 5133131331 votre solde 100000000 MAD."
g1.Retrait(99999999)
print(g1) #"Mr. Mehdi n° de compte: 5133131331 votre solde 1 MAD."
