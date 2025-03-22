from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime


def save_to_txt(data: str, filename: str = "research_output.txt") -> str:
    """
    Saves the provided research data to a text file with a timestamp.

    Args:
        data (str): The research output to save.
        filename (str, optional): Name of the file to save the output. Defaults to "research_output.txt".

    Returns:
        str: Confirmation message indicating successful file save.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    # Append data to the specified text file
    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)

    return f"Data successfully saved to {filename}"


# Tool for saving research output to a file
save_tool = Tool(
    name='save',
    func=save_to_txt,
    description="Save the output of a research query to a text file."
)

# Initialize DuckDuckGo search for web-based queries
search = DuckDuckGoSearchRun()

# Tool for performing web searches using DuckDuckGo
search_tool = Tool(
    name='search',
    func=search.run,
    description="Search the web for information on a topic."
)

# Configure Wikipedia API Wrapper to return only 1 result with a max character limit
api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)

# Wikipedia tool for querying Wikipedia
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)
