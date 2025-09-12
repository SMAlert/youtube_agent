from google.adk.agents import Agent, AgentContext, register_agent

@register_agent("thumbs_agent")
class ThumbsAgent(Agent):

    async def run(self, context: AgentContext) -> dict:
        sentiment = context.data.get("sentiment")

        if not sentiment:
            return {"error": "No sentiment found."}

        sentiment = sentiment.lower()

        if sentiment == "positive":
            result = "Thumbs Up"
        elif sentiment == "negative":
            result = "Thumbs Down"
        else:
            result = "Neutral"

        return {"thumbs": result}
