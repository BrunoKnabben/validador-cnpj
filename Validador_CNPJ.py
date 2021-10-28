
cnpj = input('CNPJ: ')

while cnpj.isnumeric():
    break
else:
    cnpj = input('Por favor, informe apenas números: ')
    if not cnpj.isnumeric():
        print('O valor informado não é composto apenas por números.')
        exit()
print()

cnpj_informado = ''
cnpj_valido = ''

formula = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]  # Números para validar os digito do CNPJ

cnpj = [int(x) for x in cnpj]  # Convertendo a variavel cnpj para uma lista de inteiros

aux = cnpj
soma = 0

if len(aux) == 14:
    aux.pop()
    aux.pop()
elif len(aux) == 13:
    aux.pop()

for num in range(0, len(formula), 1):  # faz a multiplicação dos valores CNPJ x Fórmula e obtém sua soma
    soma += (formula[num] * aux[num])

digito_verif = 11 - (soma % 11)
if digito_verif > 9:
    digito_verif = 0
formula.insert(0, 6)
aux.append(digito_verif)

soma = 0
for num in range(0, len(formula), 1):
    soma += (formula[num] * aux[num])

digito_verif = 11 - (soma % 11)
if digito_verif > 9:
    digito_verif = 0
aux.append(digito_verif)

for i in range(0, len(cnpj), 1):
    if i == 2 or i == 5:
        cnpj_informado += '.'
    if i == 8:
        cnpj_informado += '/'
    if i == 12:
        cnpj_informado += '-'
    cnpj_informado += str(aux[i])

for i in range(0, len(aux), 1):
    if i == 2 or i == 5:
        cnpj_valido += '.'
    if i == 8:
        cnpj_valido += '/'
    if i == 12:
        cnpj_valido += '-'
    cnpj_valido += str(aux[i])

print('CNPJ informado: ', cnpj_informado)
print('CNPJ válido: ', cnpj_valido)

if cnpj_informado == cnpj_valido:
    print('[CNPJ VÁLIDO]', )
else:
    print('[CNPJ INVÁLIDO]')
