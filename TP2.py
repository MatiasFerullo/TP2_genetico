from itertools import combinations

def densitySort(x):
    return x[1]/x[0]

def sumSort(x):
    return sum(item[1] for item in x)


def greedy(objetos, limite):

    objSorted = sorted(objetos, key=densitySort)
    robados = []
    volumen = 0
    valor = 0

    for obj in objSorted:
        if obj[0] < (limite - volumen):
            volumen += obj[0]
            valor += obj[1]
            robados.append(obj)

    print("Por algoritmo \"greedy\": ")
    print("Combinacion:", robados)
    print("Volumen:", volumen)
    print("Valor:", valor)
    


def exhaustivo(objetos, limite):
    combinaciones = []

    for r in range(1, len(objetos)+1 ):
        for comb in combinations(objetos, r):
            if sum(x[0] for x in comb) <= limite:
                combinaciones.append(comb)

    combinacionesSorted = sorted(combinaciones, key=sumSort)
    print("Por algoritmo exahustivo: ")
    print("Combinacion:", combinacionesSorted[-1])
    print("Volumen:", sum(x[0] for x in combinacionesSorted[-1]))
    print("Valor:", sum(x[1] for x in combinacionesSorted[-1]))


lista1 = [[150, 20], [325, 40], [600, 50], [805, 36], [430, 25]
           ,[1200, 64], [770, 54], [60, 18], [930, 46], [353, 28]]

lista2 = [[1800, 72], [600, 36], [1200, 60]]

greedy(lista1, 4200)
print()
exhaustivo(lista1, 4200)
print("\n", "=========================", "\n")
greedy(lista2, 3000)
print()
exhaustivo(lista2, 3000)
