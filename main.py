import csv
from modulos import soma_preços, separar, calcular_percentual

lista_produtos = [['Maçã', 3], ['Laranja', 2], ['Tomate', 4.50], ['Goiaba', 4], ['uva', 1.50]]
carrinho = {}
lista_preços = []

for c in range(len(lista_produtos)):
    print(f'{c + 1} - {lista_produtos[c][0]} - R${lista_produtos[c][1]}')

c = 1

while True:
    try:
        perg = int(input('Digite o ID do produto que você deseja: '))
        separar()
        perg -= 1
        carrinho[f'compra{c}'] = lista_produtos[perg][0]
        lista_preços.append(lista_produtos[perg][1])
        c += 1
        print(f'Você escolheu o(a) {lista_produtos[perg][0]}')
        
        while True:
            contin = input('Quer continuar comprando? [S/N] ').upper()
            separar()
            if contin not in ['S', 'N']:
                print('Digite [S] ou [N] amigo.')
            if contin == 'S':
                print('Você escolheu continuar comprando')
                break
            if contin == 'N':
                break
    except:
        print('Digite um ID válido, de 1 a 5, seu animal')

    if contin == "N":
        print('Você escolheu parar')
        break

separar()
valor_compra = soma_preços(lista_preços)
desconto = calcular_percentual(valor_compra, 5)

with open('produtos_comprados.csv', 'w', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    escritor_csv.writerow(['ID', 'Produto'])

    for i, v in carrinho.items():
        escritor_csv.writerow([i, v])
#
print(f'Os produtos comprados foram salvos em "produtos_comprados.csv"')

for i, v in carrinho.items():
    print(f'A {i} foi o(a) {v} \n')

print(f'O valor da compra deu R${valor_compra}')
separar()
con = 0

while True:
    print('Digite [D] para Débito, [C] Para Crédito, [DIN] para Dinheiro ou [P] para Pix ')
    
    try:
        metod = input('Qual será a forma de pagamento? ').upper()
        if metod not in ['C', 'D', 'DIN', 'P']:
            print('Digite uma forma de pagamento válida')
        if metod == 'C':
            print('Pagamento realizado com sucesso, volte sempre')
            con += 1
        if metod == 'D' or metod == 'DIN' or metod == 'P':
            print(f'O valor da compra deu {valor_compra}, mas como você está pagando à vista, o valor agora é {desconto}')
            con += 1
    except:
        print('Forma de pagamento inválida')

    if con == 1:
        break
