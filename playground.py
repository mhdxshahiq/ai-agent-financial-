from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.playground import Playground, serve_playground_app

from dotenv import load_dotenv
load_dotenv()

websearch_agent = Agent(
    name='WebSearchAgent',
    agent_id='websearch-agent',
    role="Searches the web for latest financial news and market updates.",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=[
        "You are a financial news researcher.",
        "Always search for the latest news, press releases, and market updates.",
        "Focus on financial topics: earnings, mergers, market trends, economic data.",
        "Return summarized, well-structured news with source references.",
        "Always search before answering — never rely on memory for current events.",
    ],
    show_tool_calls=True,
    markdown=True,
)

financial_agent = Agent(
    name='FinancialAgent',
    agent_id='financial-agent',
    role="Expert financial analyst providing stock analysis and investment insights.",
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
    instructions=[
        "You are an expert financial advisor and stock analyst.",
        "Always fetch real data using YFinanceTools before answering.",
        "Display stock prices, fundamentals, and recommendations in markdown tables.",
        "Provide buy/hold/sell analysis based on analyst recommendations and fundamentals.",
        "Include key metrics: P/E ratio, EPS, revenue, market cap, 52-week high/low.",
        "Give clear, actionable investment insights with supporting data.",
        "Always mention that this is for informational purposes and not official financial advice.",
    ],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent = Agent(
    name='MultiAIAgent',
    agent_id='multi-ai-agent',
    role='Senior Financial Advisor combining market data and latest news.',
    model=Groq(id="llama-3.3-70b-versatile"),
    team=[websearch_agent, financial_agent],
    instructions=[
        "You are a senior financial advisor with access to real-time data and news.",
        "For ANY stock or company query: ALWAYS use BOTH agents together.",
        "Use FinancialAgent to fetch: stock price, fundamentals, analyst recommendations.",
        "Use WebSearchAgent to fetch: latest news, earnings reports, market sentiment.",
        "Combine both data sources into a comprehensive financial report.",
        "Structure your response with sections: Overview, Key Metrics, Analyst Ratings, Latest News, Verdict.",
        "Give a clear investment verdict: Bullish / Bearish / Neutral with reasoning.",
        "Always remind the user this is informational, not official financial advice.",
    ],
    show_tool_calls=True,
    markdown=True,
)

app = Playground(agents=[websearch_agent, financial_agent, multi_ai_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", host="0.0.0.0", port=7777, reload=True)