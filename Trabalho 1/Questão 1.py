print('Bem vindo(a) à Loja de Sayuri Takano.') # Identificador Pessoal
valor = float(input('Qual é o valor do produto? '))
qtd = int(input('Qual é a quantidade desejada do produto? '))
if valor <= 0.00:
 print('O valor é 0 ou menor que zero. Por favor, digite o valor correto.')
# Se o valor for maior que zero, o programa seguirá normalmente.
elif 1 <= qtd <= 4: # quantidade do produto entre 1 e 4; sem desconto
 total = valor * qtd
 print('Não houve desconto do produto. O valor total é R$ %.2f.' % valor)
elif 5 <= qtd <= 19: # quantidade do produto entre 5 e 19; com desconto de 3%
 total = valor * qtd
 tot_c_desc = (valor * 0.97) * qtd
 print('Sua compra ganhou um desconto de 3%!')
 print('O valor total sem desconto é de R$ %.2f. O valor total com desconto é de R$%.2f.' % (total, tot_c_desc))
elif 20 <= qtd <= 99: # quantidade do produto entre 20 e 99; com desconto de 6%
 total = valor * qtd
 tot_c_desc = (valor * 0.94) * qtd
 print('Sua compra ganhou um desconto de 6%!')
 print('O valor total sem desconto é de R$%.2f. O valor total com desconto é de R$%.2f.' % (total, tot_c_desc))
elif qtd >= 100: # quantidade do produto maior ou igual a 100; com desconto de 10%
 total = valor * qtd
 tot_c_desc = (valor * 0.90) * qtd
 print('Sua compra ganhou um desconto de 10%!')
 print('O valor total sem desconto é de R$%.2f. O valor total com desconto é de R$%.2f.' % (total, tot_c_desc))
# Se a quantidade do produto for menor ou igual a zero, o programa terminará aqui.
else:
 print('A quantidade do produto é 0 ou algum valor foi escrito de maneira incorreta.')
 print('Não esqueça de usar ponto (.) no lugar da vírgula (,). Tente novamente.')