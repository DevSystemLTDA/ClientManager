import flet as ft
import pytest

from source.components import NavigationDrawer
from source.control import Control
from source.register_page import RegisterPage

@pytest.fixture
def control_obj():
    return Control()

@pytest.fixture
def register_page():
    return RegisterPage()

