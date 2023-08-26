import copy

list_of_contacts = []

contact_model = {
    'id': 'add',
    'prefixo': 'add',
    'nome': 'add',
    'nome_do_meio': 'add',
    'sobrenome': 'add',
    'nome_completo': 'add',
    'sufixo': 'add',
    'apelido': 'add',
    'nickname': 'add',

    'trabalhos': [
        {'empresa': 'add',
        'cargo': 'add',
        'departamento': 'add',
        'data_entrada': 'add',
        'data_saida': 'add'},
    ],

    'emails': [
        {'email': 'add',
        'tag_email': 'add'},
    ],

    'telefones': [
        {'codigo_pais': 'add',
        'telefone': 'add',
        'tag_telefone': 'add'},
    ],

    'enderecos': [
        {'pais': 'add',
         'endereco': 'add',
         'cidade': 'add',
         'estado': 'add',
         'cep': 'add',
         'tag_endereco': 'add'},
    ],
    'website': 'add',
    'aniversario': 'add',

    'datas': [
        {'tag_data': 'add',
         'data': 'add'},
    ],

    'pessoas_relacionadas': [
        {'id_relacao': 'add',
         'tipo_relacao': 'add',
         'observacao_relacao': 'add'},
    ],

    'historico': [
        {'historico_data': 'add',
         'historico_titulo': 'add',
         'historico_observacao': 'add'},
    ]
}

# Realiza cópia profunda, sem referenciar valores entre os objetos.
empty_contact = copy.deepcopy(contact_model)
