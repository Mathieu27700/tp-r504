import fonctions as f

while True:
        a=int(input("Entrez le premier nombre (base entière) : "))
        b=int(input("Entrez le second nombre (exposant entier) : "))

        res = f.puissance(a, b)

        print(f"{a} à la puissance {b} donne {res}\n")


