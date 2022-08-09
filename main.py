from random import randint

jogada = set()
# No ciclo do while vou utilizar um set para que nao haja numeros repetidos
while True:
    if len(jogada) < 6:
        jogada.add(randint(1,60))
    else:
        break

# Passando de set para lista para ordernar em ordem crescente
lista = []
for v in jogada:
    lista.append(v)

lista.sort()
print(f'Os números são: {lista}')