# sub_agents/youtube_transcriber/agent.py
from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from google.genai.types import GenerateContentConfig

from sub_agents.youtube_transcriber import prompt

transcribe_video = Agent(
    model="gemini-2.5-flash",
    name="transcribe_video",
    description="Transcribes the spoken content from a YouTube video given its URL.",
    instruction=prompt.CONFIRM_TRANSCRIPTION_INSTR,
)

transcribe_agent = Agent(
    model="gemini-2.5-flash",
    name="transcribe_agent",
    description="Given a YouTube URL, extract and return the transcript of the video.",
    instruction=prompt.TRANSCRIBE_AGENT_INSTR,
    tools=[AgentTool(agent=transcribe_video)],
    generate_content_config=GenerateContentConfig(
        temperature=0.0,
        top_p=0.5,
    ),
)
