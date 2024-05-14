import flet as ft

from .components import CustomButton
from .control import Control
from .form_page import FormPage
from .models import Cliente

class UpdatePage(FormPage):
    title_text = 'ALTERAR CLIENTE'
    main_button_text = 'SALVAR ALTERAÇÔES'
    button_icon = ft.icons.ARROW_BACK
    icon_button_command = lambda _, e: e.page.go('/clients')
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text_button = ft.TextButton(
            "Sim", 
            on_click=self.delete_client,
            style=ft.ButtonStyle(
                bgcolor=ft.colors.RED,
                color=ft.colors.WHITE
            )
        )
        self.buttons.insert(0, CustomButton(
            'EXCLUIR',
            on_click=self.open_dialog,
            bgcolor=ft.colors.RED
        ))
        self.dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Confirmação de exclusão"),
            content=ft.Text("Você quer deletar esse cliente?"),
            actions=[
                self.text_button,
                ft.TextButton("Não", on_click=self.close_dialog),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

    def on_pre_view(self):
        self.main_button.disabled = False
        self.text_button.disabled = False
        d = self.page.data
        self.name_field.value = d.get('nome')
        self.date_field.value = d.get('data_nasc')
        self.tel_field.value = d.get('tel')
        self.email_field.value = d.get('email')
        self.address_field.value = d.get('endereco')
        self.cpf_field.value = d.get('cpf')
        self.rg_field.value = d.get('rg')

    def on_submit(self, e):
        data = self.get_data()
        error_message = Control.validate_form(data)
        if error_message is not None:
            return e.page.snack_bar.message(error_message, 'error')

        self.main_button.disabled = True

        client_id = e.page.data['id']

        Cliente.get(id=client_id).update(**data)

        data['id'] = client_id

        e.page.data = {'instruction': {'update': data}}

        e.page.snack_bar.message('Cliente atualizado com sucesso!', 'success')
        return e.page.go('/clients')
    
    def delete_client(self, e):

        self.text_button.disabled = True

        client_id = e.page.data['id']

        Cliente.get(id=client_id).delete_instance()

        e.page.data = {'instruction': {'delete': client_id}}

        self.close_dialog(e)

        e.page.snack_bar.message('Cliente excluído com sucesso!', 'success')
        return e.page.go('/clients')

    def close_dialog(self, e):
        e.page.dialog.open = False
        e.page.update()

    def open_dialog(self, e):
        e.page.dialog = self.dialog
        e.page.dialog.open = True
        e.page.update()
