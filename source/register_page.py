import flet as ft

from .components import CustomButton, DateField, RegisterTextField, TopTitle, Title, View
from .control import Control
from .models import Cliente

class RegisterPage(View):
    title = Title(
        'CADASTRO DO CLIENTE',
        width=300
    )
    def __init__(self, page, **kwargs):
        self.name_field = RegisterTextField(label='Nome')
        self.date_field = DateField(page, width=200)
        self.tel_field = RegisterTextField(
            label='Telefone',
            input_filter=ft.NumbersOnlyInputFilter()
        )
        self.email_field = RegisterTextField(label='Email')
        self.address_field = RegisterTextField(label='Endereço')
        self.cpf_field = RegisterTextField(
            label='CPF',
            input_filter=ft.NumbersOnlyInputFilter()
        )
        self.rg_field = RegisterTextField(
            label='RG',
            input_filter=ft.NumbersOnlyInputFilter()
        )
        self.button = CustomButton(
            'CADASTRAR', 
            on_click=self.create_client
        )
        super().__init__(page, **kwargs)

    def create_client(self, e):
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

    def on_pre_view(self, page):
        self.name_field.value = ''
        self.date_field.value = ''
        self.tel_field.value = ''
        self.email_field.value = ''
        self.address_field.value = ''
        self.cpf_field.value = ''
        self.rg_field.value = ''
        return super().on_pre_view()

    def generate_main_content(self):
        return ft.Column(
            horizontal_alignment=ft.alignment.center,
            controls=[
                ft.Stack(
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.MENU,
                            icon_color=ft.colors.GREY_100,
                            icon_size=30,
                            padding=0,
                            on_click=lambda _: self.page.show_drawer(self.drawer),
                            left=0,
                            bottom=0,
                        ),
                        TopTitle(),
                    ]
                ),
                ft.Stack(
                    expand=True,
                    controls=[
                        self.generate_form(), # FORM CONTAINER
                        ft.Row([self.title], alignment=ft.MainAxisAlignment.CENTER),
                ]),
        ])

    def generate_form(self):
        return ft.Container(
            border=ft.border.only(top=ft.BorderSide(
                3, ft.colors.GREY)
            ),
            expand=True,
            margin=ft.margin.only(top=15), # TO CENTRALIZE TOP BORDER ON TITLE
            content=ft.Container(
                margin=ft.margin.only(
                    top=30,
                    bottom=80
                ),
                content=ft.Stack([
                    self.generate_form_content(),
                    ft.Row([
                        Title(
                            'INFORMAÇÕES',
                            width=200
                        )],
                        alignment=ft.MainAxisAlignment.CENTER,
                    )],
                )
            )
        )

    def generate_form_content(self):
        return ft.Row([ft.Container(
                border=ft.border.all(2, ft.colors.GREY),
                width=700,
                border_radius=25,
                margin=ft.margin.only(top=15),
                padding=ft.padding.only(
                    top=40,
                    left=20,
                    right=20,
                    bottom=20
                ),
                content=ft.Column([
                        ft.Row([
                            self.name_field,
                            self.date_field
                        ]),
                        ft.Row([
                            self.tel_field,
                            self.email_field,
                        ]),
                        self.address_field,
                        ft.Row([
                            self.cpf_field,
                            self.rg_field,
                        ]),
                        ft.Row(
                            [self.button],
                            alignment=ft.MainAxisAlignment.CENTER
                        )
                    ],
                    expand=True,
                    alignment=ft.MainAxisAlignment.SPACE_AROUND
                )
            )],
            alignment=ft.MainAxisAlignment.CENTER,
        )