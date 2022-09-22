listaProdutos = [] # criação da lista
codigo = 1 # contador do código
def cadastrarProduto(): # função de cadastrar pedido
    global codigo # código global para funcionar contagem no cadastro
    while True:
        try:
            dic_produto = {} # criação do dicionário do produto
            print('O código é {}'.format(codigo))
            nome = input('Qual o nome do produto? ')
            fabricante = input('Quem é o fabricante do produto? ')
            valor = float(input('Qual o valor(R$) do produto? '))
            dic_produto['codigo'] = codigo #declarar propriedade código no dicionário do produto
            dic_produto['nome'] = nome # declarar propriedade nome no dicionário do produto
            dic_produto['fabricante'] = fabricante # declarar propriedade fabricante no dicionário do produto
            dic_produto['valor'] = valor # declarar propriedade valor no dicionário do produto
            listaProdutos.append(dic_produto) # copiando items do dicionário para a lista
            codigo += 1
            break
        except ValueError: # verificação de input
            print('Digite um número.')

def consultarProduto(): # função de consultar produto
    while True:
        try:
            print('Você selecionou a opção de consultar um produto.')
            print('Escolha a opção desejada:')
            print('1 - consultar todos os produtos')
            print('2 - consultar produto(s) por código')
            print('3 - consultar produto(s) por fabricante')
            print('4 - retornar')
            escolha = int(input('>> '))
            if escolha == 1:
                for produto in listaProdutos:
                    for i,j in produto.items(): # consultando produto(s) na lista
                        print('{}: {}'.format(i,j))
            if escolha == 2:
                cod_prod = int(input('Digite o código do produto: '))
                for produto in listaProdutos:
                    if cod_prod == produto['codigo']: # consultando produto(s) na lista pelo código
                        for i,j in produto.items():
                            print('{}: {}'.format(i,j))
            if escolha == 3:
                fab_prod = input('Digite o fabricante do produto: ')
                for produto in listaProdutos:
                    if fab_prod == produto['fabricante']: # consultando produto(s) na lista pelo fabricante
                        for i,j in produto.items():
                            print('{}: {}'.format(i,j))
            if escolha == 4: # sair de opção de consultar produto
                break
        except ValueError: # verificação de input
            print('Digite novamente.')

def removerProduto(): # função para remover produto
    cod_apagar = int(input('Qual código você deseja remover? '))
    for produto in listaProdutos:
        if cod_apagar == produto['codigo']:
            listaProdutos.remove(produto) # excluir código desejado na lista


print('Bem vindo(a) ao Controle de Estoque da Mercearia da Sayuri Takano') # identificador pessoal
while True:
    try:
        print('Escolha a opção desejada')
        print('1 - Cadastrar pedido')
        print('2 - Consultar produto(s)')
        print('3 - Remover produto')
        print('4 - Sair')
        escolha = (int(input('>> ')))
        if escolha == 1:
            cadastrarProduto()
        elif escolha == 2:
            consultarProduto()
        elif escolha == 3:
            removerProduto()
        elif escolha == 4: # encerrar menu
            break
    except ValueError: # verificação de input
        print('Digite um número válido.')

        print('Digite um número válido.')