class Outils:
    def __init__(self):
        self.nombres = []

    def saisir(self):
        """Demande à l'utilisateur de saisir 10 entiers."""
        self.nombres = []  # réinitialisation de la liste
        print("Veuillez saisir 10 entiers :")
        for i in range(10):
            while True:
                try:
                    n = int(input(f"Entier {i + 1} : "))
                    self.nombres.append(n)
                    break
                except ValueError:
                    print("Entrée invalide. Veuillez saisir un entier.")
        print("Données saisies avec succès !")

    def min(self):
        """Retourne le plus petit entier sans utiliser de tri."""
        minimum = self.nombres[0]
        for n in self.nombres:
            if n < minimum:
                minimum = n
        return minimum

    def max(self):
        """Retourne le plus grand entier sans utiliser de tri."""
        maximum = self.nombres[0]
        for n in self.nombres:
            if n > maximum:
                maximum = n
        return maximum

    def somme(self):
        """Calcule et retourne la somme des entiers."""
        total = 0
        for n in self.nombres:
            total += n
        return total

    def moyenne(self):
        """Calcule et retourne la moyenne des entiers."""
        return self.somme() / len(self.nombres)

# ---- Programme principal (pour tester la classe) ----
if __name__ == "__main__":
    outils = Outils()
    outils.saisir()
    print("\nRésultats :")
    print("Minimum :", outils.min())
    print("Maximum :", outils.max())
    print("Somme :", outils.somme())
    print("Moyenne :", outils.moyenne())

