from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from typing import List
import langchain_together as lt
from tools import search_tool, wiki_tool, save_tool

# Load environment variables from a .env file
load_dotenv()


class AnswerResponse(BaseModel):
    """
    Defines the structured response format for the AI agent.

    Attributes:
        topic (str): The main topic of the response.
        summary (str): A brief summary of the topic.
        sources (List[str]): A list of sources used for the response.
        tools_used (List[str]): A list of tools used to generate the response.
    """
    topic: str
    summary: str
    sources: List[str]
    tools_used: List[str]


# Initialize the LLM model (TinyLlama variant)
llm = lt.ChatTogether(model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free")

# Set up the JSON output parser using Pydantic
parser = PydanticOutputParser(pydantic_object=AnswerResponse)

# Define the chat prompt template for the AI assistant
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistant that will generate structured research responses.
            Answer the user's query and use necessary tools.

            Your response MUST be valid JSON. Do NOT include any extra text, explanations, or function wrappers.
            
            Output Format:
            {format_instructions}
            """,
        ),
        ("placeholder", "{chat_history}"),  # Stores previous conversation context
        ("human", "{query}"),  # The user's question
        ("placeholder", "{agent_scratchpad}"),  # Keeps track of tool execution steps
    ]
).partial(format_instructions=parser.get_format_instructions())

# Define available tools for the agent
tools = [wiki_tool, search_tool, save_tool]

# Create the agent with the given tools and prompt
agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools
)

# Set up the agent executor to process user queries
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Invoke the agent to answer a research question and save results
raw_response = agent_executor.invoke(
    {'query': "What are the top 10 best-rated Family Guy episodes? Save only the final output to a text file."}
)

# Process the response safely
try:
    structured_response = parser.parse(raw_response.get("output"))
    print(structured_response.summary)
except Exception as e:
    print("Error parsing response", e, "Raw Response - ", raw_response)
