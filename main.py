"""
main
"""
# System imports
import create

create.create_new_contact(create.new_contact, create.list_of_contacts)

create.create_new_contact(create.new_contact, create.list_of_contacts)

for contato in create.list_of_contacts:
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

