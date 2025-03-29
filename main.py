import random

while True:

    msg = input("lancer le dés ? Tappez la touche ENTRER pour continuer ou tapez N pour quitter: ").lower()
    if msg == "n":
        print("Fin des lancées")
        break
    else:
        nbr = random.randint(0, 6)
        print(f"le nonbre donner est : {nbr}")
