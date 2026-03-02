# 💹 AI Financial Advisor Agent

A multi-agent AI system built with **Phidata**, **Groq (LLaMA 3.3)**, and **YFinance** that acts as a smart financial advisor — fetching real-time stock data, analyst recommendations, and the latest market news.

---

## 🚀 Features

- 📈 Real-time stock prices, fundamentals & analyst recommendations
- 🌐 Latest financial news via DuckDuckGo search
- 🤖 Multi-agent system with a coordinator agent
- 🖥️ Interactive Phidata Playground UI

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| [Phidata](https://phidata.app) | Agent framework & Playground UI |
| [Groq](https://groq.com) | LLaMA 3.3 70B inference |
| [YFinance](https://pypi.org/project/yfinance/) | Stock market data |
| [DuckDuckGo](https://pypi.org/project/duckduckgo-search/) | Web search |

---

## ⚙️ Setup

**1. Clone the repo**
```bash
git clone https://github.com/your-username/ai-financial-advisor.git
cd ai-financial-advisor
```

**2. Install dependencies**
```bash
pip install phidata groq yfinance duckduckgo-search python-dotenv
```

**3. Add your API keys in a `.env` file**
```
GROQ_API_KEY=your_groq_api_key
PHI_API_KEY=your_phidata_api_key
```

**4. Run the agent**
```bash
# Terminal chat
python financial_agent.py

# Playground UI
python playground.py
```

Then open [phidata.app/playground](https://phidata.app/playground) and set the endpoint to `http://localhost:7777`.

---

## 💬 Example Queries

- *"Analyze Apple stock and should I buy it?"*
- *"Summarize analyst recommendations for Cisco Systems"*
- *"What's the latest news on Tesla?"*

---

## ⚠️ Disclaimer

This tool is for **informational purposes only** and does not constitute official financial advice.
