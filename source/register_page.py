from .control import Control
from .form_page import FormPage
from .models import Cliente

class RegisterPage(FormPage):
    title_text = 'CADASTRO DO CLIENTE'
    button_text = 'CADASTRAR'
    def on_submit(self, e):
        date = self.date_field.value
        data = {
            'nome': self.name_field.value,
            'data_nasc': date if isinstance(date, str) else f'{date:%d/%m/%Y}',
            'tel': self.tel_field.value,
            'email': self.email_field.value,
            'endereco': self.address_field.value,
            'cpf': self.cpf_field.value,
            'rg': self.rg_field.value,
        }
        error_message = Control.validate_form(data)
        if error_message is not None:
            return e.page.snack_bar.message(error_message)

        Cliente.create(**data)
        e.page.snack_bar.message('Cliente criado com sucesso!')
        return e.page.go('/clients')

    def on_pre_view(self):
        self.name_field.value = ''
        self.date_field.value = ''
        self.tel_field.value = ''
        self.email_field.value = ''
        self.address_field.value = ''
        self.cpf_field.value = ''
        self.rg_field.value = ''