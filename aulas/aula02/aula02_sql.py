import sqlite3

banco = sqlite3.connect('database.db')

cursor = banco.cursor()

#cursor.execute('CREATE TABLE pessoas (nome text , idade integer, email text)')

#cursor.execute('INSERT INTO pessoas VALUES("Maria", 12, "test@gmail.com")')

cursor.execute('DELETE from pessoas WHERE idade >= 10')

banco.commit()
banco.close()




