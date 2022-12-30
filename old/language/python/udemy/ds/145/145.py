from neo4j import GraphDatabase

driver = GraphDatabase.driver(
    "bolt://localhost:7687", auth=('neo4j', 'password')
)

def clear_db(tx):
    tx.run('match (n) detach delete n')

with driver.session() as session:
    session.write_transaction(clear_db)