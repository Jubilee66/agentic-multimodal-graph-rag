def planner_agent(query):
    
    query = query.lower()

    if any(
        word in query
        for word in [
            "relationship",
            "connected",
            "link",
            "between",
            "graph"
        ]
    ):
        return "GRAPH"

    elif any(
        word in query
        for word in [
            "show",
            "image",
            "diagram",
            "picture"
        ]
    ):
        return "IMAGE"

    return "TEXT"