import datetime

import flet as ft

from .clients_page import ClientsPage
from .components import Message, View, NavigationDrawer
from .login_page import LoginPage
from .register_page import RegisterPage
from .update_page import UpdatePage

def main(page: ft.Page):
    page.title = "DevSystem"
    page.padding = 1
    page.fonts = {
        "Garet-Heavy": "fonts/Garet-Heavy.ttf",
        "Garet": "fonts/Garet-Book.ttf",
    }
    page.snack_bar = Message(page)
    page.drawer = NavigationDrawer()
    View.page = page

    views = {
        '/register': RegisterPage(route='/register'),
        '/clients': ClientsPage(route='/clients'),
        '/login': LoginPage(route='/login'),
        '/update': UpdatePage(route='/update')
    }

    def on_route_change(e):
        view = views[page.route]
        page.views[-1] = view
        view.page = page
        view.on_pre_view()

    starter_page = '/login'

    logged_date = page.client_storage.get('logged')
    if logged_date and logged_date == f"{datetime.datetime.today():%d/%m}":
        starter_page = '/clients'

    page.on_route_change = on_route_change
    page.views.append(views[starter_page])
    page.go(starter_page)