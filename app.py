import flet as ft

from source import main, Control

if __name__ == '__main__':
    try:
        ft.app(main, assets_dir="assets")
    except Exception as e:
        Control.log(e)
