from agent.planner_agent import planner_agent

from tools.vector_search_tool import search_documents
from tools.image_search_tool import search_images
from tools.graph_search_tool import graph_search


def run_agent(query, api_key=None):

    plan = planner_agent(query)

    answer = ""
    images = []

    if plan == "TEXT":

        text_results = search_documents(query)

        answer = "\n\n".join([
            f"SOURCE: {doc['source']}\n\n{doc['content'][:1000]}"
            for doc in text_results
        ])

    elif plan == "IMAGE":

        images = search_images(query)

        answer = "Retrieved image evidence."

    elif plan == "GRAPH":

        graph_results = graph_search(query)

        if graph_results:

            answer = "\n".join(
                [
                    f"{r['source']} -> {r['relation']} -> {r['target']}"
                    for r in graph_results
                ]
            )

        else:

            answer = "No graph relationships found."

    return {
        "answer": answer,
        "images": images
    }