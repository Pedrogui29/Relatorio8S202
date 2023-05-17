from Database import Database
from FutebolDatabase import FutebolDatabase

db = Database("bolt://44.203.120.80:7687", "neo4j", "farads-poisons-canyon")
db.drop_all()


players_database = FutebolDatabase(db)

players_database.create_player("Rodrigo",25)
players_database.create_player("Matheus", 40)
players_database.create_player("Leo", 2)
players_database.create_player("Luiz", 10)

players_database.create_match("Futebol")
players_database.create_match("Basquete")
players_database.create_match("Volei")


players_database.insert_player_match("Rodrigo", "Basquete")
players_database.insert_player_match("Matheus", "Volei")
players_database.insert_player_match("Leo", "Futebol")


players_database.update_player("Rodrigo", "Jose")

players_database.delete_player("Luiz")

print("Lista de Jogadores:")
print(players_database.get_player())
print("Lista de Partidas:")
print(players_database.get_match())

print("")

player_scores = players_database.get_players_scores_per_match()
for player_name, scores in player_scores.items():
    print("Jogador:", player_name)
    for match_name, score in scores:
        print("Partida:", match_name, "- Pontuação:", score)
        print("")


db.close()