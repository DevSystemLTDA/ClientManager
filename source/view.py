import flet as ft

class View(ft.View):
    page = None
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.drawer = self.page.drawer
        self.text = ft.Text(
            'Aperte F11 para entrar na tela cheia',
            size=12,
            top=0,
            right=0
        )
        self.controls = [ft.Container(
            image_src='img/background.png',
            image_fit=ft.ImageFit.COVER,
            expand=True,
            content=ft.Stack(
                controls=[
                    self.generate_main_content(),
                    self.text
                ]
            )
        )]

    def on_pre_view(self):
        pass

    def generate_main_content(self):
        return ft.Text('Generate main content')
