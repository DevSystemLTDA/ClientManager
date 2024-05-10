import datetime

import flet as ft

class NavigationDrawer(ft.NavigationDrawer):
    routes = ['/clients', '/register']
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controls=[
            ft.Stack(
                height=85,
                controls=[
                    ft.Image(
                        src='img/smaller_logo.png',
                        width=150,
                        height=75,
                        bottom=0,
                    )
                ]
            ),
            ft.Divider(
                color=ft.colors.WHITE,
                thickness=2
            ),
            ft.NavigationDrawerDestination(
                label="CLIENTES CADASTRADOS"
            ),
            ft.NavigationDrawerDestination(
                label="CADASTRAR CLIENTE"
            ),
        ]

        self.on_change = self.on_change_func

    def on_change_func(self, e):
        e.page.go(
            self.routes[self.selected_index]
        )
        self.open = False

class View(ft.View):
    def __init__(self, page, **kwargs):
        super().__init__(**kwargs)
        self.page = page
        self.drawer = self.page.drawer
        self.controls = [ft.Container(
            image_src='img/background.png',
            image_fit=ft.ImageFit.COVER,
            expand=True,
            content=self.generate_main_content()
        )]

    def generate_main_content(self):
        return ft.Text('Generate main content')

    def on_pre_view(self, page=None):
        pass

class CustomButton(ft.Container):
    def __init__(self, text, on_click, **kwargs):
        super().__init__(**kwargs)
        self.content = ft.TextButton(
            content=ft.Text(
                text,
                font_family='Garet',
                color=ft.colors.WHITE
            ),
            on_click=on_click
        )
        self.width = 200
        self.height = 45
        self.border = ft.border.all(2, ft.colors.WHITE)
        self.border_radius = 50
        self.bgcolor = ft.colors.GREY_800

class RegisterTextField(ft.TextField):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        bgcolor = '#dddddd'
        self.label_style = ft.TextStyle(
            color = ft.colors.GREY_800
        )
        self.color = ft.colors.GREY_800
        self.text_style = ft.TextStyle(
            font_family = "Garet"
        )
        self.focused_border_color = bgcolor
        self.border = ft.InputBorder.OUTLINE
        self.border_color = bgcolor
        self.border_radius = 90
        self.filled = True
        self.bgcolor = bgcolor
        self.height = 45
        self.expand = True
        self.expand_loose = True

class ClientTextField(RegisterTextField):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text_size = 15
        self.disabled = True

class LoginTextField(RegisterTextField):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.width = 450

class Title(ft.Container):
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)
        self.alignment = ft.alignment.center
        self.bgcolor = ft.colors.GREY_100
        self.border_radius = 25
        self.height = 30
        self.border = ft.border.all(2, ft.colors.GREY)
        self.content = ft.Text(
            text,
            font_family='Garet-Heavy',
            color=ft.colors.GREY_600
        )

class TopTitle(ft.Row):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controls = [
            ft.Container(
                bgcolor=ft.colors.WHITE,
                width=150,
                height=150,
                border_radius=20,
                content=ft.Image(
                    border_radius=90,
                    src="img/logo.png",
                    width=150,
                    height=150,
                    fit=ft.ImageFit.CONTAIN,
                ),
            ),
            ft.Text('DEV.SYSTEMS', size=40)
        ]
        self.alignment = ft.MainAxisAlignment.CENTER

class Message(ft.SnackBar):
    def __init__(self, page, **kwargs):
        super().__init__(
            content=ft.Text(
                'Default message',
                color=ft.colors.GREY_100
            ),
            shape=ft.RoundedRectangleBorder(radius=50),
            margin=10,
            bgcolor=ft.colors.GREY_800,
            **kwargs
        )
        self.page = page

    def message(self, text):
        self.content.value = text
        self.open = True
        self.page.update()

class DateField(ft.Container):
    def __init__(self, page, value='', disabled=False, **kwargs):
        super().__init__(**kwargs)

        self._value = value

        def on_change(_):
            self.value = self.date_picker.value

        self.date_picker = ft.DatePicker(
            on_change=on_change,
            value=value,
            last_date=datetime.datetime.today()
        )
        page.overlay.append(self.date_picker)

        self.text = ClientTextField(
            label='Data de nascimento',
            value=value if isinstance(value, str) else f'{value:%d/%m/%Y}',
            color=ft.colors.GREY_800,
            text_style=ft.TextStyle(
                font_family = "Garet"
            ),
            disabled=True,
        )

        self.alignment = ft.alignment.center
        self.content = self.text
        self.height = 45
        if not disabled:
            self.on_click = lambda _: self.date_picker.pick_date()

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        self.text.value = value if isinstance(value, str) else f'{value:%d/%m/%Y}'
        try:
            self.text.update()
        except AssertionError:
            return None