""" REQUISITOS PARA O SISTEMA

• Cadastro de Livros: Permitir o cadastro de livros no sistema, incluindo informações como título, 
autor, ano de publicação, e número de cópias disponíveis. 
• Cadastro de Usuários: Possibilitar o cadastro de usuários da biblioteca, incluindo informações como nome, 
número de identificação, e contato. 
• Empréstimo de Livros: Permitir que um usuário solicite o empréstimo de um livro disponível na biblioteca. 
o Verificar a disponibilidade do livro antes de confirmar o empréstimo. o 
Atualizar o número de cópias disponíveis após o empréstimo. 
• Devolução de Livros: Permitir que um usuário devolva um livro previamente emprestado. 
o Atualizar o número de cópias disponíveis após a devolução. 
• Consulta de Livros: o Implementar uma funcionalidade que permita a consulta de livros por título, 
autor ou ano de publicação. 
• Relatórios: Gerar relatórios que exibam a lista de livros disponíveis, 
livros emprestados, usuários cadastrados, etc.

Modifique o código de acordo com a sua necessidade.
Esse código foi feito às pressas, pretendo refinar para excluir os métodos de consulta
que dependem de loops, visto o o Tinydb já possúi métodos própios.
No mais, estou iniciando com a tecnologia, expero que isso seja útil de alguma forma

"""
from functions import formatar, data_atual, soma_dias
from functions import validar_isbn10 as v_isbn
from functions import number as n
from functions import atraso
from functions import clear_term as limpa
from functions import validar_cep as v_cep
from functions import validar_cpf as v_cpf
from functions import num_entre as entre
from tinydb import TinyDB, Query
# Banco de dados dos Livros da Biblioteca
dbLivros = TinyDB('db-books.json', indent=2, encoding='utf-8')
# Banco de dados dos Usuários da Biblioteca
dbUsers = TinyDB('db-users.json', indent=2, encoding='utf-8')
# Banco de dados dos Empréstimos da Biblioteca
dbMov = TinyDB('db-movimentacoes.json', indent=2, encoding='utf-8')

def emprestar_devolver(operacao):
    isbn = v_isbn(); cpf = v_cpf()
    livros = dbLivros.all()
    if user_existe(cpf):
        if livro_existe(isbn):
            if operacao == 1:
                print('Emprestrando Livro')
                if consulta_livro(isbn, 4) > 1:
                    print('Movimentação Cadastrada com sucesso')
                    print(f'{consulta_user(cpf)} tem 5 dias para devolver {consulta_livro(isbn)}')
                    atulizar_quantidade(isbn, 2)
                    cadastrar_movimentacao(isbn, cpf, data_atual(), 2)
                    print(consulta_livro(isbn, 4))
                    limpa()
                else:
                    print(f'Há apenas uma exempar de {consulta_livro(isbn)}')
                    print(f'Infelizmente não pode ser emprestado')
                    limpa()
            elif operacao ==2:
                cadastrar_movimentacao(isbn, cpf, data_atual(), 1)
                atulizar_quantidade(isbn, 1)
        else:
            print('Livro não Cadastrado')
            limpa()
    else:
        print('Usuário não Cadastrado')
        limpa()     

def atulizar_quantidade(isbn, quantidade):
    # 1 - Adicionar
    # 2 - Remover
    if quantidade == 1:
        nova_disponibilidade = consulta_livro(isbn, 4) + 1
    elif quantidade == 2:
        nova_disponibilidade = consulta_livro(isbn, 4) - 1
    Livro = Query()
    dbLivros.update({'Disponiveis': nova_disponibilidade}, Livro.ISBN == isbn)
    
def multa(cpf, data_atual, data_entrega, prazo, isbn):
    dia = 2 #Multa por dia de atraso
    if atraso(data_atual, data_entrega):
        print(f'{consulta_user(cpf)} está em atraso com a biblioteca.')
        print(f'O livro {consulta_livro(isbn)} deveria ter sido devolvido em: {data_entrega}')
        print(f'A multa aplicada será de R$: {(atraso(data_atual, data_entrega) * dia):.2f}')
        limpa()


def cadastrar_movimentacao(isbn, cpf, data, tipo):
    # 1 - Devolver
    # 2 - Emprestrar
    users = dbMov.all()
    Usuario = Query()
    prazo = 5 #Prazo padrão de Empréstimo sem multa
    for user in users:
        if user['User'] == cpf:
            for user in users:
                if user['User'] == cpf:
                    if tipo == 1:
                        dbMov.update({'Atual': False}, Usuario.User == cpf)
                        dbMov.update({'Data': False}, Usuario.User == cpf)
                        dbMov.update({'Entrega': False}, Usuario.User == cpf)
                        multa(cpf, data_atual(), user['Entrega'], prazo, isbn)
                        return 0
                    elif tipo == 2:
                        livros = user['Livros Emprestados']
                        livros.append(isbn)
                        dbMov.update({'Livros Emprestados': livros}, Usuario.User == cpf)
                        dbMov.update({'Atual': isbn}, Usuario.User == cpf)
                        dbMov.update({'Data': data}, Usuario.User == cpf)
                        dbMov.update({'Entrega': soma_dias(data, prazo)}, Usuario.User == cpf)
                        return 0
    if tipo == 2:
            dbMov.insert({
                'User': cpf,
                'Data': data,
                'Entrega': soma_dias(data, prazo),
                'Livros Emprestados': [isbn],
                'Atual': isbn
                })
    else:
        print(f'{consulta_user(cpf)} não pussuí empréstimos ativos')

def ultimo_id():
    livros = dbLivros.all()
    if not livros:
        return 1
    ultimo = max(livro['Codigo'] for livro in livros)
    return ultimo + 1 

def consulta_user(cpf, tipo=1):
    # 1 - Nome
    # 2 - Dados Cadastrais
    users = dbUsers.all()
    if tipo == 1:
        for user in users:
            if cpf == user['CPF']:
                return user['Nome']
    elif tipo == 2:
        for user in users:
            if cpf == user['CPF']:
                for livro in dbMov.all():
                    if livro['User'] == cpf:
                        history = livro['Livros Emprestados']
                        titulos = []
                        for iten in history:
                            titulos.append(consulta_livro(iten))

                print(f"""
Dados do Usuário
Nome Completo: {user['Nome']}
CPF: {user['CPF']}
Contato: {user['Contato']}
CEP: {user['CEP']}
Rua: {user['Rua']}
Número da Casa: {user['Casa']}
Livros Emprestados: {titulos}
                    """)

def consulta_livro(isbn, tipo=1):
    # 1 - Consultar Nome
    # 2 - Consultar Dados
    # 3 - Consultar Disponibilidade
    # 4 - Para uso interno da função
    livros = dbLivros.all()
    for livro in livros:
        if isbn == livro['ISBN']:
            if tipo == 1:
                return livro['Titulo']
            elif tipo == 2:
                print(f"""
Dados do Livro
Título: {livro['Titulo']}
Autor: {livro['Autor']}
Ano de Publicação: {livro['Ano']}
Exemplares: {livro['Disponiveis']}
ISBN-10:  {livro['ISBN']}
Code: {livro['Codigo']}
                    """)
                return 0
            elif tipo == 3:
                print('Em desenvolvimento')
                return 0
            elif tipo == 4:
                return livro['Disponiveis']

def user_existe(cpf):
    users = dbUsers.all()
    if not users:
        return False
    for user in users:
        if cpf == user['CPF']:
            return True
    return False

def livro_existe(isbn):
    livros = dbLivros.all()
    if not livros:
        return False
    for livro in livros:
        if isbn == livro['ISBN']:
            return True

def adicionar_user(nome, cpf, contato, cep, casa, rua):
    dbUsers.insert({
        'Nome': formatar(nome),
        'CPF': cpf,
        'Contato': contato,
        'CEP': cep,
        'Casa': casa,
        'Rua': formatar(rua),
        })

def dados_user():
    qto = n(2, 'Quantos Usuários deseja cadastrar? ')
    for _ in range(qto):
        cpf = v_cpf()
        if not user_existe(cpf):
            nome = str(input('Digite o nome Completo do Usuário: ')).strip().title()
            contato = str(input('Digite seu o Número de Contato: '))
            cep = v_cep()
            casa = n(2,'Número da Casa: ')
            rua = str(input('Nome da Rua: ')).strip().title()
            adicionar_user(nome, cpf, contato, cep, casa, rua)
        else:
            print(f'Usuário {consulta_user(cpf)} Já Cadastrado!')
            limpa()

def adicionar_livro(titulo, ano, autor, dispo, isbn):
    dbLivros.insert({
        'Codigo': ultimo_id(),
        'Titulo': formatar(titulo),
        'Ano': ano,
        'Autor': formatar(autor),
        'Disponiveis': dispo,
        'ISBN': isbn
        })
    print(f'Livro \033[1;34m{titulo}\033[0m adicionado com sucesso!\nCode: \033[31;4m{codigo}\033[0m')
    limpa()

def dados_livro():
    qto = n(2, 'Quantos Livros deseja cadastrar? ')
    for _ in range(qto):
        isbn = v_isbn()
        if not livro_existe(isbn):      
            titulo = str(input('Título do Livro: ')).strip().title()
            ano = n(2, 'Ano de Publicação do Livro: ')
            autor = str(input('Autor do Livro: ')).strip().title()
            exemplares = n(2, 'Exemplares disponíveis: ')
            adicionar_livro(titulo, ano, autor, exemplares, isbn)
        else:
            print(f'Livro {consulta_livro(isbn)} já Cadastrado!')
            limpa()

def pendencias(cpf):
    for user in dbMov.all():
        if user['User'] == cpf:
            if user['Atual'] != False:
                print(f"O Usuário {consulta_user(cpf)} tem um empréstimo ativo")
                print(f"Livro Atual: {consulta_livro(user['Atual'])}")
                print(f"Data do empréstimo: {user['Data']}")
                print(f"Prazo de Entrega: {user['Entrega']}")
                print(f"Atraso: {atraso(data_atual(), user['Entrega'])}")
            else:
                print(f"Usuário {consulta_user(cpf)} não pussuí empréstimos ativos")

def relatorio():
    print("Relatório de Livros Disponíveis:")
    livros = dbLivros.all(); exemplares = []
    for livro in livros:
        if livro['Disponiveis'] > 0:
            print(f"{livro['Titulo']} - {livro['Disponiveis']} cópias disponíveis")
            exemplares.append(livro['Disponiveis'])
    print(f'Total de livros disponíveis {sum(exemplares)}')
    print("\nRelatório de Empréstimos:")
    movimentacoes = dbMov.all()
    for mov in movimentacoes:
        if mov['Atual']:
            print(f"Usuário: {consulta_user(mov['User'])} - Livro: {consulta_livro(mov['Atual'])} - Data de Empréstimo: {mov['Data']} - Prazo de Entrega: {mov['Entrega']}")

def consulta():
    while True:
        print('''
[0] - Voltar
[1] - Usuário
[2] - Livro
            ''')
        op = n(2)
        if op == 0:
            break
        elif op == 1:
            cpf = v_cpf()
            if user_existe(cpf):
                print('''
[0] - Voltar
[1] - Nome
[2] - Pendencias
[3] - Tudo
                    ''')
                op = n(2)
                if op == 0:
                    pass
                elif op == 1:
                     consulta_user(cpf)
                     limpa()
                elif op == 2:
                    pendencias(cpf)
                    limpa()
                elif op == 3:
                    consulta_user(cpf, 2)
                    limpa()
            else:
                print('Usuário não Cadastrado')
                limpa()
        elif op == 2:
            print('''
[0] - Voltar
[1] - Nome
[2] - ISBN
[3] - Autor
[4] - Ano
                ''')
            op = n(2)
            if op == 0:
                pass
            elif op in [1,2,3,4]:
                termo = formatar(str(input('Digite o termo: ')).strip().title())
                livro_isbn(termo, op)

def livro_isbn(termo, tipo):
    r = 0 # variavel dos resultados
    for livro in dbLivros.all():
        if tipo == 1:
            if livro['Titulo'] == termo:
                consulta_livro(livro['ISBN'], 2)
                r +=1
        elif tipo == 2:
            if livro['ISBN'] == termo:
                consulta_livro(termo, 2)
                r +=1
        elif tipo == 3:
            if livro['Autor'] == termo:
                consulta_livro(livro['ISBN'], 2)
                r +=1
        elif tipo == 4: #int
            termo = int(termo)
            if livro['Ano'] == termo:
                consulta_livro(livro['ISBN'], 2)
                r +=1
    if r <= 0:
        print(f'Livro não encontrado')

while True:
    limpa(False)
    print('''Biblioteca Pública Nostradamous
[0] - Sair
[1] - Cadastrar Livro
[2] - Cadastrar Usuário
[3] - Emprestrar Livro
[4] - Devolver Livro
[5] - Gerar Relatório
[6] - Consultar

Apenas para uso educacional
by: Gustavo Carneiro @quietbytesilence
        ''')
    opcao = entre(0, 6, 'Digite sua escolha')
    if opcao == 1:
        dados_livro()
    elif opcao == 2:
        dados_user()
    elif opcao == 3:
        emprestar_devolver(1)
    elif opcao == 4:
        emprestar_devolver(2)
    elif opcao == 5:
        relatorio()
        limpa()
    elif opcao == 6:
        consulta()
    else:
        exit()