from operator import attrgetter

class Camiseta():
    def __init__(self, nome, cor, tamanho):
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho

def ordenacao_multipla(lista, specs):
    for key, reverse in reversed(specs):
        lista.sort(key=attrgetter(key), reverse=reverse)
    return lista

while True:
    loop = int(input())
    if loop == 0 or loop > 60:
        break
    lista = [None] * loop
    cont = 0
    while cont < loop:
        nome = input()
        entrada = input()
        cor, tamanho = entrada.split(" ")
        b = Camiseta(nome, cor, tamanho)
        lista[cont] = b
        cont += 1
    specs = (('cor', False), ('tamanho', True), ('nome', False))  
    aux = ordenacao_multipla(list(lista), specs)
    cont = 0
    while cont < loop:
        print(aux[cont].cor, aux[cont].tamanho, aux[cont].nome)
        cont += 1
    print()  