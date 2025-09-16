from google.adk.agents import Agent
import random

class SentimentScoreAnalyzer(Agent):
    name: str = "sentiment_score_analyzer"
    description: str = "Analyzes sentiment score"

    async def run(self, context: dict) -> dict:
        sentiment = context.data.get("sentiment")

        if not sentiment:
            return {"error": "No sentiment found."}

        sentiment = sentiment.strip().lower()

        if sentiment == "positive":
            score = random.randint(7, 10)
        elif sentiment == "neutral":
            score = random.randint(4, 6)
        elif sentiment == "negative":
            score = random.randint(1, 3)
        else:
            return {"error": f"Unexpected sentiment value: {sentiment}"}

        return {"score": score}