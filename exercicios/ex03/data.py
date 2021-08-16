import sqlite3 as sq

banco = sq.connect('database.db')
cursor = banco.cursor()

#cursor.execute('CREATE TABLE pessoas (nome text, idade integer, email text)')


class Database:
    
    def cadastra_usu(self, nome, idade, email):
        cursor.execute(f'INSERT INTO pessoas VALUES("{nome}",{idade},"{email}")')
        print('Usuario criado !!!')

    def excluir_usu(self, condicao, caracter, integer =False):

        if integer :
            cursor.execute(f'DELETE from pessoas where idade {condicao}= {caracter}')

        else:
            cursor.execute(f'DELETE from pessoas where {condicao} = "{caracter}"')

    def ler_usu(self, condicao, caracter, integer=False):
        
        if integer:
            sql = f'SELECT * FROM pessoas WHERE idade {condicao}= {caracter}'
        else:
            sql = f'SELECT * FROM pessoas WHERE {condicao} = "{caracter}"'
        
        for row in cursor.execute(sql):
            print(row)

    def alterar_dados(self,nome=False, idade=False, email=False):
        if nome:
            modificar = str(input('Oque deseja por no lugar : '))            
            cursor.execute(f'UPDATE pessoas set nome = "{modificar}" WHERE nome = "{nome}"')

        if idade:
            modificar = int(input('Oque desaja por no lugar : '))
            cursor.execute(f'UPDATE pessoas set idade = "{modificar}" WHERE idade = "{idade}"')

        if email:
            modificar = str(input('Oque deseja por no lugar : '))
            cursor.execute(f'UPDATE pessoas set email = "{modificar}" WHERE email = "{email}"')
        
    


test = Database()
#test.cadastra_usu('boboo',24,'test@gmail.com')
#test.excluir_usu('<', 12, True)
#test.ler_usu('>', 23, True)
#test.alterar_dados(email='test@gmail.com')
banco.commit()
