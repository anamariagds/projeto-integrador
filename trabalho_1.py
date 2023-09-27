import sqlite3

# Conectar ao banco de dados
conexao = sqlite3.connect('banco_de_dados.db')
cursor = conexao.cursor()

# criando tabelas "pessoa" e "conta_bancaria"
cursor.execute('''
               CREATE TABLE IF NOT EXISTS pessoa (
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



def exibir_menu():
    print("Menu:")
    print("1. Preencher tabela com arquivos")
    print("2. Criar pessoa na tabela")
    print("3. Atualizar")
    print("4. Deletar")
    print("5. Sair")

arquivo_pessoa = 'dados_pessoa.txt'
arquivo_contas = 'contas_1.txt'


while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
       #Preencher tabelas pelo arquivo .txt                    
        with open(arquivo_pessoa, 'r') as arquivo:
            for linha in arquivo:
                linha = linha.strip() 
                cpf, nome, sobrenome, idade = linha.split()
                cursor.execute('INSERT INTO pessoa (cpf, nome, sobrenome, idade) VALUES (?, ?, ?, ?)',
                                (cpf, nome, sobrenome, idade))
                conexao.commit()

        with open(arquivo_contas, 'r') as arquivo:
            for linha in arquivo:
                agencia, numero, saldo, gerente, titular = linha.split()
                cursor.execute('INSERT INTO conta_bancaria ( agencia, numero, saldo, gerente, titular) VALUES (?, ?, ?, ?, ?)',
                                (agencia, numero, saldo, gerente, titular))
                conexao.commit()
                

    elif opcao == '2':
       
        # Adicionar pessoa
        cpf = input("Informe o cpf: ")
        nome = input("Nome da Pessoa: ")
        sobrenome =  input("Sobrenome da Pessoa: ")
        idade =  input("idade: ")

        agencia = input("Agencia bancaria: ")
        numero = input("Número da Conta: ")
        saldo = input("Saldo: ")
        gerente = input("Gerente: ")
       # titular = input("Titular da conta: ")

        
        cursor.execute('INSERT INTO pessoa (cpf, nome, sobrenome, idade) VALUES(?, ?, ?, ?)',
                        (cpf, nome, sobrenome, idade))
        conexao.commit()
        id_pessoa = cursor.lastrowid
        cursor.execute('INSERT INTO conta_bancaria ( agencia, numero, saldo, gerente, titular) VALUES (?, ?, ?, ?, ?)',
                        (agencia, numero, saldo, gerente, id_pessoa))
        conexao.commit()
      
        print("Linhas de pessoa adicionadas com sucesso!")
    
    elif opcao == '4':
        # Deletar

        id_conta = input("Id para deletar: ")
        cursor.execute('DELETE FROM conta_bancaria WHERE id = ?', (id_conta,))
        conexao.commit()
        print("Dados deletados com sucesso!")

        '''
        cpf = input("Cpf para excluir: ")
        cursor.execute('DELETE FROM pessoa WHERE cpf = ?', (cpf,))
        conexao.commit() #salva as alterações
        print("pessoa removidas com sucesso!")'''
        


    elif opcao == '3':
        #Atualizar

        cpf = input("CPF para editar")
        
        op = input()

        novo_nome = input("Nome atualizado: ")
        novo_sobrenome = input("Sobrenome atualizado: ")
        nova_idade = input("Idade atualizada: ")

        cursor.execute('UPDATE pessoa SET nome = ?, sobrenome = ?, idade = ? WHERE cpf = ?',
                        (novo_nome, novo_sobrenome, nova_idade, cpf))
        conexao.commit()
        print("Dados atualizados com sucesso!")
        
                  
    elif opcao == '5':
        # Sair
        break 

# Fechar a conexão com o banco de dados
conexao.close()
