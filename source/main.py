import datetime

import flet as ft

from .clients_page import ClientsPage
from .components import Message, NavigationDrawer
from .login_page import LoginPage
from .register_page import RegisterPage
from .update_page import UpdatePage
from .view import View

def main(page: ft.Page):
    page.window_center()
    page.title = "DevSystem"
    page.padding = 0
    page.spacing = 0
    page.fonts = {
        "Garet-Heavy": "fonts/Garet-Heavy.ttf",
        "Garet": "fonts/Garet-Book.ttf",
    }
    page.snack_bar = Message(page)
    page.drawer = NavigationDrawer()

    def on_keyboard_event(e):
        if e.key == 'F11':
            page.window_full_screen = not page.window_full_screen
            page.update()
        elif e.key == 'F1':
            if e.page.drawer.open:
                e.page.close_drawer()
            else:
                e.page.show_drawer(e.page.drawer)
            page.update()

    page.on_keyboard_event = on_keyboard_event

    View.page = page

    page.views.extend([
        RegisterPage(route='/register'),
        ClientsPage(route='/clients'),
        LoginPage(route='/login'),
        UpdatePage(route='/update'),
    ])

    def on_route_change(_):
        page.views.sort(key=lambda view: view.route == page.route)
        page.views[-1].page = page
        page.views[-1].on_pre_view()
        page.update()

    initial_route = '/login'

    logged_date = page.client_storage.get('logged')
    if logged_date and logged_date == f"{datetime.datetime.today():%d/%m}":
        initial_route = '/clients'

    page.on_route_change = on_route_change
    page.views.sort(key=lambda view: view.route == initial_route)
    page.go(initial_route)
