revenu = 0
depenses = []

while True:
    print("\n1. Ajouter revenu")
    print("2. Ajouter dépense")
    print("3. Voir solde")
    print("4. Quitter")

    choix = input("Choix : ")

    if choix == "1":
        montant = float(input("Montant revenu : "))
        revenu += montant

    elif choix == "2":
        montant = float(input("Montant dépense : "))
        categorie = input("Catégorie : ")
        depenses.append((montant, categorie))

    elif choix == "3":
        total_depenses = sum(d[0] for d in depenses)
        solde = revenu - total_depenses

        print("Revenu total :", revenu)
        print("Total dépenses :", total_depenses)
        print("Solde :", solde)

        print("\nDépenses par catégorie :")
        categories = {}
        for montant, cat in depenses:
            categories[cat] = categories.get(cat, 0) + montant

        for cat, total in categories.items():
            print(cat, ":", total)

    elif choix == "4":
        break

    else:
        print("Choix invalide")