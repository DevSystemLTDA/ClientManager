import datetime

import flet as ft

from .components import CustomButton, CustomTextField, Title, TopTitle
from .control import Control
from .view import View

class LoginTextField(CustomTextField):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.width = 450

class LoginPage(View):
    login_field = LoginTextField(label='Login')
    password_field = LoginTextField(
        label='Senha',
        password=True,
        can_reveal_password=True,
    )

    def on_pre_view(self):
        self.login_field.value = ''
        self.password_field.value = ''

    def generate_main_content(self):
        return ft.Column(
            horizontal_alignment=ft.alignment.center,
            controls=[
                TopTitle(),
                ft.Stack( # TITLE AND HORIZONTAL LINE
                    expand=True,
                    controls=[
                        self.generate_login_form(),
                        ft.Row(
                            [
                                Title(
                                    'LOGIN',
                                    width=300
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                ]),
        ])

    def generate_login_form(self):
        return ft.Row(
            controls=[
                ft.Container(
                    border=ft.border.only(top=ft.BorderSide(
                        3, ft.colors.GREY)
                    ),
                    expand=True,
                    margin=ft.margin.only(top=15, bottom=30), # TO CENTRALIZE TOP BORDER ON TITLE
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            self.generate_form_content()
                        ]
                    )
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )

    def generate_form_content(self):
        def login(e):
            if Control.check_credentials(
                self.login_field.value,
                self.password_field.value
            ):
                e.page.client_storage.set('logged', f"{datetime.datetime.today():%d/%m}")
                e.page.snack_bar.message('Login realizado!', 'success')
                return e.page.go('/clients')
            return e.page.snack_bar.message('Login ou senha inválidos', 'error')

        return ft.Container(
            border=ft.border.all(3, ft.colors.GREY),
            border_radius=50,
            width=750,
            margin=ft.margin.only(
                top=30,
                bottom=80
            ),
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                controls=[
                    self.login_field,
                    self.password_field,
                    CustomButton('ENTRAR', login)
                ]
            )
        )
