import random
import string

# Ensembles de caractères
majuscules = string.ascii_uppercase
minuscules = string.ascii_lowercase
chiffres = string.digits
speciaux = string.punctuation

def generer_mot_de_passe(longueur, maj, min, chiff, spec):
    caracteres = ''
    if maj:
        caracteres += majuscules
    if min:
        caracteres += minuscules
    if chiff:
        caracteres += chiffres
    if spec:
        caracteres += speciaux

    if not caracteres:
        return "Erreur: Aucun type sélectionné"

    mot_de_passe = ''.join(random.choice(caracteres) for _ in range(longueur))
    return mot_de_passe

def evaluer_force(mdp):
    types = sum([
        any(c in majuscules for c in mdp),
        any(c in minuscules for c in mdp),
        any(c in chiffres for c in mdp),
        any(c in speciaux for c in mdp)
    ])
    if types <= 1:
        return "Faible"
    elif types == 2:
        return "Moyen"
    else:
        return "Fort"

while True:
    print("\nGénérateur de mot de passe simple")

    try:
        longueur = int(input("Longueur (8-20): "))
        if not 8 <= longueur <= 20:
            print("Entre 8 et 20")
            continue
    except:
        print("Nombre invalide")
        continue

    print("Types:")
    maj = input("Majuscules (o/n): ").lower() == 'o'
    min = input("Minuscules (o/n): ").lower() == 'o'
    chiff = input("Chiffres (o/n): ").lower() == 'o'
    spec = input("Spéciaux (o/n): ").lower() == 'o'

    if not any([maj, min, chiff, spec]):
        print("Au moins un type")
        continue

    mdp = generer_mot_de_passe(longueur, maj, min, chiff, spec)
    print(f"Mot de passe: {mdp}")
    print(f"Force: {evaluer_force(mdp)}")

    if input("Nouveau? (o/n): ").lower() != 'o':
        break
