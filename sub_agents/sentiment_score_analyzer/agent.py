from google.adk.agents import Agent, AgentContext, register_agent
import random

@register_agent("sentiment_score_analyzer")
class SentimentScoreAnalyzer(Agent):

    async def run(self, context: AgentContext) -> dict:
        sentiment = context.data.get("sentiment")

        if not sentiment:
            return {"error": "No sentiment found."}

        if sentiment.lower() == "positive":
            score = random.randint(1, 4)
        elif sentiment.lower() == "neutral":
            score = 5
        else:
            score = random.randint(6, 10)

        return {"score": score}
