# Constantes

ADD = '1'
REMOVE = '2'
UPDATE = '3'
SEARCH_BY_NAME = '4'
SEARCH_BY_TEL = '5'
SHOW_LIST = '6'
EXIT = '0'


def init():
    print('Lista telefonica. Dado os itens do menu, escolha um.')


def show_menu():
    print('1 - Adicionar')
    print('2 - Remover')
    print('3 - Atualizar')
    print('4 - Pesquisar por nome')
    print('5 - Pesquisar por telefone')
    print('6 - Mostrar lista de telefones')
    print('0 - Sair')


def add(nomes, telefones):
    read_name = input('Entre com o nome: ')
    read_tel = input('Entre com o telefone: ')
    nomes.append(read_name)
    telefones.append(read_tel)
    print('Contato adicionado!')


def show_list(nomes, telefones):
    i = 1
    if len(nomes) > 0:
        print('Lista de telefones')
        for nome, telefone in zip(nomes, telefones):
            print(f'{i} - Nome: {nome} Telefone: {telefone}')
            i += 1
    else:
        print('Lista vazia! Sem contatos!')


def remove(nomes, telefones):
    read_name = input('Entre com o nome para remocao: ')
    if read_name in nomes:
        name_index = nomes.index(read_name)
        telefones.pop(name_index)
        nomes.remove(read_name)
        print('Contato removido com sucesso!')
    else:
        print('Nome nao encontardo na lista!')


def action(value, nomes, telefones):
    if value == ADD:
        add(nomes, telefones)
    elif value == REMOVE:
        remove(nomes, telefones)
    elif value == UPDATE:
        update(value)
    elif value == SEARCH_BY_NAME:
        seach_by_name(value)
    elif value == SEARCH_BY_TEL:
        seach_by_tel(value)
    elif value == SHOW_LIST:
        show_list(nomes, telefones)
    else:
        print('Entrada nao reconhecida:', value)
    print()


def main():
    init()
    read_value = ADD
    nomes, telefones = [], []
    while read_value != EXIT:
        show_menu()

        # Valor lido do usuario.
        read_value = input('Entre com o valor escolhido: ')

        # Toma acao de acordo com a entrada do usuario.
        action(read_value, nomes, telefones)


if __name__ == '__main__':
    main()
