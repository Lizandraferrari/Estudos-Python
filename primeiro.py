#Lista de Exercícios 2 – Programas com estruturas de repetição
#1. Escreva um programa que lê 15 valores reais, encontra o maior e o
#  menor deles e mostra o resultado
cont = 0
list = []
for cont in range(15):
    num = int(input('Insira o número desejado: '))
    list.insert(cont , num)
    cont+1
print('O maior número dos inseridos foi: ',max(list))
print('O menor número dos inseridos foi: ',min(list))


