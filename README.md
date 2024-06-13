# <p align="center">Projeto de Web Mining & Crawler Scraping<br>Bacen - Histórico das Taxas de Juros</p>

<p align="center">
<img src="http://img.shields.io/static/v1?label=LICENCA&message=...&color=GREEN&style=for-the-badge"/>     
<img src="http://img.shields.io/static/v1?label=STATUS&message=N/A&color=GREEN&style=for-the-badge"/>
</p>

Este projeto foi desenvolvido como parte de um desafio durante a disciplina de Web Mining & Crawler Scraping no curso de pós-graduação em Engenharia de Dados na Universidade de Fortaleza (Unifor).

O desafio consistia em desenvolver um scraper no site de nossa escolha, extrair e retornar os dados. Optei por raspar o histórico de taxas de juros do BACEN.

Para realizar esse processo, utilizei o Selenium para a raspagem de dados, o pandas para transformação e o SQLAlchemy ORM para persistência em banco de dados. O SQLAlchemy controlou o modelo de dados e realizou insert e update conforme necessário.

## Dependências do Projeto

Este projeto foi desenvolvido utilizando o Poetry + Pyenv para gerenciamento de ambientes virtuais e bibliotecas.

### Bibliotecas Utilizadas

- loguru
- selenium
- jupyter
- pandas
- lxml
- sqlalchemy
- psycopg2
- html5lib
- pyodbc

### Instalação das Dependências

Você pode instalar as dependências manualmente, ou, utilizando o Poetry ou o Pip com os seguintes comandos:

#### Utilizando Poetry

```bash
poetry install

```

#### Utilizando Pip

```bash
pip install -r requirements.txt

```

## Configurações do Projeto

O arquivo <code>./src/models/models.py</code> contém a definição da classe que representa a tabela do banco de dados, ou seja, a classe para armazenar o histórico de taxas de juros do BACEN, com os campos necessários para cada registro. Aqui eu aponto para a tabela historico_juros_taxas, mude se necessário.

O script SQL disponibilizado em <code>./sql</code> inclui o esquema da tabela, com detalhes sobre os tipos de dados, chaves primárias e quaisquer restrições adicionais necessárias.

### Como usar?

No script principal, o <code>./src/main.py</code>, na linha 11 existe a criação do objeto engine <code>db_engine = DBEngine("sqlserver", "localhost:5434", "sa", "Teste!1234", "BACEN")</code>, basta configurar na ordem:

- Banco para persistência(Postgres, SQL Server, MySQL etc)
- IP do banco
- Usuário
- Senha
- Database

### Qual banco usar?

A engine está adaptada para persistir os dados ou no Postgres ou no SQL Server, caso precise persistir em outros bancos, como MySQL, basta consultar a documentação do SQL Alchemy e adicionar uma nova opção na função <code>create_engine</code> existente no arquivo <code>./src/config/db_engine.py</code>.

#### Utilizando Docker

Tenho preparado no arquivo <code>docker-compose.yml</code> um container Postgres e um container SQL Server, que cria automaticamente o banco e as tabelas, caso queira utilizar um deles, prossiga com o comando:
<pre><code>docker-compose up -d</code></pre>

### Conclusão

Após realizar essa primeira configuração, o projeto está pronto para ser executado. Ele pode facilmente persistir em qualquer banco de dados relacional, desde que a Engine esteja configurada corretamente. Isso oferece uma ampla flexibilidade para adaptar o projeto a diferentes ambientes e requisitos de armazenamento de dados.

Para executar o projeto, utilize o seguinte comando:

```bash
python .\src\main.py
```
</p>

## Considerações Finais

- A documentação pode não estar tão detalhada; talvez seja necessário um certo nível de conhecimento para adaptar o código.
- Se tudo estiver configurado corretamente, basta executa o script e verificar a tabela no banco de dados usando o DBeaver ou outra ferramenta de sua preferencia.
- Tentei aplicar os conceitos de SOLID nesse projeto, por isso a estrutura pode parecer uma pouco confusa.

<hr>

![Image](https://i.imgur.com/p4vnGAN.gif)