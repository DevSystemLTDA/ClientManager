import flet as ft

from .components import CustomButton, DateField, CustomTextField, TopTitle, Title
from .view import View

class FormPage(View):
    title_text = 'Title text'
    main_button_text = 'Button text'
    button_icon = ft.icons.MENU
    icon_button_command = None
    def __init__(self, **kwargs):
        self.title = Title(
            self.title_text,
            width=300
        )
        self.name_field = CustomTextField(label='Nome')
        self.date_field = DateField(self.page, width=200)
        self.tel_field = CustomTextField(
            label='Telefone',
            input_filter=ft.NumbersOnlyInputFilter()
        )
        self.email_field = CustomTextField(label='Email')
        self.address_field = CustomTextField(label='Endereço')
        self.cpf_field = CustomTextField(
            label='CPF',
            input_filter=ft.NumbersOnlyInputFilter()
        )
        self.rg_field = CustomTextField(
            label='RG',
            input_filter=ft.NumbersOnlyInputFilter()
        )
        self.main_button = CustomButton(
            self.main_button_text,
            on_click=self.on_submit
        )
        self.buttons = [self.main_button]
        if self.icon_button_command is None:
            self.icon_button_command = lambda e: e.page.show_drawer(self.drawer)
        super().__init__(**kwargs)

    def get_data(self):
        date = self.date_field.value
        return {
            'nome': self.name_field.value,
            'data_nasc': date if isinstance(date, str) else f'{date:%d/%m/%Y}',
            'tel': self.tel_field.value,
            'email': self.email_field.value,
            'endereco': self.address_field.value,
            'cpf': self.cpf_field.value,
            'rg': self.rg_field.value,
        }

    def on_submit(self, e):
        pass

    def generate_main_content(self):
        return ft.Column(
            horizontal_alignment=ft.alignment.center,
            controls=[
                ft.Stack(
                    controls=[
                        ft.IconButton(
                            icon=self.button_icon,
                            icon_color=ft.colors.GREY_100,
                            icon_size=30,
                            padding=0,
                            on_click=self.icon_button_command,
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
                            self.buttons,
                            alignment=ft.MainAxisAlignment.CENTER
                        )
                    ],
                    expand=True,
                    alignment=ft.MainAxisAlignment.SPACE_AROUND
                )
            )],
            alignment=ft.MainAxisAlignment.CENTER,
        )