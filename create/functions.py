from create import id_generator, list_of_contacts

balloon_dict = {}
name_1 = ''
name_2 = ''
name_3 = ''

def populate_list(key, primary_list, variable_to_insert):
    secundary_list = []

    for index in primary_list:
        temp_dict = {}

        for index_key, index_value in index.items():
            new_index_value = input(f'Digite o {index_key} do novo contato: ')
            temp_dict[index_key] = new_index_value

        secundary_list.append(temp_dict)

    variable_to_insert[key] = secundary_list


def populate_value_of_key(key, value, variable_to_insert):

    global name_1
    global name_2
    global name_3

    match key:
        case 'id':
            variable_to_insert[key] = next(id_generator)
        case 'nome':
            new_value = input(f'Digite o {key} do novo contato: ')
            name_1 = new_value
            variable_to_insert[key] = new_value
        case 'nome_do_meio':
            new_value = input(f'Digite o {key} do novo contato: ')
            name_2 = new_value
            variable_to_insert[key] = new_value
        case 'sobrenome':
            new_value = input(f'Digite o {key} do novo contato: ')
            name_3 = new_value
            variable_to_insert[key] = new_value
        case 'nome_completo':
            if name_1 != '' and name_2 == '' and name_3 == '':
                variable_to_insert[key] = name_1
            elif name_1 != '' and name_2 != '' and name_3 == '':
                variable_to_insert[key] = f'{name_1} {name_2}'
            elif name_1 != '' and name_2 == '' and name_3 != '':
                variable_to_insert[key] = f'{name_1} {name_3}'
            elif name_1 != '' and name_2 != '' and name_3 != '':
                variable_to_insert[key] = f'{name_1} {name_2} {name_3}'
            else:
                variable_to_insert[key] = ''
        case _:
            new_value = input(f'Digite o {key} do novo contato: ')
            variable_to_insert[key] = new_value

def create_in_list(lista):

    def create_by_dict(dicionario):
        global balloon_dict
        global name_1
        global name_2
        global name_3

        for chave, valor in dicionario.items():

            if isinstance(valor, list):
                populate_list(chave, valor, balloon_dict)
            else:
                populate_value_of_key(chave, valor, balloon_dict)

        lista.append(balloon_dict)
        balloon_dict = {}
        name_1 = ''
        name_2 = ''
        name_3 = ''

    return create_by_dict


create_in_db = create_in_list(list_of_contacts)

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

