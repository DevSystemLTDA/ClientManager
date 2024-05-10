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
            content=self.generate_main_content()
        )]

    def generate_main_content(self):
        return ft.Text('Generate main content')

    def on_pre_view(self):
        pass