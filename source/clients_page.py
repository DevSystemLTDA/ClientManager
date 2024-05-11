import datetime

import flet as ft

from .components import TopTitle, Title, ClientTextField, DateField
from .models import Cliente
from .view import View

class ClientsPage(View):
    def on_pre_view(self):
        self.grid_view.controls = [ClientCard(self.page, c.get_data()) for c in Cliente.select()]
        return super().on_pre_view()

    def generate_main_content(self):
        return ft.Column(
            horizontal_alignment=ft.alignment.center,
            controls=[
                ft.Stack( # TITLE AND HORIZONTAL LINE
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
                ft.Stack( # TITLE AND HORIZONTAL LINE
                    expand=True,
                    controls=[
                        self.generate_clients(),
                        ft.Row(
                            [
                                Title(
                                    'CLIENTES CADASTRADOS',
                                    width=300
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                ]),
        ])

    def generate_clients(self):
        self.grid_view = ft.GridView(
            controls=[ClientCard(self.page, c.get_data()) for c in Cliente.select()],
            child_aspect_ratio=.75,
            runs_count=4,
            expand=1
        )
        return ft.Container(
            border=ft.border.only(top=ft.BorderSide(
                3, ft.colors.GREY)
            ),
            expand=True,
            margin=ft.margin.only(top=15), # TO CENTRALIZE TOP BORDER ON TITLE
            content=ft.Row(
                controls=[
                    ft.Container(
                        margin=ft.margin.only(
                            top=30,
                            bottom=10
                        ),
                        height=1200,
                        expand=True,
                        expand_loose=True,
                        content=self.grid_view,
                        )
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )

class ClientCard(ft.Container):
    fields = {
        'Nome': 'nome',
        'Telefone': 'tel',
        'Data de Nascimento': 'data_nasc',
        'CPF': 'cpf',
        'RG': 'rg',
        'Endereço': 'endereco',
        'Email': 'email',
    }
    def __init__(self, page, data, **kwargs):
        super().__init__(**kwargs)
        self.page = page
        self.data = data
        bgcolor = ft.colors.GREY_100
        self.alignment = ft.alignment.center
        self.bgcolor = bgcolor
        self.border_radius = 25
        self.border = ft.border.all(2, bgcolor)
        self.height = 30
        self.content = self.generate_content()
        def on_click(e):
            self.page.data = data
            self.page.go('/update')
        self.on_click = on_click

    def generate_content(self):
        card_controls = [ft.Row([self.generate_title()])]
        for field, attr in self.fields.items():
            if attr == 'data_nasc':
                card_controls.append(DateField(
                    self.page,
                    disabled=True,
                    width=500,
                    value=datetime.datetime.strptime(
                        self.data[attr], '%d/%m/%Y',
                    )
                ))
            else:
                card_controls.append(ClientTextField(
                    label=field, value=str(self.data[attr])
                ))
        return ft.Column(
            controls=card_controls,
            spacing=5,
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

    def generate_title(self):
        return ft.Stack(
            controls=[
                ft.Container(
                    content=ft.Text(
                        'DEV SYSTEMS',
                        italic=True,
                        font_family='Garet-Heavy',
                    ),
                    bgcolor=ft.colors.GREY_900,
                    border=ft.border.all(1, ft.colors.GREY_900),
                    border_radius=50,
                    height=50,
                    width=500,
                    padding=ft.padding.only(
                        left=75, top=15
                    ),
                    margin=ft.margin.only(top=10, left=1, right=5),
                ),
                ft.Container(
                    content=ft.Icon(
                        ft.icons.ACCOUNT_CIRCLE,
                        color=ft.colors.GREY_900,
                        size=70
                    ),
                    padding=ft.padding.all(0),
                    bgcolor=ft.colors.GREY_100,
                    border=ft.border.all(1, ft.colors.GREY_100),
                    border_radius=90,
                ),
            ],
            expand=True
        )