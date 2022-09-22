print('Bem vindo(a) à Feijoadinha Querida da Sayuri Takano')  # Identificador Pessoal


def vol_feijoada():  # função do menu do volume da feijoada
    while True:
        print('Menu do volume da feijoada.')
        try:
            ml = int(input('Digite a quantidade desejada(ml): '))
            vol_valor = ml * 0.08
            if ml < 300 or ml > 5000:
                print(
                    'Não aceitamos porções menores que 300ml ou maiores que 5l! Tente novamente!')  # verificação de input
                continue
            elif ml >= 300 or ml <= 5000:
                return vol_valor
        except ValueError:  # verificação de input
            print('Você não digitou um número. Tente novamente!')


def opc_feijoada():  # função do menu da opção da feijoada
    while True:
        print('Menu da opção da feijoada.')
        print('b - Básica (Feijão + paiol + costelinha) ')
        print('p - Premium (Feijão + paiol + costelinha + partes de porco)')
        print('s - Suprema (Feijão + paiol + costelinha + partes do porco + charque + calabresa + bacon)')
        peso = str(input('Digite a opção desejada: '))
        if peso != 'b' and peso != 'p' and peso != 's':  # verificação de input
            print('Você digitou uma opção que não existe. Tente novamente!')
        elif peso == 'b':
            peso_valor = 1.00
            return peso_valor
        elif peso == 'p':
            peso_valor = 1.25
            return peso_valor
        elif peso == 's':
            peso_valor = 1.50
            return peso_valor


def acomp_feijoada():  # função do menu do acompanhamento da feijoada
    tot_acomp = 0
    while True:
        try:
            print('Deseja mais algum acompanhamento?')
            print('0 - não desejo mais acompanhamentos (encerrar pedido)')  # atendimento encerrado caso seja escolhido
            print('1 - 200g de arroz')
            print('2 - 150g de farofa especial')
            print('3 - 100g de couve cozida')
            print('4 - 1 laranja descascada')
            acomp = int(input('>> '))
            if acomp <= -1 or acomp >= 5:  # verificação de input
                print('Não há um acompanhamento para o número escolhido. Tente novamente')
                continue
            if acomp == 1:
                acomp_valor = 5.00
            if acomp == 2:
                acomp_valor = 6.00
            if acomp == 3:
                acomp_valor = 7.00
            if acomp == 4:
                acomp_valor = 3.00
            if acomp == 0:
                return tot_acomp
            tot_acomp += acomp_valor
        except ValueError:  # verificação de input
            print('Você não digitou um número. Tente novamente!')


volume_feijoada = vol_feijoada()
opcao_feijoada = opc_feijoada()
acompanha_feijoada = acomp_feijoada()
total = (volume_feijoada * opcao_feijoada) + acompanha_feijoada  # resultado da equação que a empresa cobra por feijoada
print('O total a ser pago é R$ %.2f. (volume = %.2f * opção = %.2f + acompanhamento = %.2f) ' % (total, volume_feijoada,
opcao_feijoada, acompanha_feijoada))
