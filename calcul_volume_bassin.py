'''
Déclaration des variables
'''

An = 800
n = 0
liste = {"A0" : 800}                 # Pour stocker le rang An et sa valeur dans un meme dictionaire 
# file = open("resultats.txt", "w")    # Pour écrire le résultat dans un document texte

'''
Partie logique
'''

while An <= 1300:
    An = (3/4) * An + 330
    n += 1
    liste["A" + str(n)] = An        # Je sauvegarde dans le dictionaire le rang An et sa valeur

'''
Mise en forme de la plage de données
'''


for cle, valeur in liste.items():   # Parcours de chaque rang du dictionaire pour afficher les données
    # file.write("%s  ==>  %5.2f\n" % (cle, valeur))    # Affichage formater des données dans le document texte
    print("l'élément de clé", cle, "vaut", valeur)

# file.write('Le bassin A aura un volume supérieur à 1300 au bout du  %iieme jour.' % (n))
print('Le bassin A aura un volume supérieur à 1300 au bout du ', n, 'ième jour.')

'''
Fermeture du prgramme
'''

# file.close()