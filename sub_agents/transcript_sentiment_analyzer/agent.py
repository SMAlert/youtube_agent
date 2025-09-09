from google.adk.agents import Agent
from google.genai.types import GenerateContentConfig
from sub_agents.transcript_sentiment_analyzer import prompt

sentiment_analyzer_agent = Agent(
    model="gemini-2.5-flash",
    name="sentiment_analyzer_agent",
    description="Analyze sentiment of the given transcript text",
    instruction=prompt.ANALYZE_SENTIMENT_INSTR,
    generate_content_config=GenerateContentConfig(
        temperature=0.0,
        top_p=0.5,
    )
)
