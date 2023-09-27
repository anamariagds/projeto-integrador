import sqlite3

# Conectar ao banco de dados
conexao = sqlite3.connect('banco_de_dados.db')
cursor = conexao.cursor()

# criando tabelas "pessoa" e "conta_bancaria"
cursor.execute('''CREATE TABLE IF NOT EXISTS pessoa (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               cpf TEXT,
               nome TEXT,
               sobrenome TEXT,
               idade INTEGER
               
               )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS conta_bancaria (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               agencia VARCHAR(7) NOT NULL,
               numero TEXT NOT NULL,
               saldo REAL ,
               gerente INTEGER,
               titular INTEGER, FOREIGN KEY (titular) REFERENCES pessoa (id)
              
               )''' )

arquivo_pessoa = 'dados_pessoa.txt'
arquivo_contas = 'contas_1.txt'

cpf = input("Informe o cpf: ")
nome = input("Nome da Pessoa: ")
sobrenome =  input("Sobrenome da Pessoa: ")
idade =  input("idade: ")

agencia = input("Agencia bancaria: ")
numero = input("Número da Conta: ")
saldo = input("Saldo: ")
gerente = input("Gerente: ")
       

        
cursor.execute('INSERT INTO pessoa (cpf, nome, sobrenome, idade) VALUES(?, ?, ?, ?)', 
               (cpf, nome, sobrenome, idade))
conexao.commit()
id_pessoa = cursor.lastrowid #pega o id da instancia criada

cursor.execute('INSERT INTO conta_bancaria ( agencia, numero, saldo, gerente, titular) VALUES (?, ?, ?, ?, ?)',
                (agencia, numero, saldo, gerente, id_pessoa))
conexao.commit()
      
print("Linhas de pessoa adicionadas com sucesso!")

conexao.close()