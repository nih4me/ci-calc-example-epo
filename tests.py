from functions import *

# Attention: Nom de function doit commencer par `test_`

def test_addition():
    # Test d'addition
    num1 = 5
    num2 = 3
    resultat = addition(num1, num2)
    assert resultat == 8, f"Erreur lors de l'addition : {num1} + {num2} != 8"

def test_soustraction():
    # Test de soustraction
    num1 = 10
    num2 = 4
    resultat = soustraction(num1, num2)
    assert resultat == 6, f"Erreur lors de la soustraction : {num1} - {num2} != 6"

def test_multiplication():
    # Test de multiplication
    num1 = 6
    num2 = 5
    resultat = multiplication(num1, num2)
    assert resultat == 30, f"Erreur lors de la multiplication : {num1} * {num2} != 30"

    num1 = 10
    num2 = 5
    resultat = multiplication(num1, num2)
    assert resultat == 50, f"Erreur lors de la multiplication : {num1} * {num2} != 50"

def test_division():
    # Test de division
    num1 = 15
    num2 = 3
    resultat = division(num1, num2)
    assert resultat == 5, f"Erreur lors de la division : {num1} / {num2} != 5"

def test_division_zero():
    # Test de division par zéro
    num1 = 8
    num2 = 0
    resultat = division(num1, num2)
    assert resultat is None, f"Erreur lors de la division par zéro : {num1} / {num2} devrait être None"
