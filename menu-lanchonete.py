print('Bem-vindo a Lanchonete do Luan')
print('******************CARDÁPIO******************')
print('| Código |        Descrição              | Valor')
print('|   100  | Cachorro-Quente               | 9.00 ')
print('|   101  | Cachorro-Quente Duplo         | 11.00 ')
print('|   102  | X-Egg                         | 12.00 ')
print('|   103  | X-Salada                      | 13.00 ')
print('|   104  | X-Bacon                       | 14.00 ')
print('|   105  | X-Tudo                        | 17.00 ')
print('|   200  | Refri Lata                    | 5.00 ')
print('|   201  | Chá Gelado                    | 4.00 ')

valor = 0 #o valor do montante inicia em 0.

while True:
    codigo = input('Insira o código do pedido: ')
    codigos_validos = ['100', '101', '102', '103', '104', '105', '200', '201'] #lista contendo apenas os códigos válidos para realizar pedido.
    if codigo not in codigos_validos: #caso o(s) código(s) não esteja na lista, resulturá em opção inválida
        print('Opção inválida!')
        continue #'continue' para que o usuário insira uma opção válida de acordo com o código do cardápio.

    if (codigo == '100'):
        print('Você pediu um Cachorro-Quente no valor de: R$ 9.00')
        pedido = "Cachorro-Quente"
        valor = valor + 9.00
    elif (codigo == '101'):
        print('Você pediu um Cachorro-Quente Duplo no valor de: R$ 11.00')
        pedido = "Cachorro-Quente Duplo"
        valor = valor + 11.00
    elif (codigo == '102'):
        print('Você pediu um X-Egg no valor de: R$ 12.00')
        pedido = "X-Egg"
        valor = valor + 12.00
    elif (codigo == '103'):
        print('Você pediu um X-Salada no valor de: R$ 13.00')
        pedido = "X-Salada"
        valor = valor + 13.00
    elif (codigo == '104'):
        print('Você pediu um X-Bacon no valor de: R$ 14.00')
        pedido = "X-Bacon"
        valor = valor + 14.00       
    elif (codigo == '105'):
        print('Você pediu um X-Tudo no valor de: R$ 17.00')
        pedido = "X-Tudo"
        valor = valor + 17.00
    elif (codigo == '200'):
        print('Você pediu um Refri Lata no valor de: R$ 5.00')
        pedido = "Refri Lata"
        valor = valor + 5.00
    elif (codigo == '201'):
        print('Você pediu um Chá Gelado no valor de: R$ 4.00')
        pedido = "Chá Gelado"
        valor = valor + 4.00

    print('Deseja pedir mais alguma coisa?')
    print('1 - SIM')
    print('0 - NÃO')
    pedir_mais = input ('>>')

    if pedir_mais == '1':
        continue #'continue' aqui, indica que, caso o usuário seleciona a opção 1 - SIM, o programa pergunta novamente qual produto deseja acrescentar.
    else:
        print('O Valor total a ser pago é de: R${:.2f}' .format(valor))
        break

    print(valor)   