import sqlite3 as sq


banco = sq.connect('database.db')
cursor = banco.cursor()

def cadastrar_usu(nome, idade, email):
    cursor.execute(f'INSERT INTO pessoas VALUES ("{nome}","{idade}","{email}")')


def modificar_usu(nome=False, idade=False, email=False):
    if nome:
        
        modificar = input('Oque deseja colocar no lugar ? ')
        cursor.execute(f"UPDATE pessoas set nome = '{modificar}' WHERE nome = '{nome}'")
        
    if idade:
        
        modificar = input('Oque deseja modificar ? ')
        cursor.execute(f"UPDATE pessoas set nome = '{modificar}' WHERE idade = {idade}")      

    if email:
        
        modificar = input('Oque deseja modificar ? ')
        cursor.execute(f"UPDATE pessoas set nome = '{modificar}' WHERE email = '{email}'")

modificar_usu(idade="45")

banco.commit()