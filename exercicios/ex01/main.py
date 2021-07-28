import sqlite3 as sq

banco = sq.connect('database.db')

cursor = banco.cursor()


def create_user(nome, idade, email):
    try:
        cursor.execute(f'INSERT INTO pessoas VALUES("{nome}",{idade},"{email}")')
    
    except sq.Error as erro:
        print(f'Não foi possivel adicionar {erro}')

    else:
        print('User create com sucesso !!')
        banco.commit()

def delete_user(nome):
    try:
        cursor.execute(f'DELETE from pessoas WHERE nome = "{nome}"')
    except sq.Error as erro :
        print(f'não foi possivel excluir o usuario {nome} : {erro}')

    else:
        print(f'usuario {nome} excluido com sucesso !!!')
        banco.commit()



while True:

    escolha = int(input('[1] para excluir [2] para adicionar [3] para sair : '))
    
    if escolha == 1:
        nome = str(input('Qual o nome do user : '))
        delete_user(nome)

    elif escolha == 2 :
        nome = str(input('Qual o nome do user : '))
        idade = int(input('Idade : '))
        email = str(input('Email : '))
        create_user(nome, idade, email)
    
    elif escolha == 3 :
        break