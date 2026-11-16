from neo4j import GraphDatabase

driver = GraphDatabase.driver(
    "bolt://localhost:7687",
    auth=("neo4j", "User@1234")
)

def graph_search(entity):

    query = """
    MATCH (n)-[r]-(m)
    WHERE toLower(n.name) = toLower($entity)

    RETURN
        n.name AS source,
        type(r) AS relation,
        m.name AS target

    LIMIT 20
    """

    results = []

    with driver.session() as session:

        records = session.run(
            query,
            entity=entity
        )

        for r in records:

            results.append(
                {
                    "source": r["source"],
                    "relation": r["relation"],
                    "target": r["target"]
                }
            )

    return results