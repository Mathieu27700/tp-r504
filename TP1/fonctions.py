def puissance(a,b):
	if (not type(a) is int) or (not type(b) is int):
		raise TypeError("seul des int peuvent être allouer")
	if a==0 and b<=0:
		raise ValueError("b ne peut pas être inférieur ou égal à 0 si a est égal à 0")
	return a ** b
