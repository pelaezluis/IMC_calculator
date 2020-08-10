"""
imc_calculator, es un programa que calcula tu Indice de Masa Corporal (IMC)
y te indica en que rango te encuentras
"""
from os import system, name

def limpiarPantalla():
    """
    Detecta que OS se está usando para así limpiar la
    pantalla correctamente.
    """
    if name == "posix":
        system ("clear")
    elif name == "ce" or name == "nt" or name == "dos":
        system ("cls")


def entrada_datos():
    """
    Recibe el peso y la estatura de la persona
    """
    print ("\n***** Bienvenido a IMC calculator! *****\n")
    peso = float(input("Ingresa tu peso en kilogramos: "))
    estatura = float(input("Ingresa tu estatura en metros: "))
    return peso, estatura


def calcular_imc(peso, estatura):
    """
    Calcula el IMC
    """
    imc = peso / estatura ** 2

    print ("\n---------------------------------------")
    print ("Tu indice de masa corporal es:", round(imc, 2))
    if (imc < 16):
        print ("\n=> Delgadez severa.")
    elif (imc >= 16 and imc < 17):
        print ("\n=>Delgadez moderada.")
    elif (imc >= 17 and imc < 18.5):
        print ("\n=> Delgadez no pronunciada.")
    elif (imc >= 18.5 and imc < 25):
        print ("\n=> Normal.")
    elif (imc >= 25 and imc < 30):
        print ("\n=> Sobrepeso.")
    elif (imc >= 30 and imc < 35):
        print ("\n=> obesidad tipo I")
    elif (imc >= 35 and imc < 40):
        print ("\n=> obesidad tipo II")
    elif (imc >= 40):
        print ("\n=> obesidad tipo III")
    print ("---------------------------------------")



opcion = 's'

while opcion == 's'.lower():
    limpiarPantalla()
    peso, estatura = entrada_datos()
    calcular_imc(peso, estatura)
    opcion = input('\n>>> Desea calcular el IMC de nuevo? [s/n]: ')

input("\n>>> Presiona una tecla para salir")
limpiarPantalla()
