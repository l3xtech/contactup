import create

# Cria um novo contato no db
def create_new_contact(dicionario, lista):
    new_contact = {}
    nome1 = ''
    nome2 = ''
    nome3 = ''

    for chave, valor in dicionario.items():

        if isinstance(valor, list):
            novo_valor = []
            for item in valor:
                novo_item = {}
                for sub_chave, sub_valor in item.items():
                    novo_sub_valor = input(f'Digite o {sub_chave} do novo contato: ')
                    novo_item[sub_chave] = novo_sub_valor

                novo_valor.append(novo_item)

            new_contact[chave] = novo_valor

        elif chave == 'id':
            new_contact[chave] = next(create.id_generator)

        elif chave == 'nome':
            novo_valor = input(f'Digite o {chave} do novo contato: ')
            nome1 = novo_valor
            new_contact[chave] = novo_valor

        elif chave == 'nome_do_meio':
            novo_valor = input(f'Digite o {chave} do novo contato: ')
            nome2 = novo_valor
            new_contact[chave] = novo_valor

        elif chave == 'sobrenome':
            novo_valor = input(f'Digite o {chave} do novo contato: ')
            nome3 = novo_valor
            new_contact[chave] = novo_valor

        elif chave == 'nome_completo':

            if nome1 != '' and nome2 == '' and nome3 == '':
                new_contact[chave] = nome1
            elif nome1 != '' and nome2 != '' and nome3 == '':
                new_contact[chave] = f'{nome1} {nome2}'
            elif nome1 != '' and nome2 == '' and nome3 != '':
                new_contact[chave] = f'{nome1} {nome3}'
            elif nome1 != '' and nome2 != '' and nome3 != '':
                new_contact[chave] = f'{nome1} {nome2} {nome3}'
            else:
                new_contact[chave] = ''

        else:
            novo_valor = input(f'Digite o {chave} do novo contato: ')
            new_contact[chave] = novo_valor


    lista.append(new_contact)

