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
    chaine.insert(5, 'Velo')#insertion du mot au num 5 et non a l'index 
    print(chaine)
    # I.3. Creation d'une nouvelle liste avec les elements de la liste precedente mais contenant la lettre "a"
    print("\n-----3. Creation d'une nouvelle liste avec les elements de la liste precedente mais contenant la lettre a----\n")
    n_chaine = []
    #print(type(n_chaine))
    for a in chaine:
      if 'a' in a:
        n_chaine.append(a)
        
    print("\nListe de mots contenant a sont:\n",n_chaine)
    