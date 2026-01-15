class Triangle:
    def __init__(self, n):
        self.n = n

    def generer(self):
        lignes = []
        for i in range(1, self.n + 1):
            ligne = " " * (self.n - i) + "*" * (2 * i - 1)
            lignes.append(ligne)
        return lignes

class Affichage:
    def __init__(self, triangle1, triangle2):
        self.triangle1 = triangle1
        self.triangle2 = triangle2

    def afficher(self):
        lignes1 = self.triangle1.generer()
        lignes2 = self.triangle2.generer()
        for i in range(len(lignes1)):
            if i < len(lignes1) - 1:
                print(lignes1[i])
            else:
                for j in range(len(lignes2)):
                    if j == 0:
                        print(lignes1[i] + lignes2[j][1:])
                    else:
                        print(" " * (self.triangle1.n - i + j) + lignes2[j])

def main():
    try:
        n = int(input("Saisir un entier n : "))
        if n <= 0:
            print("Veuillez entrer un entier positif.")
            return
        triangle1 = Triangle(n)
        triangle2 = Triangle(n)
        affichage = Affichage(triangle1, triangle2)
        affichage.afficher()
    except ValueError:
        print("Entrée invalide. Veuillez saisir un entier.")

if __name__ == "__main__":
    main()


