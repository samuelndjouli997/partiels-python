import json


class Report:
    def __init__(self):
        self.players = []
        self.tournaments = []
        self.load_players()
        self.load_tournaments()

    def load_players(self):
        try:
            with open('data/players.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Le fichier des joueurs n'existe pas.")
        except json.JSONDecodeError:
            print("Erreur lors de la lecture du fichier JSON.")
        return []

    def load_tournaments(self):
        try:
            with open('data/tournaments.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Le fichier des tournois n'existe pas.")
        except json.JSONDecodeError:
            print("Erreur lors de la lecture du fichier JSON.")
        return []
