from Views.Menu import Menu
from io import StringIO


def test_main_menu(monkeypatch):
    menu = Menu()
    monkeypatch.setattr('sys.stdin', StringIO('2\n'))

    assert menu.main_menu() == '2'


def test_report_menu(monkeypatch):
    menu = Menu()
    monkeypatch.setattr('sys.stdin', StringIO('3\n'))

    assert menu.report_menu() == '3'
