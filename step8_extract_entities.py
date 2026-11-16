import json
import spacy

from step2_chunk_documents2 import all_chunks

nlp = spacy.load("en_core_web_sm")

triples = []

for chunk in all_chunks:

    doc = nlp(chunk["content"])

    entities = [ent.text.strip() for ent in doc.ents]

    if len(entities) < 2:
        continue

    for i in range(len(entities) - 1):

        triples.append({
            "source": entities[i],
            "relationship": "RELATED_TO",
            "target": entities[i + 1]
        })

with open(
    "graph_db/triples.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        triples,
        f,
        indent=4
    )

print(f"\nGenerated {len(triples)} triples")