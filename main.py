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
    # I.8. Ordonner la liste
    print("\n--------------Ordonner la liste-------------\n")
    chaine.sort()
    print(chaine)
    # I.9. Affichage de la liste en sens inverse
    print("\n----------------I.9. Affichage de la liste en sens inverse-----------------------\n")
    chaine.reverse()
    print(chaine)
    # I.10. Vider la liste
    print("\n-------------I.10. Vider la liste--------------------\n")
    chaine.clear()
    print(chaine)
    # I.11. Suppression de la liste
    print("\n------------------I.11. Suppression de la liste-------------\n")
    del chaine
    #print(chaine)
    
    # II. Creation d'une tuple avec 10 elements de type entier
    print("\n*********************II. Creation d'une tuple avec 10 elements de type entier*************\n")
    ent = (14, 4, 100, 0, 45, 89, 67, 28, 6, 345)
    # Affichage des elements de la tuple
    print("\n--------------------------Affichage des elements de la tuple--------------------\n")
    print(ent)
    # II.1. Afficher le nombre de fois que la valeur 3 apparait dans la tuple
    print("\n-------------------II.1. Afficher le nombre de fois que la valeur 3 apparait dans la tuple-----------------------------\n")
    print("Le nombre d'occurrences de 3 est de: ",ent.count(3))
    # II.2. Affichage du contenu de l'element numero 5
    print("\n--------------------II.2. Affichage du contenu de l'element numero 5---------------\n")
    print(ent[4])
    # II.3. Ordonner la tuple
    print("\n---------------- II.3. Ordonner la tuple----------------------\n")
    ent = tuple(sorted(ent))
    print(ent)
    # II.4. Ajout d'un element a la fin de la tuple
    print("\n------------------------II.4. Ajout d'un element a la fin de la tuple-------------------\n")
    # Une tuple etant inchangeable on la convertit en une liste 
    ent_list = list(ent)
    # Cette fois on peut ajouter un element a la fin car une liste est changeable
    ent_list.append(143)
    # Reconversion la liste en tuple
    ent = tuple(ent_list)
    print(ent)
    # II.5. Ajout d'un element a l'index au numero 3 de la tuple
    print("\n------------------------Ajout d'un element a l'index au numero 3 de la tuple------------\n")
    # Conversion de la tuple en liste et ajout de l'element a l'index num 3
    ent_nouveau_list = list(ent)
    ent_nouveau_list.insert(3, 3)
    # Reconversion de la liste en tuple
    ent = tuple(ent_nouveau_list)
    print(ent)
    # II.6. Affichage de la nouvelle tuple
    print("\n-------------------------II.6. Affichage de la nouvelle tuple------------------\n")
    print(ent)
    
    # III. Creation d'un set de 10 elements de type chaine de caracteres
    print("\n********************* III. Creation d'un set de 10 elements de type chaine de caracteres***********\n")
    chaine_set = {"Janvier", "Fevrier", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout", "Septembre", "Octobre"}
    # III. 1. Affichage du set
    print("\n-----------------III. 1. Affichage du set------------------\n")
    print(chaine_set)
    # III.2. Ajout d'un element
    print("\n-------------------III.2. Ajout d'un element---------------------\n") 
    chaine_set.add("Novembre")
    print(chaine_set)
    # III.3. Suppression d'un element
    print("\n-----------------------III.3. Suppression d'un element----------------------\n")
    chaine_set.remove("Mai")
    print(chaine_set)
    # III.4. Suppression du set
    print("\n-----------------------III.4. Suppression du set---------------------------\n")
    del chaine_set
    
    # IV. Creation d'un dictionnaire avec 10 elements de type chaine de caracteres
    print("\n********************************IV. Creation d'un dictionnaire avec 10 elements de type chaine de caracteres*********************\n")
    chaine_dict = {
      "v": "vrai",
      "f": "faux",
      "rs": "rien a signaler",
      "hs": "hors service",
      "cad": "c'est a dire",
      "bg": "beau gosse",
      "bcbg": "bon chic bon genre",
      "bcp": "beaucoup",
      "rn": "right now",
      "mm": "meme",
    }
    # IV.1. Affichage du dictionnaire
    print("\n-----------------IV.1. Affichage du dictionnaire---------------------\n")
    print(chaine_dict)
    # IV.2. Affichage des cles
    print("\n---------------------------IV.2. Affichage des cles---------------------\n")
    print(chaine_dict.keys())
    # IV.3. Affichage des valeurs
    print("\n---------------------------IV.3. Affichage des valeurs---------------------\n")
    print(chaine_dict.values())
    # IV.4. Affichage des cles et des valeurs sous le format: cle: valeur
    print("\n---------------------------IV.4. Affichage des cles et des valeurs sous le format: cle: valeur----------------------\n")
    for k,v in chaine_dict.items():
       print(f"{k} : {v}")