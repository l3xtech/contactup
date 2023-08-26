from create import id_generator

balloon_dict = {}
name_1 = ''
name_2 = ''
name_3 = ''

# Cria um novo contato no db
def create_new_contact(dicionario, lista):
    global balloon_dict
    global name_1
    global name_2
    global name_3

    for chave, valor in dicionario.items():

        if isinstance(valor, list):
            novo_valor = []
            for item in valor:
                novo_item = {}
                for sub_chave, sub_valor in item.items():
                    novo_sub_valor = input(f'Digite o {sub_chave} do novo contato: ')
                    novo_item[sub_chave] = novo_sub_valor

                novo_valor.append(novo_item)

            balloon_dict[chave] = novo_valor

        elif chave == 'id':
            balloon_dict[chave] = next(id_generator)

        elif chave == 'nome':
            novo_valor = input(f'Digite o {chave} do novo contato: ')
            name_1 = novo_valor
            balloon_dict[chave] = novo_valor

        elif chave == 'nome_do_meio':
            novo_valor = input(f'Digite o {chave} do novo contato: ')
            name_2 = novo_valor
            balloon_dict[chave] = novo_valor

        elif chave == 'sobrenome':
            novo_valor = input(f'Digite o {chave} do novo contato: ')
            name_3 = novo_valor
            balloon_dict[chave] = novo_valor

        elif chave == 'nome_completo':

            if name_1 != '' and name_2 == '' and name_3 == '':
                balloon_dict[chave] = name_1
            elif name_1 != '' and name_2 != '' and name_3 == '':
                balloon_dict[chave] = f'{name_1} {name_2}'
            elif name_1 != '' and name_2 == '' and name_3 != '':
                balloon_dict[chave] = f'{name_1} {name_3}'
            elif name_1 != '' and name_2 != '' and name_3 != '':
                balloon_dict[chave] = f'{name_1} {name_2} {name_3}'
            else:
                balloon_dict[chave] = ''

        else:
            novo_valor = input(f'Digite o {chave} do novo contato: ')
            balloon_dict[chave] = novo_valor


    lista.append(balloon_dict)
    balloon_dict = {}
    name_1 = ''
    name_2 = ''
    name_3 = ''


def show_list_of_contacts(cont_list_db):
    for contato in cont_list_db:
        for chave, valor in contato.items():
            if isinstance(valor, list):
                print()
                print(f'---------{chave}----------')
                for item in valor:
                    for sub_chave, sub_valor in item.items():
                        print(f'{sub_chave}: {sub_valor}')
            else:
                if valor == '':
                    continue
                print(f'{chave}: {valor}')

