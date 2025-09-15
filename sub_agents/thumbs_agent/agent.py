from google.adk.agents import Agent, AgentContext, register_agent

@register_agent("thumbs_agent")
class ThumbsAgent(Agent):

    async def run(self, context: AgentContext) -> dict:
        sentiment = context.data.get("sentiment")

        if not sentiment:
            return {"error": "No sentiment found."}

        sentiment = sentiment.strip().lower()

        if sentiment == "positive":
            result = "Thumbs Up"
        elif sentiment == "negative":
            result = "Thumbs Down"
        elif sentiment == "neutral":
            result = "Neutral"
        else:
            return {"error": f"Unexpected sentiment value: {sentiment}"}

        return {"thumbs": result}
