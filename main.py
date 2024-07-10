#Criando o código principal(main)
print('Bem-vindos(as) a fábrica de camisetas da Natália do Nascimento\n')

# Chamando as funções
valor_modelo = escolha_modelo()
valor_camisetas = num_camisetas()
valor_frete = frete()

# Calculando o total a pagar
total = (valor_modelo * valor_camisetas) + valor_frete

print(f'\nTotal a pagar: R$ {total:.2f} (Valor modelo: {valor_modelo:.2f} x Quantidade(com desconto): {valor_camisetas:.0f} + Frete: {valor_frete:.2f})')
