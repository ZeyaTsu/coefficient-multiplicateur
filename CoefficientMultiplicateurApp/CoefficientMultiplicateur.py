import math
# setup
def start():
    result = None
    prix = float(input("Entrez le prix en Euros /!\ '.' et non ',' si décimale. = "))
    print("Votre prix a baissé ou augmenté ?")
    
    s = True
    while s:
        augmente_baisse = str(input("BAISSE ou AUGMENTATION : "))
 
# Programme Calcul
        if augmente_baisse == "BAISSE":
            baisse = float(input("De combien de pourcentage le prix a baissé ? "))
            result = prix * (1 - (baisse/100))
            print("Le prix revient donc à", result, "€")
            restart()
            s = False
        if augmente_baisse == "AUGMENTATION":
            baisse = float(input("De combien de pourcentage le prix a augmenté ? "))
            result = prix * (1 + (baisse/100))
            print("Le prix revient donc à", result, "€")
            restart()
            s = False
# relancer
def restart():
    print("Voulez-vous relancer le programme ?")
    ch = str(input("OUI ou QUIT"))
    if ch == "OUI":
        start()
    if ch == "QUIT":
        print("Au revoir.")
start()


  


