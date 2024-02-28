from Views.MatchView import MatchView
from io import StringIO


def test_get_user_choice(monkeypatch):
    match_view = MatchView()
    monkeypatch.setattr('sys.stdin', StringIO('2\n'))

    assert match_view.get_user_choice() == 2
