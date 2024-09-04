nome = input('Nome do vendedor: ')
qc = int(input('Quantidade de carros vencidos: '))
vtv = float(input('Valor total das vendas: R$'))
qcrs = qc * 200
pv = (2 * vtv) / 100
s = qcrs + pv + 2500
print(f'O vendedor {nome} receberá um salário de R${s:.2f}')