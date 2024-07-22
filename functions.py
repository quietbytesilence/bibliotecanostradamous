import os, re
from unidecode import unidecode
from datetime import datetime, timedelta
def number(opt, msg='====='):
    print(msg)
    num = None; a = 'Inteiro' if opt == 2 else 'Decimal ou Inteiro'
    while True:
        valor = input('>>>> ').strip()
        try:
            if opt == 1:
                num = float(valor)
            elif opt == 2:
                num = int(valor)
            else:
                print('Erro Crítico: parâmetros incorretos!')
                return 0;
            break
        except ValueError:
            print(f'Valor Inválido! Por favor insira um número. {a}')
    return num;

def clear_term(pause=True):
    if pause:
        a = str(input('Press <ENTER> to Continue.'))
    os.system('cls' if os.name == 'nt' else 'clear')

def num_entre(n1, n2, msg='=====',tp=2):
    while True:
        num = number(tp, msg)
        if n1 <= num <= n2:
            return int(num);
            break
        print(f'Por favor, escolha valores entre {n1} e {n2}')

def validar_cpf():
    while True:
        try:
            cpf = input('Digite o CPF: ').strip()
            cpf = ''.join(filter(str.isdigit, cpf))
            if len(cpf) != 11:
                raise ValueError("CPF deve conter exatamente 11 dígitos.")
            soma = 0
            for i in range(9):
                soma += int(cpf[i]) * (10 - i)
            digito1 = 11 - (soma % 11)
            if digito1 > 9:
                digito1 = 0
            if int(cpf[9]) != digito1:
                raise ValueError("CPF inválido. Digito verificador 1 não confere.")
            soma = 0
            for i in range(10):
                soma += int(cpf[i]) * (11 - i)
            digito2 = 11 - (soma % 11)
            if digito2 > 9:
                digito2 = 0
            if int(cpf[10]) != digito2:
                raise ValueError("CPF inválido. Digito verificador 2 não confere.")
            return cpf
        except ValueError as e:
            print(f"Erro: {e}. Por favor, digite um CPF válido.")

def formatar(texto):
    texto_limpo = unidecode(texto)
    texto_limpo = re.sub(r'[^\w\s\/:.\\-]', '', texto_limpo)
    return texto_limpo.strip()

def validar_cep():
    while True:
        try:
            cep = input('Digite o CEP (apenas números ou com hífen): ').strip()
            cep = ''.join(filter(str.isdigit, cep))
            if len(cep) < 8 or len(cep) > 9:
                raise ValueError("CEP deve conter 8 dígitos (com hífen opcional).")
            if len(cep) == 9 and cep[5] != '-':
                raise ValueError("CEP com hífen inválido.")
            if '-' in cep:
                cep_parts = cep.split('-')
                cep = ''.join(cep_parts)
            if len(cep) != 8:
                raise ValueError("CEP inválido.")
            return cep
        except ValueError as e:
            print(f"Erro: {e}. Por favor, digite um CEP válido.")

def validar_isbn10():
    while True:
        try:
            isbn = input("Digite o ISBN-10 (com ou sem hífens): ").strip()
            isbn = isbn.replace('-', '').replace(' ', '')
            if len(isbn) != 10:
                raise ValueError("O ISBN deve conter exatamente 10 dígitos")
            if not isbn[:-1].isdigit():
                raise ValueError("Os primeiros 9 caracteres do ISBN devem ser dígitos")
            if isbn[-1].isdigit():
                digito_verificador = int(isbn[-1])
            elif isbn[-1].upper() == 'X':
                digito_verificador = 10
            else:
                raise ValueError("O último caractere do ISBN deve ser um dígito de 0 a 9 ou 'X'")
            soma = 0
            for i in range(9):
                soma += int(isbn[i]) * (i + 1)
            if soma % 11 == digito_verificador:
                print(f"ISBN-10 válido: {isbn}")
                return isbn
            else:
                print("ISBN-10 inválido. Tente novamente.")
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.")

def data_atual():
    hoje = datetime.today()
    data_formatada = hoje.strftime('%d/%m/%Y')
    return data_formatada

def soma_dias(data_inicial_str, dias_para_adicionar):
    data_inicial = datetime.strptime(data_inicial_str, '%d/%m/%Y')
    data_final = data_inicial + timedelta(days=dias_para_adicionar)
    data_final_str = data_final.strftime('%d/%m/%Y')
    return data_final_str

def atraso(data_hoje_str, data_entrega_str):
    data_hoje = datetime.strptime(data_hoje_str, '%d/%m/%Y')
    data_entrega = datetime.strptime(data_entrega_str, '%d/%m/%Y')
    dias_atraso = (data_hoje - data_entrega).days
    dias_atraso = int(dias_atraso)
    return dias_atraso if dias_atraso > 0 else 0