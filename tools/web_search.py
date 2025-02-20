from langchain_community.tools import Tool
from langchain_community.utilities import GoogleSerperAPIWrapper

def setup_search_tool():
    search = GoogleSerperAPIWrapper()
    return Tool(
        name="Web Search",
        func=search.run,
        description="Useful for searching current events or factual information"
    )
