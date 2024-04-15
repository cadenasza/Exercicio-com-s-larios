salarios = []
soma = 0
print('-' * 40)
quantidade = int(input('Quantos salários vão ser analisados? '))
print('-' * 40)

for i in range(quantidade):
    salario = float(input('Sálario: R$'))
    salarios.append(salario)
    soma += salario
    i += 1

print()
media = soma / quantidade    
print(f'A média é {media:.2f}')
print('-' * 40)

for salario in salarios:
    if salario < media:
        menor_salario = salario
        print(f'O salario R${menor_salario:.2f} está abaixo da média')
       