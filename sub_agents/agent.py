from google.adk.agents import Agent
from . import prompt

from sub_agents.youtube_transcriber.agent import transcribe_agent
from sub_agents.transcript_sentiment_analyzer.agent import sentiment_analyzer_agent
from sub_agents.sentiment_score_analyzer.agent import sentiment_score_agent
from sub_agents.thumbs_agent.agent import thumbs_agent

root_agent = Agent(
    model="gemini-2.5-flash",
    name="root_agent",
    description="A YouTube agent orchestrating multiple sub-agents.",
    instruction=prompt.ROOT_AGENT_INSTR,
    sub_agents=[
        transcribe_agent,
        sentiment_analyzer_agent,
        sentiment_score_agent,
        thumbs_agent,
    ],
)
