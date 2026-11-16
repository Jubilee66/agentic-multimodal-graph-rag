from tools.graph_search_tool import graph_search

while True:

    query = input("\nEnter Entity: ")

    if query.lower() == "exit":
        break

    results = graph_search(query)

    if not results:
        print("\nNo relationships found.")
        continue

    print("\nRelationships Found:\n")

    for r in results:

        print(
            f"{r['source']} "
            f"--[{r['relation']}]--> "
            f"{r['target']}"
        )