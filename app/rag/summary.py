from app.rag.embed import search


def generate_summary(query: str):
    logs = search(query)

    if not logs:
        return "No patrol intelligence available."

    summary = "Patrol Intelligence Summary:\n"
    for log in logs:
        summary += f"- {log}\n"

    summary += "\nRecommendation: Increase monitoring in frequently crowded areas."

    return summary
