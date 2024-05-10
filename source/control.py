from bcrypt import checkpw

from .models import Data

class Control:
    print('Apagar dados expostos em Control')
    @classmethod
    def check_credentials(cls, login: str, password: str):
        # devsystems
        # minhasenha654
        return checkpw(
            login.encode('utf-8'),
            Data.get_value('login').encode('utf-8')
        ) and checkpw(
            password.encode('utf-8'),
            Data.get_value('pw').encode('utf-8')
        )
    
    @classmethod
    def validate_form(cls, data: dict):
        for i in data:
            data[i] = data[i].strip()

        if '' in list(data.values()):
            return 'Preencha todos os campos!'

        name = data['nome']
        if not name.count(' '):
            return 'Digite seu nome completo!'

        email = data['email']
        if any([
            '@' not in email,
            ' ' in email,
            '.' not in email.split('@')[-1],
        ]):
            return 'Email inválido!'

        cpf = data['cpf']
        if not cpf.isdigit():
            return 'Digite apenas os dígitos do CPF!'
        if len(cpf) != 11:
            return 'CPF inválido!'

        rg = data['rg']
        if not rg.isdigit():
            return 'Digite apenas os dígitos do RG!'
        if len(rg) != 11:
            return 'rg inválido!'

        return None