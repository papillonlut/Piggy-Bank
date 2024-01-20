def choix_recomptage(): # Première fonction permetant le recomptage
    # Initialiser les variables pour chaque type de billet ou pièce
    billet_500 = int(input("Entrez le nombre de billet(s) de 500€ : "))
    billet_200 = int(input("Entrez le nombre de billet(s) de 200€ : "))
    billet_100 = int(input("Entrez le nombre de billet(s) de 100€ : "))
    billet_50 = int(input("Entrez le nombre de billet(s) de 50€ : "))
    billet_20 = int(input("Entrez le nombre de billet(s) de 20€ : "))
    billet_10 = int(input("Entrez le nombre de billet(s) de 10€ : "))
    billet_5 = int(input("Entrez le nombre de billet(s) de 5€ : "))
    piece_2 = int(input("Entrez le nombre de pièce(s) de 2€ : "))
    piece_1 = int(input("Entrez le nombre de pièce(s) de 1€ : "))
    cent_50 = int(input("Entrez le nombre de pièce(s) de 0.50€ : "))
    cent_20 = int(input("Entrez le nombre de pièce(s) de 0.20€ : "))
    cent_10 = int(input("Entrez le nombre de pièce(s) de 0.10€ : "))
    cent_05 = int(input("Entrez le nombre de pièce(s) de 0.05€ : "))
    cent_02 = int(input("Entrez le nombre de pièce(s) de 0.02€ : "))
    cent_01 = int(input("Entrez le nombre de pièce(s) de 0.01€ : "))

    # Calculer le montant total
    first_montant = (billet_500 * 500) + (billet_200 * 200) + (billet_100 * 100) + \
                    (billet_50 * 50) + (billet_20 * 20) + (billet_10 * 10) + \
                    (billet_5 * 5) + (piece_2 * 2) + piece_1

    second_montant = (cent_50 * 0.50) + (cent_20 * 0.20) + (cent_10 * 0.10) + (cent_05 * 0.05) + (cent_02 * 0.02) + (cent_01 * 0.01)

    montant_total = first_montant + second_montant

    # Afficher le montant total
    print("Le montant total est de {}€.".format(montant_total))

    # Ouvrir le fichier en écriture ('w')
    with open('value', 'w') as fichier:
        # Écrire le montant total dans le fichier
        fichier.write(str(montant_total))

    print("Le montant total enregistré.")
def choix_add_comptage(): # Deuxième fonction permetant l'ajout
    # Initialiser les variables pour chaque type de billet ou pièce
    billet_500 = int(input("Entrez le nombre de billet(s) de 500€ : "))
    billet_200 = int(input("Entrez le nombre de billet(s) de 200€ : "))
    billet_100 = int(input("Entrez le nombre de billet(s) de 100€ : "))
    billet_50 = int(input("Entrez le nombre de billet(s) de 50€ : "))
    billet_20 = int(input("Entrez le nombre de billet(s) de 20€ : "))
    billet_10 = int(input("Entrez le nombre de billet(s) de 10€ : "))
    billet_5 = int(input("Entrez le nombre de billet(s) de 5€ : "))
    piece_2 = int(input("Entrez le nombre de pièce(s) de 2€ : "))
    piece_1 = int(input("Entrez le nombre de pièce(s) de 1€ : "))
    cent_50 = int(input("Entrez le nombre de pièce(s) de 0.50€ : "))
    cent_20 = int(input("Entrez le nombre de pièce(s) de 0.20€ : "))
    cent_10 = int(input("Entrez le nombre de pièce(s) de 0.10€ : "))
    cent_05 = int(input("Entrez le nombre de pièce(s) de 0.05€ : "))
    cent_02 = int(input("Entrez le nombre de pièce(s) de 0.02€ : "))
    cent_01 = int(input("Entrez le nombre de pièce(s) de 0.01€ : "))

    # Calculer le montant total
    first_montant_add = (billet_500 * 500) + (billet_200 * 200) + (billet_100 * 100) + \
                    (billet_50 * 50) + (billet_20 * 20) + (billet_10 * 10) + \
                    (billet_5 * 5) + (piece_2 * 2) + piece_1

    second_montant_add = (cent_50 * 0.50) + (cent_20 * 0.20) + (cent_10 * 0.10) + (cent_05 * 0.05) + (cent_02 * 0.02) + (cent_01 * 0.01)

    montant_total_add = first_montant_add + second_montant_add

    # Lire la valeur actuelle dans le fichier
    with open('value', 'r') as fichier:
        valeur_actuelle = float(fichier.read())

    # Additionner la valeur actuelle avec la valeur entrée
    nouvelle_valeur_add = valeur_actuelle + montant_total_add

    # Mettre à jour la nouvelle valeur dans le fichier
    with open('value', 'w') as fichier:
        fichier.write(str(nouvelle_valeur_add))

    print("La nouvelle valeur est de {}€.".format(nouvelle_valeur_add))
def choix_del_comptage(): # Troisième fonction permetant le retrait
    # Initialiser les variables pour chaque type de billet ou pièce
    billet_500 = int(input("Entrez le nombre de billet(s) de 500€ : "))
    billet_200 = int(input("Entrez le nombre de billet(s) de 200€ : "))
    billet_100 = int(input("Entrez le nombre de billet(s) de 100€ : "))
    billet_50 = int(input("Entrez le nombre de billet(s) de 50€ : "))
    billet_20 = int(input("Entrez le nombre de billet(s) de 20€ : "))
    billet_10 = int(input("Entrez le nombre de billet(s) de 10€ : "))
    billet_5 = int(input("Entrez le nombre de billet(s) de 5€ : "))
    piece_2 = int(input("Entrez le nombre de pièce(s) de 2€ : "))
    piece_1 = int(input("Entrez le nombre de pièce(s) de 1€ : "))
    cent_50 = int(input("Entrez le nombre de pièce(s) de 0.50€ : "))
    cent_20 = int(input("Entrez le nombre de pièce(s) de 0.20€ : "))
    cent_10 = int(input("Entrez le nombre de pièce(s) de 0.10€ : "))
    cent_05 = int(input("Entrez le nombre de pièce(s) de 0.05€ : "))
    cent_02 = int(input("Entrez le nombre de pièce(s) de 0.02€ : "))
    cent_01 = int(input("Entrez le nombre de pièce(s) de 0.01€ : "))

    # Calculer le montant total
    first_montant_del = (billet_500 * 500) + (billet_200 * 200) + (billet_100 * 100) + \
                    (billet_50 * 50) + (billet_20 * 20) + (billet_10 * 10) + \
                    (billet_5 * 5) + (piece_2 * 2) + piece_1

    second_montant_del = (cent_50 * 0.50) + (cent_20 * 0.20) + (cent_10 * 0.10) + (cent_05 * 0.05) + (cent_02 * 0.02) + (cent_01 * 0.01)

    montant_total_del = first_montant_del - second_montant_del

    # Lire la valeur actuelle dans le fichier
    with open('value', 'r') as fichier:
        valeur_actuelle = float(fichier.read())

    # Calculer la nouvelle valeur en fonction du signe de montant_total_del
    nouvelle_valeur_del = max(0, valeur_actuelle - abs(montant_total_del))

    # Mettre à jour la nouvelle valeur dans le fichier
    with open('value', 'w') as fichier:
        fichier.write(str(nouvelle_valeur_del))

    print("La nouvelle valeur est de {}€.".format(nouvelle_valeur_del))
def choix_reset(): # Quatrième fonction permetant la remise à zéro
    # Lire la valeur actuelle dans le fichier
    with open('value', 'r') as fichier:
        valeur_actuelle = float(fichier.read())
        ready = input(f"Êtes-vous sûr de vouloir supprimer {valeur_actuelle}€ (y/n): ")

    if ready.lower() == "y":
        # Mettre à jour la nouvelle valeur dans le fichier (remettre à zéro)
        with open('value', 'w') as fichier:
            fichier.write("0")

        print("TOUT votre argent a été supprimé.")
    else:
        print("L'opération a été annulée.")
    
print("Salut, je suis 'Piggy Bank' ta tirelire numérique.")
print("\nTes différents choix possible:\n0. Quitter.\n1. Recompter tout.\n2. Rajouter de l'argent.\n3. Retirer de l'argent.\n4. Remettre à zéro.")
choix = int(input("Que voulez-vous faire ? "))

if choix == 1:
    choix_recomptage()
elif choix == 2:
    choix_add_comptage()
elif choix == 3:
    choix_del_comptage()
elif choix == 4:
    choix_reset()