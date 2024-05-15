import flet as ft

class View(ft.View):
    page = None
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.drawer = self.page.drawer
        self.controls = [ft.Container(
            image_src='img/background.png',
            image_fit=ft.ImageFit.COVER,
            expand=True,
            content=ft.Stack(
                controls=[
                    self.generate_main_content(),
                    ft.Text(
                        'Aperte F1 para abrir ou fechar o menu\nAperte F11 para entrar ou sair da tela cheia',
                        size=12,
                        top=0,
                        right=5
                    )
                ]
            )
        )]

    def on_pre_view(self):
        pass

    def generate_main_content(self):
        return ft.Text('Generate main content')
