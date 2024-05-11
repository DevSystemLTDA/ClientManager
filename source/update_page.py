import flet as ft

from .components import CustomButton
from .form_page import FormPage

class UpdatePage(FormPage):
    title_text = 'ALTERAR CLIENTE'
    main_button_text = 'SALVAR ALTERAÇÔES'
    button_icon = ft.icons.ARROW_BACK
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.buttons.insert(0, CustomButton(
            'EXCLUIR',
            on_click=lambda _: print('Hi'),
            bgcolor=ft.colors.RED
        ))
        self.icon_button_command = lambda e: e.page.go('/clients')

    def on_submit(self, e):
        pass

    def on_pre_view(self):
        d = self.page.data
        self.name_field.value = d.get('nome')
        self.date_field.value = d.get('data_nasc')
        self.tel_field.value = d.get('tel')
        self.email_field.value = d.get('email')
        self.address_field.value = d.get('endereco')
        self.cpf_field.value = d.get('cpf')
        self.rg_field.value = d.get('rg')