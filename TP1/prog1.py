import fonctions as f

while True:
    try:
        a = float(input("Entrez le premier nombre (base entière) : "))
        b = float(input("Entrez le second nombre (exposant entier) : "))

        res = f.puissance(a, b)
        print(f"{a} à la puissance {b} donne {res}\n")

    except ValueError as ve:
        print(f"Erreur de valeur : {ve}\n")

    except TypeError as te:
        print(f"Erreur de type : {te}\n")


