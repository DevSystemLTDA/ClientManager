<p align="center">
    <img src="/assets/img/logo.png" alt="Logo" width=200 height=200>
</p>

# ClientManager

O ClientManager consiste num sistema, protegido com login e senha, cuja função é gerenciar cadastros de clientes de uma empresa fictícia.

## Funcionalidades

- Cadastro, atualização e exclusão de registros de clientes;
- Visualização dos clientes cadastrados;
- Segurança com o login e senha.

## Tecnologias usadas

- Python;
- Framework Flet;
- Bcrypt, para criptografia;
- Peewee, como *Object Relational Mapping*;
- Dotenv.

## Instalação

Para instalar o projeto, siga os seguintes passos:

1. [Instale o python](https://www.python.org/downloads/) mais recente em sua máquina
2. Clone o projeto:

    ```
    git clone https://github.com/DevsystemsLTDA/ClientManager ClientManager
    ```

3. Entre na pasta do projeto, crie e ative um ambiente virtual:

    - Windows:

        ```
        cd ClientManager
        python -m venv venv
        venv\Scripts\activate
        ```

    - Linux/MacOS:

        ```
        cd ClientManager
        python3 -m venv venv
        source venv/bin/activate
        ```

4. Instale as dependências do projeto:

    ```
    pip install -r requirements.txt
    ```

5. Agora, rode o seguinte comando para gerar seu login e senha:

    ```
    python generate_env.py
    ```

6. Para iniciar o projeto, rode o seguinte comando:

    ```
    python app.py
    ```

## Contribuição

Fique à vontade para fazer Forks e várias Pull Requests. Estou aberto a sugestões e melhorias.