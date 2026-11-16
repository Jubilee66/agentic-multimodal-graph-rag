import json
from neo4j import GraphDatabase

driver = GraphDatabase.driver(
    "bolt://localhost:7687",
    auth=("neo4j", "User@1234")
)

with open("graph_db/triples.json", "r") as f:
    triples = json.load(f)


def create_graph(tx, source, rel, target):

    query = f"""
    MERGE (a:Entity {{name:$source}})
    MERGE (b:Entity {{name:$target}})
    MERGE (a)-[:{rel.upper()}]->(b)
    """

    tx.run(
        query,
        source=source,
        target=target
    )


with driver.session() as session:

    for t in triples:

        session.execute_write(
            create_graph,
            t["source"],
            t["relationship"],
            t["target"]
        )

print("Graph created")