# Fonction d'addition
def addition(a, b):
    return a + b

# Fonction de soustraction
def soustraction(a, b):
    return a - b

# Fonction de multiplication
def multiplication(a, b):
    return a * b

# Fonction de division
def division(a, b):
    if b != 0:
        return a / b
    else:
        print("Erreur : Division par zéro.")
        return None