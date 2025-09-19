from google.adk.agents import Agent

class ThumbsAgent(Agent):
    name: str = "thumbs_agent"
    description: str = "Gives thumbs up/down/neutral based on sentiment."

    async def run(self, context: dict) -> dict:
        sentiment = context.data.get("sentiment")

        if not sentiment:
            return {"error": "No sentiment found."}

        sentiment = sentiment.strip().lower()

        if sentiment == "positive":
            result = "up"
        elif sentiment == "negative":
            result = "down"
        elif sentiment == "neutral":
            result = "neutral"
        else:
            return {"error": f"Unexpected sentiment value: {sentiment}"}

        return {"thumbs": result}

thumbs_agent = ThumbsAgent()
