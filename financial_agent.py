from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

from dotenv import load_dotenv
load_dotenv()

websearch_agent = Agent(
    name='WebSearchAgent',
    role="Searches the web for information.",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions="""You are a helpful assistant that searches the web for information. 
    Use the DuckDuckGo tool to find relevant information based on the user's query. 
    Provide concise and accurate answers based on the search results.""",
    show_tool_calls=True,
    markdown=True,
)

financial_agent = Agent(
    name='FinancialAgent',
    role="Provides financial information and analysis.",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[
        YFinanceTools(
            stock_price=True,
            historical_prices=True,
            analyst_recommendations=True,
            stock_fundamentals=True,
            company_info=True,
        )
    ],
    instructions="""Use tables to display the data. You are a financial assistant that provides 
    information and analysis on stocks, market trends, and financial news. Use the YFinanceTools 
    to retrieve stock data and financial information. Provide concise and accurate answers.""",
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent = Agent(
    name='MultiAIAgent',
    role='Coordinator of multiple specialized agents.',
    model=Groq(id="llama-3.3-70b-versatile"),
    team=[websearch_agent, financial_agent],
    instructions="""You are a multi-agent system with a WebSearchAgent and a FinancialAgent. 
    Determine which agent is best suited to handle the query and delegate accordingly. 
    Provide concise and accurate answers based on the information retrieved.""",
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent.print_response(
    "Summarize analyst recommendations and share the latest news on Cisco Systems Inc",
    stream=True
)