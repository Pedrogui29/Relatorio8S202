class FutebolDatabase:
    def __init__(self, database):
        self.db = database

    def create_player(self, name, pontuacao):
        query = "CREATE (:Player {name: $name, pontuacao: $pontuacao})"
        parameters = {"name": name , "pontuacao": pontuacao}
        self.db.execute_query(query, parameters)

    def create_match(self, name):
        query = "CREATE (:Match {name: $name})"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)


    def get_player(self):
        query = "MATCH (p:Player) RETURN p.name AS name, p.pontuacao AS pontuacao"
        results = self.db.execute_query(query)
        return [(result["name"], result["pontuacao"]) for result in results]


    def get_match(self):
        query = "MATCH (m:Match) RETURN m.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    def insert_player_match(self, player_name, match_name):
        query = "MATCH (p:Player {name: $player_name}) MATCH (m:Match {name: $match_name}) CREATE (p)-[:JOGA{pontuacao: p.pontuacao}]->(m)"
        parameters = {"player_name": player_name, "match_name": match_name}
        self.db.execute_query(query, parameters)

    def get_players_scores_per_match(self):
        query = "MATCH (p:Player)-[j:JOGA]->(m:Match) RETURN p.name AS player_name, m.name AS match_name, j.pontuacao AS score"
        results = self.db.execute_query(query)
        player_scores = {}
        for result in results:
            player_name = result["player_name"]
            match_name = result["match_name"]
            score = result["score"]
            if player_name in player_scores:
                player_scores[player_name].append((match_name, score))
            else:
                player_scores[player_name] = [(match_name, score)]
        return player_scores

    def update_player(self, old_name, new_name):
        query = "MATCH (p:Player {name: $old_name}) SET p.name = $new_name"
        parameters = {"old_name": old_name, "new_name": new_name}
        self.db.execute_query(query, parameters)


    def delete_player(self, name):
        query = "MATCH (p:Professor {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

