# Biblioteca Pública Nostradamous

![GitHub](https://img.shields.io/badge/license-MIT-blue) ![Python](https://img.shields.io/badge/python-3.x-green)

O **Biblioteca Pública Nostradamous** é um sistema de gerenciamento de biblioteca desenvolvido em Python, utilizando o banco de dados **TinyDB** para armazenamento de dados. Este projeto foi criado para fins educacionais e demonstra como implementar funcionalidades básicas de uma biblioteca, como cadastro de livros e usuários, empréstimos, devoluções e geração de relatórios.

---

## Funcionalidades

- **Cadastro de Livros**: Permite cadastrar livros com informações como título, autor, ano de publicação e número de cópias disponíveis.
- **Cadastro de Usuários**: Possibilita o cadastro de usuários com informações como nome, CPF, contato e endereço.
- **Empréstimo de Livros**: Permite que usuários solicitem o empréstimo de livros disponíveis, atualizando o número de cópias.
- **Devolução de Livros**: Registra a devolução de livros e atualiza o número de cópias disponíveis.
- **Consulta de Livros e Usuários**: Oferece funcionalidades de consulta por título, autor, ano de publicação ou CPF.
- **Relatórios**: Gera relatórios de livros disponíveis, livros emprestados e usuários cadastrados.
- **Validações**: Inclui validações de CPF, ISBN e CEP para garantir a integridade dos dados.

---

## Pré-requisitos

Antes de começar, certifique-se de que você tem os seguintes requisitos instalados:

- **Python 3.x**: O projeto foi desenvolvido em Python 3. Recomenda-se a versão mais recente.
- **TinyDB**: Biblioteca utilizada para armazenamento de dados em arquivos JSON.
- **Unidecode**: Biblioteca utilizada para normalização de textos.

Você pode instalar as dependências necessárias usando o `pip`:

```bash
pip install tinydb unidecode
```

---

## Como Usar

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/quietbytesilence/bibliotecanostradamous.git
   cd biblioteca-nostradamous
   ```

2. **Execute o programa**:

   ```bash
   python nostradamous.py
   ```

3. **Menu Principal**:

   O sistema exibirá um menu com as seguintes opções:

   ```
   Biblioteca Pública Nostradamous
   [0] - Sair
   [1] - Cadastrar Livro
   [2] - Cadastrar Usuário
   [3] - Emprestar Livro
   [4] - Devolver Livro
   [5] - Gerar Relatório
   [6] - Consultar
   ```

   - **Cadastrar Livro**: Adicione novos livros ao sistema.
   - **Cadastrar Usuário**: Registre novos usuários na biblioteca.
   - **Emprestar Livro**: Realize empréstimos de livros para usuários cadastrados.
   - **Devolver Livro**: Registre a devolução de livros emprestados.
   - **Gerar Relatório**: Visualize relatórios de livros disponíveis, emprestados e usuários cadastrados.
   - **Consultar**: Pesquise livros por título, autor, ISBN ou ano de publicação, e consulte informações de usuários.

---

## Estrutura do Projeto

- **`nostradamous.py`**: Contém a lógica principal do sistema, incluindo as funcionalidades de cadastro, empréstimo, devolução e consulta.
- **`functions.py`**: Contém funções auxiliares, como validações de CPF, ISBN e CEP, formatação de textos e manipulação de datas.
- **Banco de Dados**:
  - `db-books.json`: Armazena os dados dos livros cadastrados.
  - `db-users.json`: Armazena os dados dos usuários cadastrados.
  - `db-movimentacoes.json`: Armazena os registros de empréstimos e devoluções.

---

## Exemplos de Uso

### Cadastrar um Livro

1. Escolha a opção **1 - Cadastrar Livro** no menu principal.
2. Insira os dados solicitados: título, autor, ano de publicação, número de cópias e ISBN.

### Emprestar um Livro

1. Escolha a opção **3 - Emprestar Livro** no menu principal.
2. Insira o CPF do usuário e o ISBN do livro.
3. O sistema verificará a disponibilidade do livro e registrará o empréstimo.

### Gerar Relatório

1. Escolha a opção **5 - Gerar Relatório** no menu principal.
2. O sistema exibirá uma lista de livros disponíveis e empréstimos ativos.

---

## Contribuição

Contribuições são bem-vindas! Se você deseja melhorar este projeto, siga os passos abaixo:

1. Faça um fork do repositório.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas alterações (`git commit -m 'Adicionando nova feature'`).
4. Faça push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

---

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## Autor

- **Gustavo Carneiro** ([@quietbytesilence](https://github.com/quietbytesilence))
- Projeto criado para fins educacionais.

---

## Agradecimentos

- À comunidade Python por fornecer ferramentas incríveis para desenvolvimento.
- Ao TinyDB por oferecer uma solução simples e eficiente para armazenamento de dados.

---

Espero que este projeto seja útil para você! Se tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato. 😊
