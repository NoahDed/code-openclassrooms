
# 1) Utilisez une boucle et la fonction "range" pour calculer la somme.
# Testez et récupérez le résultat en faisant tourner le code (> "Run")

for x in range(100):
    print(x)


# 2) Assignez le résultat obtenu dans la variable "solution" pour vérification
solution = 5050

# Ne touchez pas le print ci-dessous :)
print(f"{solution} est la bonne valeur de la somme !" if solution == (100 * 101) / 2 else "Raté")