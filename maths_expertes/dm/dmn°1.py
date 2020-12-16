

# Méthode 1 : script du cours :
'''
n = int(input("Choisir la valeur de n : ")) # On injecte depuis la console la valeur que l'on veut
b = int(input("Choisir la valeur de b : "))
d = 0

while n > b:
	d += 1 # (même chose que d = d + 1 : c'est ce qu'on appel en programmation l'incrémentation)
	n -= b # (même chose que n = n - b)
	print(d, n)
'''

# Méthode 2 : le dictionnaire : 

n = int(input("Choisir la valeur de n : ")) # On injecte depuis la console la valeur que l'on veut
b = int(input("Choisir la valeur de b : "))
tableau = {} # Création d'un dictionnaire

while n > b:
	tableau[n] = b # J'attribue à 'n' la clé de valeur 'b'
	n -= b

print("d = ",
 len(tableau), # longueur du dictionnaire = d dans le programme initial
  '\n S =',
   tableau) # Affiche le contenu du dictionaire