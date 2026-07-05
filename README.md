# 💰 AI Personal Finance Coach

An AI-powered Personal Finance Coach built using **Python**, **OpenRouter LLM**, **Streamlit**, and **Tool Calling**. The application helps users manage their finances through natural language conversations by analyzing budgets, planning savings goals, evaluating financial risks, generating financial summaries, and answering finance-related questions using specialized AI agents.

---

# 📌 Project Overview

The AI Personal Finance Coach is an intelligent conversational assistant that provides personalized financial guidance using a multi-agent architecture. Instead of relying on hardcoded calculations, the system uses Large Language Models (LLMs) together with Python tools to perform financial analysis, budgeting, savings planning, risk evaluation, and financial education.

The application automatically routes user queries to specialized AI agents that invoke the required financial tools, perform calculations, and present results through an interactive Streamlit chat interface.

This project demonstrates the practical implementation of **Agentic AI**, where multiple specialized AI agents collaborate with external tools to solve real-world personal finance problems.

---

# 🎯 Objectives

- Build an AI-powered personal finance assistant.
- Demonstrate Agentic AI using multiple specialized agents.
- Implement OpenRouter Tool Calling.
- Perform financial calculations using Python tools.
- Provide personalized financial recommendations.
- Generate financial summaries.
- Visualize financial insights using charts.
- Build an interactive Streamlit chatbot.

---

# 🚀 Features

- 💬 ChatGPT-style conversational interface
- 🤖 Multi-Agent architecture
- 💰 Budget analysis
- 🎯 Goal planning
- ⚠ Financial risk assessment
- 📊 Automatic chart generation
- 📄 Financial summary generation
- 📚 Financial knowledge assistant
- 🧠 Conversation memory
- 🛠 Automatic tool calling
- 🎨 Modern Streamlit UI
- 🔐 Secure API key management using `.env`

---

# 🛠️ Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend Development |
| Streamlit | Web Interface |
| OpenRouter | Large Language Model |
| Gemini | AI Model |
| Plotly | Data Visualization |
| Requests | API Communication |
| JSON | Memory Storage |
| python-dotenv | Environment Variables |

---

# 📂 Project Structure

```text
Personal_Finance_Coach/

│
├── agents/
│   ├── budget_agent.py
│   ├── goal_agent.py
│   ├── risk_agent.py
│   ├── report_agent.py
│   └── knowledge_agent.py
│
├── services/
│   ├── openrouter.py
│   ├── router.py
│   ├── tool_executor.py
│   └── memory.py
│
├── tools/
│   ├── budget_tools.py
│   ├── goal_tools.py
│   ├── risk_tools.py
│   └── report_tools.py
│
├── assets/
│   └── style.css
│
├── memory.json
├── app.py
├── main.py
├── requirements.txt
└── README.md
```

---

# 📦 Required Libraries

```bash
streamlit
plotly
requests
python-dotenv
```
---

# 🔑 Environment Variable

Create a `.env` file.

```text
OPENROUTER_API_KEY=YOUR_OPENROUTER_API_KEY
```

---

# 🤖 Multi-Agent Workflow

```text
                 User
                   │
                   ▼
          Streamlit Chat Interface
                   │
                   ▼
             Router Service
                   │
 ┌─────────────────┼──────────────────┐
 │                 │                  │
 ▼                 ▼                  ▼
Budget Agent   Goal Agent      Risk Agent
 │                 │                  │
 └──────────────┬──┴───────────────┬──┘
                ▼                  ▼
        Report Agent      Knowledge Agent
                │
                ▼
          OpenRouter LLM
                │
                ▼
         Tool Executor
                │
                ▼
      Python Financial Tools
                │
                ▼
       Final AI Response
```

---

# 🔄 Agent Execution Flow

1. User enters a financial query.
2. The Router identifies the appropriate AI agent.
3. The selected agent sends the request to OpenRouter.
4. The LLM determines whether tool execution is required.
5. Required financial tools are automatically executed.
6. Tool results are returned to the LLM.
7. The assistant generates a natural language response.
8. Charts are generated automatically whenever financial data is detected.
9. Conversation history is stored in memory.

---

# 🤖 AI Agents

## 💰 Budget Agent

Responsible for

- Budget analysis
- Expense calculation
- Savings calculation
- Saving rate calculation
- Budget recommendations

---

## 🎯 Goal Agent

Responsible for

- Goal feasibility
- Monthly savings calculation
- Goal completion estimation
- Goal progress
- Future savings prediction

---

## ⚠ Risk Agent

Responsible for

- Spending risk
- Savings risk
- Debt risk
- Emergency fund analysis
- Financial health score

---

## 📄 Report Agent

Responsible for

- Financial summary
- Monthly report
- Financial recommendations
- Health score generation

---

## 📚 Knowledge Agent

Responsible for

- Financial education
- Investment concepts
- Banking concepts
- Mutual funds
- SIP
- Taxes
- Loans

---

# 🧰 Financial Tools

The system automatically invokes Python tools such as

- calculate_budget()
- analyze_budget()
- expense_breakdown()
- calculate_monthly_savings()
- estimate_goal_completion()
- goal_progress()
- spending_risk()
- debt_risk()
- financial_summary()
- monthly_report()
- generate_recommendations()

---

# 📊 Automatic Visualizations

Whenever financial information is detected, the application automatically displays

- 📊 Income vs Expense Bar Chart
- 🥧 Savings Distribution Pie Chart
- 📈 Financial Health Progress Bar

Charts appear directly below the related chat response.

---

# 🧠 Memory Management

Conversation history is stored in

```text
memory.json
```

The memory module

- Loads previous conversations
- Saves new interactions
- Maintains conversational context
- Improves follow-up responses

---

# 📊 System Architecture

```text
                    User
                      │
                      ▼
            Streamlit Interface
                      │
                      ▼
                 Router Service
                      │
                      ▼
              Specialized Agents
                      │
                      ▼
               OpenRouter API
                      │
                 Tool Calling
                      │
                      ▼
             Financial Tools
                      │
                      ▼
             Financial Analysis
                      │
                      ▼
          Charts & AI Response
```

---

# 📁 File Description

## app.py

Responsible for

- Streamlit Interface
- Chat Interface
- Chart Generation
- Financial Dashboard

---

## main.py

Responsible for

- User Request Processing
- Memory Management
- Final Response Generation

---

## router.py

Responsible for

- Query Classification
- Agent Routing

---

## tool_executor.py

Responsible for

- Executing Python Financial Tools
- Formatting Tool Responses

---

## report_tools.py

Responsible for

- Financial Summary
- Financial Health Score
- Monthly Report
- Recommendations

---

# 📈 Advantages

- ChatGPT-like experience
- Agentic AI architecture
- Modular codebase
- Easy to extend
- Interactive charts
- Financial education
- Personalized recommendations
- Conversation memory
- Automatic tool calling
- Beginner-friendly interface

---

# 🔮 Future Enhancements

- User authentication
- Database integration
- Expense categorization
- CSV and Excel import
- Voice assistant
- Investment portfolio analysis
- EMI calculator
- Real-time stock market integration
- Mobile application
- Cloud deployment
- Personalized financial advisor

---

# 📸 Sample Conversation

### User

```text
My monthly income is ₹70,000 and expenses are ₹42,000.
```

### Assistant

```text
Your monthly savings are ₹28,000 with a saving rate of 40%.

Financial Health: Excellent

Recommendations:
• Continue your current savings habit.
• Consider investing in SIPs.
• Maintain an emergency fund.
```

---

### User

```text
Can I buy a laptop worth ₹1,20,000 by saving ₹15,000 per month?
```

### Assistant

```text
Yes.

You can achieve your goal in approximately 8 months.

Monthly Saving Required: ₹15,000
Goal Status: Achievable
```

---

# 👨‍💻 Author

Developed as a hands-on **Agentic AI** project using **Python**, **OpenRouter**, **Streamlit**, **Plotly**, and **Tool Calling** to demonstrate multi-agent collaboration, financial analytics, conversation memory, and intelligent personal finance assistance.
