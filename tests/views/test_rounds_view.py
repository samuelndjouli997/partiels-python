from Views.PlayerView import PlayerView
from io import StringIO


def test_get_player_info(monkeypatch):
    player_view = PlayerView()
    monkeypatch.setattr('sys.stdin', StringIO('John\nDoe\n01/01/1990\nAB12345\n'))

    result = player_view.get_player_info()

    assert result == ('John', 'Doe', '01/01/1990', 'AB12345')


def test_select_player(monkeypatch):
    player_view = PlayerView()
    players = [
        {'first_name': 'John', 'last_name': 'Doe',
         'birth_date': '01/01/1990', 'national_chess_id': 'AB12345'},
        {'first_name': 'Jane', 'last_name': 'Smith',
         'birth_date': '02/02/1991', 'national_chess_id': 'CD67890'}
    ]
    monkeypatch.setattr('sys.stdin', StringIO('1\n'))

    result = player_view.select_player(players)

    assert result == 1
