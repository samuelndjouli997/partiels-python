from Models.Match import Match


def test_match_serialization():
    # Création d'un match
    player1 = {'first_name': 'John', 'last_name': 'Doe'}
    player2 = {'first_name': 'Jane', 'last_name': 'Smith'}
    match = Match(player1, player2)

    # Sérialisation du match
    serialized_match = match.serialize()

    # Vérification du contenu du dictionnaire sérialisé
    assert serialized_match == {
        'player1': {'first_name': 'John', 'last_name': 'Doe'},
        'player2': {'first_name': 'Jane', 'last_name': 'Smith'},
        'winner': None
    }


def test_match_string_representation():
    # Création d'un match
    player1 = {'first_name': 'John', 'last_name': 'Doe'}
    player2 = {'first_name': 'Jane', 'last_name': 'Smith'}
    match = Match(player1, player2)

    # Récupération de la représentation en chaîne du match
    match_str = str(match)

    # Vérification de la représentation en chaîne
    assert match_str == "John Doe VS Jane Smith"
