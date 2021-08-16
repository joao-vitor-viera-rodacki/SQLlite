import sqlite3 as sq

banco = sq.connect('database.db')
cursor = banco.cursor()

#cursor.execute('CREATE TABLE pessoas (nome text, idade integer, email text)')
#cursor.execute('INSERT INTO pessoas VALUES("joao",12,"text@gmail.com")')
sql = 'SELECT * FROM pessoas WHERE nome = ?'


def red (palavra):
    for row in cursor.execute(sql,(palavra,)):
        print(row)


red('12')

banco.commit()
banco.close()