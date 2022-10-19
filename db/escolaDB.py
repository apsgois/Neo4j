from db.database import Graph


class EscolaDB():
    def __init__(self):
        self.db = Graph(uri='bolt://3.93.36.199:7687',
                        user='neo4j', password='finishes-piers-alerts')

    def create_professor(self, professor):
        return self.db.execute_query('CREATE (n:Professor {nome:$nome, idade:$idade, area:$area}) return n',
                                     {'nome': professor['nome'], 'idade': professor['idade'],
                                      'area': professor['area']})

    def create_materia(self, materia):
        return self.db.execute_query('CREATE (n:Materia {assunto:$assunto, horario:$horario}) return n',
                                     {'assunto': materia['assunto'], 'horario': materia['horario']})

    def read_by_professor(self, professor):
        return self.db.execute_query('MATCH (n:Professor {nome:$nome}) RETURN n',
                                     {'nome': professor['nome']})

    def read_all_nodes(self):
        return self.db.execute_query('MATCH (n) RETURN n')

    def create_relation(self, professor1, materia1, ano):
        return self.db.execute_query(
            'MATCH (n:Professor {nome:$nome}), (m:Materia {assunto:$assunto}) CREATE (n)-[r:DA_AULA{ano: $ano}]->(m) RETURN n, r, m',
            {'nome': professor1['nome'], 'assunto': materia1['assunto'], 'ano': ano})
