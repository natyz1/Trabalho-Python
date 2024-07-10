# Trabalho em Python
Este trabalho foi feito durante a faculdade como uma forma para aprender mais sobre loops(while) e o uso de try/except.
<h3><strong> Eu tinha que atender aos seguintes requisitos: </strong></h3>

Enunciado: Você foi contratado para desenvolver um sistema de cobrança de serviços de uma fábrica que vende Camisetas em atacado. Você ficou com a parte de desenvolver a interface com o funcionário. 

A Fábrica opera as vendas da seguinte maneira: 

<ul>
  <li> Camiseta Manga Curta Simples (MCS), o valor unitário é de um real e oitenta centavos; </li>
  <li> Camiseta Manga Longa Simples (MLS), o valor unitário é de dois reais e dez centavos; </li>
  <li> Camiseta Manga Curta Com Estampa (MCE), o valor unitário é de dois reais e noventa centavos; </li>
  <li> Camiseta Manga Longa Com Estampa (MLE), o valor unitário é de três reais e vinte centavos; </li> 
</ul>
 
<ul>
  <li> Se número de camisetas for menor que 20 não há desconto na venda; </li>
  <li> Se número de camisetas for igual ou maior que 20 e menor que 200, o desconto será de 5%; </li>
  <li >Se número de camisetas for igual ou maior que 200 e menor que 2000, o desconto será de 7%; </li>
  <li> Se número de camisetas for igual ou maior que 2000 e menor ou igual que 20000, o desconto será de 12%; </li>
  <li> Se número de camisetas for maior que 20000, não é aceito pedidos nessa quantidade de camisetas; </li>
</ul>
 
<ul>
  <li> Para o adicional de frete por transportadora (1) é cobrado um valor extra de 100 reais; </li>
  <li> Para o adicional de frete por Sedex (2) é cobrado um valor extra de 200 reais; </li>
  <li> Para o adicional de retirar o pedido na fábrica (0) é cobrado um valor extra de 0 reais; </li>
</ul>

O valor final da conta é calculado da seguinte maneira: 

<strong>total = (modelo * num_camisetas) + frete </strong>

Elabore um programa em Python que:  

<ol>
  <li>Deve-se implementar o print com o seu nome completo (somente print, não usar input aqui). 
    <br/>Por exemplo: print(“Bem vindos a Fábrica de Camisetas do Fulano”); </li>
  <li>Deve-se implementar a função escolha_modelo() em que:; </li>
  <ol>
    <li>Pergunta o modelo desejado; </li>
    <li>Retorna o valor do modelo com base na escolha do usuário (use return); </li>
    <li>Repete a pergunta do item 2.i se digitar uma opção diferente de: MCS/MLS/MCE/MLE </li>
  </ol>
  <li>Deve-se implementar a função num_camisetas() em que:; </li>
  <ol>
    <li>Pergunta o número de camisetas; </li>
    <li>Retorna (use return) o número de camisetas com desconto seguindo a regra do enunciado (desconto calculado em cima do número de camisetas); </li>
    <li>Repete a pergunta do item 3.i se digitar um valor acima de 20000 ou valor não numérico (use try/except para não numérico) </li>
  </ol>
  <li>Deve-se implementar a função frete() em que:; </li>
  <ol>
    <li>Pergunta pelo serviço adicional de frete; </li>
    <li>Retorna (use return) o valor de apenas uma das opções de frete;  </li>
    <li>Repetir a pergunta item 4.i se digitar uma opção diferente de: 1/2/0</li>
  </ol>
  <li>Deve-se implementar o total a pagar no código principal (main), ou seja, não pode estar dentro de função, conforme o enunciado; </li>
  <li>Deve-se implementar try/except; </li>
  <li>Deve-se inserir comentários relevantes no código;</li> 
</ol>
