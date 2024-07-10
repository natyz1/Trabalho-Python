# Criando o código com as funções
# Primeira função usada para definir qual modelo será escolhido e seu respectivo valor
def escolha_modelo():
    while True:
        modelo = input('Entre com o modelo desejado:\n MCS - Manga curta simples\n MLS - Manga longa simples\n MCE - Manga curta com estampa\n MLE - Manga longa com estampa\n >> ')

        if modelo.upper() == 'MCS':
            valor_modelo = 1.8
        elif modelo.upper() == 'MLS':
            valor_modelo = 2.1
        elif modelo.upper() == 'MCE':
            valor_modelo = 2.9
        elif modelo.upper() == 'MLE':
            valor_modelo = 3.2
        else:
            print('Escolha inválida, entre com o modelo novamente\n')
            continue
        print(f'O valor da unidade do modelo é de: R$ {valor_modelo:.2f}')
        return valor_modelo

# Segunda função criada para definir quantas camisetas o usuário deseja e calcular o desconto com base no total de camisetas escolhidas
def num_camisetas():
    while True:
        try:
            quantidade = int(input('\nEntre com o número de camisetas: '))
            if quantidade < 20:
                desconto = 0
            elif quantidade >= 20 and quantidade < 200:
                desconto = 5/100
            elif quantidade >= 200 and quantidade < 2000:
                desconto = 7/100
            elif quantidade >= 2000 and quantidade <= 20000:
                desconto = 12/100
            else:
                raise ValueError('Não aceitamos tantas camisetas de uma vez.')

            total_com_desconto = quantidade * (1 - desconto)
            print(f'O total de camisetas (com desconto) é de: {total_com_desconto:.0f}')
            return int(total_com_desconto)

        except ValueError as e:
            print(e)
            print('Por favor, entre com um NÚMERO de camisetas VÁLIDO')

# Terceira função criada para definir o tipo de frete que o usuário deseja
def frete():
    while True:
        frete = input('\nEscolha o tipo de frete:\n 1 - Frete por transportadora - R$100.00\n 2 - Frete por Sedex - R$200.00\n 0 - Retirar pedido na fábrica - R$0.00\n >> ')
        if frete == '1':
            valor_frete = 100
        elif frete == '2':
            valor_frete = 200
        elif frete == '0':
            valor_frete = 0
        else:
            print('Escolha inválida, entre com o frete novamente\n')
            continue
        print(f'O valor do frete é de: R$ {valor_frete:.2f}')
        return valor_frete
