def puissance(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Seuls des entiers (int) peuvent être utilisés")

    if b < 0:
        raise ValueError("L'exposant ne peut pas être négatif")

    if a == 0 and b > 0:
        return 0

    result = 1
    for _ in range(b):
        result *= a

    return result

