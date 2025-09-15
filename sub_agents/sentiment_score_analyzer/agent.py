from google.adk.agents import Agent, AgentContext, register_agent
import random

@register_agent("sentiment_score_analyzer")
class SentimentScoreAnalyzer(Agent):

    async def run(self, context: AgentContext) -> dict:
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
