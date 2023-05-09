if __name__ == '__main__':
    # I. Création de la liste avec 10 elements de type chaines de caracteres
    print("***********I. Creation d'une liste de 10 elements de type chaines de caracteres******************\n")
    chaine = ['Table', 'Chaise', 'Carotte', 'Fruits',
               'The', 'Cafe', 'Veloure', 'Pass', 'Classe', 'Mot']
    # I.1. Affichage des elements de la liste 
    print("----1.Affichage des elements de la liste-------------\n")
    print(chaine)
    # I.2. Changement du contenu de l'element numéro 5
    print("\n-------------2. Changement du contenu de l'element numero 5-----------------------\n")
    chaine[4] = 'Velo'
    print(chaine)
    # I.3. Creation d'une nouvelle liste avec les elements de la liste precedente mais contenant la lettre "a"
    print("\n-----3. Creation d'une nouvelle liste avec les elements de la liste precedente mais contenant la lettre a----\n")
    n_chaine = []#creation de la liste qui va accueillir les mots contenant "a"
    #print(type(n_chaine))
    for a in chaine:
      if 'a' in a:
        n_chaine.append(a)
    
    print("Liste de mots contenant a sont:\n",n_chaine)
    # I.4. Ajouter un element a la fin de la liste
    print("\n-------------------------------Ajout d'un element a la fin de la liste--------------------\n")
    chaine.append('Moto')
    print(chaine)
    # I.5. Ajout a l'index numero 2
    print("\n-----------------------I.5. Ajout a l'index numero 2-----------------------------------\n")
    chaine.insert(2, 'Argent')
    print(chaine)
    # I.6. Suppression de l'element numero 3
    print("\n-----------------------I.6. Suppression de l'element numero 3-------------------\n")
    del chaine[2]
    print(chaine)
    # I.7. Suppression de l'element a l'index numero 2
    print("\n-----------------Suppression de l'element a l'index numero 2-----------\n")
    del chaine[2]
    print(chaine)