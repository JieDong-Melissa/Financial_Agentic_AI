from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

from dotenv import load_dotenv
load_dotenv()


# web search agent
web_search_agent=Agent(
    name = "Web Search Agent",
    role = "search the web for the information",
    model = Groq(id="llama-3.3-70b-versatile"),
    tools = [DuckDuckGo()],
    instructions = ["Always include sources"],
    show_tool_calls = True,
    markdown = True,
    debug_mode = True
)

# Financial agent
finance_agent=Agent(
    name = "Finance AI Agent",
    model = Groq(id="llama-3.3-70b-versatile"),
    tools = [YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
    instructions = ["Use tables to display data"],
    show_tool_calls = True,
    markdown = True,
    debug_mode = True
)

multi_ai_agent=Agent(
    model = Groq(id="llama-3.3-70b-versatile"),
    team = [web_search_agent, finance_agent],
    instructions = ["Always include sources", "Use tables to display data"],
    show_tool_calls = True,
    markdown = True,
    debug_mode = True
)

# query
multi_ai_agent.print_response("Summarize stock analyst recommendation and share the latest news for NVDA", stream=True)