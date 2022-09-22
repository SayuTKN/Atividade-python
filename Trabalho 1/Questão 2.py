print('Bem vindo(a) à pizzaria de Sayuri Takano.')  # Identificador Pessoal
print('Cardárpio:')
print('Código: 21 - Napolitana - (Média - R$ 20,00) / (Grande - R$ 26,00)')
print('Código: 22 - Margherita - (Média - R$ 20,00) / (Grande - R$ 26,00)')
print('Código: 23 - Calabresa - (Média - R$ 25,00) / (Grande - R$ 32,50)')
print('Código: 24 - Toscana - (Média - R$ 30,00) / (Grande - R$ 39,00)')
print('Código: 25 - Portuguesa - (Média - R$ 30,00) / (Grande - R$ 39,00)')

tot_pizzas = 0
atendimento = 0
while True:
    if atendimento == 0:  # Começar atendimento
        print('Você deseja ser atendido?')
        print('1 - Sim')
        print('0 - Não')
    else:  # Segunda ou mais tentativas de atendimento
        print('Você deseja ser atendido novamente?')
        print('1 - Sim')
        print('0 - Não')
    ctz = (int(input('>>')))
    if ctz != 1 and ctz != 0:  # Verificação de input
        print('Opção inválida')
        continue
    if ctz == 1:  # Começo do pedido
        tam = input('Qual o tamanho de pizza desejado (M/G)?')
        if tam != 'm' and tam != 'g':  # Verificação de input
            print('Opção de tamanho inválida.')
            atendimento += 1
            continue
        codigo = int(input('Digite o código do sabor desejado.'))
        total = 0
        if codigo != 21 and codigo != 22 and codigo != 23 and codigo != 24 and codigo != 25:  # Verificação de input
            print('Opção de código inválida.')
            atendimento += 1
            continue
        if codigo == 21:
            if tam == 'm':
                napm = 20.00
                total = napm
            if tam == 'g':
                napm = 20.00
                total = napm * 1.30
            print('Você pediu uma Napolitana que custa R$ %.2f.' % (total))
        elif codigo == 22:
            if tam == 'm':
                marm = 20.00
                total = marm
            if tam == 'g':
                marm = 20.00
                total = marm * 1.30
            print('Você pediu uma Margherita que custa R$ %.2f.' % (total))
        elif codigo == 23:
            if tam == 'm':
                calm = 25.00
                total = calm
            if tam == 'g':
                calm = 25.00
                total = calm * 1.30
            print('Você pediu uma Calabresa que custa R$ %.2f.' % (total))
        elif codigo == 24:
            if tam == 'm':
                tosm = 30.00
                total = tosm
            if tam == 'g':
                tosm = 30.00
                total = tosm * 1.30
            print('Você pediu uma Toscana que custa R$ %.2f.' % (total))
        elif codigo == 25:
            if tam == 'm':
                porm = 30.00
                total = porm
            if tam == 'g':
                porm = 30.00
                total = porm * 1.30
            print('Você pediu uma Portuguesa que custa R$ %.2f.' % (total))
        tot_pizzas += total
    else:  # Atendimento encerrado
        if tot_pizzas > 0: # Caso 'tot_pizzas' não seja maior que 0, o total não será exibido
            print('O valor total é R$ %.2f.' % (tot_pizzas))
        print('Encerrar...')
        break
    atendimento += 1