from .components import Title
from .register_page import CustomButton, RegisterPage

class UpdatePage(RegisterPage):
    title = Title(
        'ALTERAR CLIENTE',
        width=300
    )
    button = CustomButton(
        'SALVAR ALTERAÇÔES', 
        lambda _: print('Opa')
    )
    def on_pre_view(self, page):
        d = page.data
        self.name_field.value = d.get('nome')
        self.date_field.value = d.get('data_nasc')
        self.tel_field.value = d.get('tel')
        self.email_field.value = d.get('email')
        self.address_field.value = d.get('endereco')
        self.cpf_field.value = d.get('cpf')
        self.rg_field.value = d.get('rg')