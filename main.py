"""
contatos
"""

import copy

import create

db_contatos = []
id_generator = (n for n in range(1, 1000000))

# Realiza cópia profunda, sem referenciar valores entre os objetos.
novo_contato = copy.deepcopy(create.contact_model)

# Cria um novo contato no db
def criar_novo_contato(dicionario, lista):
    novo_contato = {}
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

            novo_contato[chave] = novo_valor

        elif chave == 'id':
            novo_contato[chave] = next(id_generator)

        elif chave == 'nome':
            novo_valor = input(f'Digite o {chave} do novo contato: ')
            nome1 = novo_valor
            novo_contato[chave] = novo_valor

        elif chave == 'nome_do_meio':
            novo_valor = input(f'Digite o {chave} do novo contato: ')
            nome2 = novo_valor
            novo_contato[chave] = novo_valor

        elif chave == 'sobrenome':
            novo_valor = input(f'Digite o {chave} do novo contato: ')
            nome3 = novo_valor
            novo_contato[chave] = novo_valor

        elif chave == 'nome_completo':

            if nome1 != '' and nome2 == '' and nome3 == '':
                novo_contato[chave] = nome1
            elif nome1 != '' and nome2 != '' and nome3 == '':
                novo_contato[chave] = f'{nome1} {nome2}'
            elif nome1 != '' and nome2 == '' and nome3 != '':
                novo_contato[chave] = f'{nome1} {nome3}'
            elif nome1 != '' and nome2 != '' and nome3 != '':
                novo_contato[chave] = f'{nome1} {nome2} {nome3}'
            else:
                novo_contato[chave] = ''

        else:
            novo_valor = input(f'Digite o {chave} do novo contato: ')
            novo_contato[chave] = novo_valor


    lista.append(novo_contato)

criar_novo_contato(novo_contato, db_contatos)

criar_novo_contato(novo_contato, db_contatos)

#  print(*db_contatos, sep='\n')

for contato in db_contatos:
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

# pega o valor de uma chave no dicionario
#  print(contact_model.get('nome'))
# Igual anterior porem o segundo argumento é a saida caso não encontre a chave.
#  print(contact_model.get('nome', 'Não existe'))


# Atualiza / Edita valores em um dicionario.
#  novo_contato.update({
    #  'nome': 'joão'
#  })


#  print(novo_contato.get('nome'))

# Outra maneira de usar Update. Em uma linha.
#  novo_contato.update(nome='José', sobrenome='Silva')

#  print(novo_contato.get('nome_completo'))

#  db_contatos.append(novo_contato)

#  todos_os_nomes = [
    #  {**pessoa, 'nome_completo':
        #  pessoa['nome'] + ' ' + \
        #  pessoa['nome_do_meio'] + ' ' + \
        #  pessoa['sobrenome']}
    #  for pessoa in db_contatos
#  ]

### COMPRIMENTO - Metodo len()

# Comprimento de telefones. Quantos dicionarios de telefone cadastrados.
#  print(len(contact_model['telefones']))
# Comprimento do dicionario telefone. Numero de campos no modelo.
#  print(len(contact_model['telefones'][0]))

# Itera / Percorre todo o dicionario mostrando chave e valor.
#  for chave, valor in contact_model.items():
    #  print(chave, valor)

#  print()
#  print(db_contatos)
