import streamlit as st
import plotly.graph_objects as go
import re

from main import chat
from memory import clear_memory

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="AI Personal Finance Coach",
    page_icon="💰",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

.block-container{
    max-width:900px;
    padding-top:2rem;
    padding-bottom:2rem;
}

.stChatMessage{
    border-radius:16px;
    padding:16px;
}

.stButton>button{
    width:100%;
    border-radius:10px;
    height:42px;
    font-weight:600;
}

.report-card{
    background:#f8fafc;
    border-left:5px solid #0ea5e9;
    padding:18px;
    border-radius:12px;
    margin-top:10px;
}

.metric-card{
    background:#f8fafc;
    padding:15px;
    border-radius:10px;
    border:1px solid #e2e8f0;
}

.footer{
    text-align:center;
    color:gray;
    font-size:14px;
    margin-top:40px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# SESSION STATE
# ==========================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "income" not in st.session_state:
    st.session_state.income = 0

if "expenses" not in st.session_state:
    st.session_state.expenses = 0

if "savings" not in st.session_state:
    st.session_state.savings = 0

if "saving_rate" not in st.session_state:
    st.session_state.saving_rate = 0

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.title("💰 Finance Coach")

    st.caption(
        "Your AI-powered Personal Finance Assistant"
    )

    st.divider()

    st.subheader("🚀 Features")

    st.success("💬 Chat Assistant")
    st.success("📊 Budget Analysis")
    st.success("🎯 Goal Planning")
    st.success("⚠ Risk Analysis")
    st.success("📄 Financial Reports")
    st.success("📚 Finance Knowledge")

    st.divider()

    st.subheader("💡 Example Questions")

    st.info("Analyze my monthly budget")

    st.info("My income is ₹60000 and expenses are ₹35000")

    st.info("Can I save ₹5 lakh in 3 years?")

    st.info("Generate my monthly financial report")

    st.info("What is SIP?")

    st.divider()

    if st.button("🗑 Clear Conversation"):

        st.session_state.messages = []

        st.session_state.income = 0
        st.session_state.expenses = 0
        st.session_state.savings = 0
        st.session_state.saving_rate = 0

        clear_memory()

        st.rerun()

# ==========================================================
# HEADER
# ==========================================================

st.title("💰 AI Personal Finance Coach")

st.caption(
    "Budget Planning • Goal Tracking • Financial Health • Risk Analysis • Knowledge Assistant"
)

st.divider()

# ==========================================================
# HELPER FUNCTIONS
# ==========================================================

import re

def get_number(pattern, text):

    match = re.search(pattern, text, re.IGNORECASE)

    if not match:
        return None

    value = match.group(1)

    # Remove commas, currency symbol and spaces
    value = (
        value.replace(",", "")
             .replace("₹", "")
             .strip()
    )

    try:
        return float(value)
    except:
        return None


def extract_financial_values(response):

    data = {}

    income = get_number(
        r"Monthly Income\s*:?\s*₹?\s*([\d,]+(?:\.\d+)?)",
        response
    )

    expense = get_number(
        r"Monthly Expenses\s*:?\s*₹?\s*([\d,]+(?:\.\d+)?)",
        response
    )

    saving = get_number(
        r"Monthly Savings\s*:?\s*₹?\s*([\d,]+(?:\.\d+)?)",
        response
    )

    rate = get_number(
        r"Saving Rate\s*:?\s*([\d.]+)",
        response
    )

    if income is not None:
        data["monthly_income"] = income

    if expense is not None:
        data["monthly_expenses"] = expense

    if saving is not None:
        data["monthly_savings"] = saving

    if rate is not None:
        data["saving_rate"] = rate

    return data


def extract_health_score(text):

    match = re.search(
        r"Health Score.*?(\d+)",
        text,
        re.IGNORECASE
    )

    if match:
        return int(match.group(1))

    return None


def is_report(text):

    keywords = [
        "Monthly Income",
        "Monthly Expenses",
        "Monthly Savings",
        "Saving Rate",
        "Recommendations"
    ]

    count = 0

    for word in keywords:

        if word.lower() in text.lower():
            count += 1

    return count >= 3


def show_bar_chart(data):

    fig = go.Figure()

    fig.add_bar(
        x=["Income","Expenses","Savings"],
        y=[
            data["income"],
            data["expenses"],
            data["savings"]
        ]
    )

    fig.update_layout(
        title="Monthly Financial Summary",
        height=340
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


def show_pie_chart(data):

    fig = go.Figure()

    fig.add_pie(
        labels=["Expenses","Savings"],
        values=[
            data["expenses"],
            data["savings"]
        ],
        hole=0.45
    )

    fig.update_layout(height=340)

    st.plotly_chart(
        fig,
        use_container_width=True
    )


def show_health(score):

    st.progress(score/100)

    if score >= 80:
        st.success(f"Excellent ({score}/100)")
    elif score >= 60:
        st.info(f"Good ({score}/100)")
    elif score >= 40:
        st.warning(f"Average ({score}/100)")
    else:
        st.error(f"Needs Improvement ({score}/100)")


def show_report(text):

    st.markdown("### 📄 Monthly Financial Report")

    st.markdown(
        f"""
<div class="report-card">
{text.replace(chr(10),"<br>")}
</div>
""",
        unsafe_allow_html=True
    )
# ==========================================================
# DISPLAY CHAT HISTORY
# ==========================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        # --------------------------------------
        # Chat Text
        # --------------------------------------

        st.markdown(message["content"])

        # --------------------------------------
        # Financial Charts
        # --------------------------------------

        if "chart" in message:

            st.markdown("---")
            st.subheader("📊 Financial Summary")

            col1, col2 = st.columns(2)

            with col1:
                show_bar_chart(message["chart"])

            with col2:
                show_pie_chart(message["chart"])

        # --------------------------------------
        # Financial Health
        # --------------------------------------

        if "health" in message:

            st.markdown("---")
            st.subheader("📈 Financial Health")

            show_health(message["health"])

        # --------------------------------------
        # Financial Report
        # --------------------------------------

        if "report" in message:

            st.markdown("---")

            show_report(message["report"])


# ==========================================================
# CHAT INPUT
# ==========================================================

prompt = st.chat_input(
    "Ask anything about your finances..."
)

# Don't execute anything until the user sends a message.
if not prompt:
    st.stop()
# ==========================================================
# USER MESSAGE
# ==========================================================

user_message = {
    "role": "user",
    "content": prompt
}

st.session_state.messages.append(user_message)

with st.chat_message("user"):
    st.markdown(prompt)

# ==========================================================
# ASSISTANT RESPONSE
# ==========================================================

with st.chat_message("assistant"):

    with st.spinner("Thinking..."):

        try:
            response = chat(prompt)

        except Exception as e:
            response = f"❌ Error:\n\n{e}"

    # Display AI response
    st.markdown(response)

    # ======================================================
    # Extract Financial Information
    # ======================================================

    financial_data = extract_financial_values(response)

    chart_data = None

    if (
        "income" in financial_data and
        "expenses" in financial_data and
        "savings" in financial_data
    ):

        chart_data = financial_data

        st.markdown("---")
        st.subheader("📊 Financial Summary")

        col1, col2 = st.columns(2)

        with col1:
            show_bar_chart(chart_data)

        with col2:
            show_pie_chart(chart_data)

    # ======================================================
    # Financial Health
    # ======================================================

    health_score = extract_health_score(response)

    if health_score is not None:

        st.markdown("---")
        st.subheader("📈 Financial Health")

        show_health(health_score)

    # ======================================================
    # Monthly Report
    # ======================================================

    report_text = None

    if is_report(response):

        report_text = response

        st.markdown("---")

        show_report(report_text)

# ==========================================================
# SAVE MESSAGE
# ==========================================================

assistant_message = {
    "role": "assistant",
    "content": response
}

if chart_data is not None:
    assistant_message["chart"] = chart_data

if health_score is not None:
    assistant_message["health"] = health_score

if report_text is not None:
    assistant_message["report"] = report_text

st.session_state.messages.append(
    assistant_message
)

# ==========================================================
# UPDATE DASHBOARD VALUES
# ==========================================================

if chart_data:

    st.session_state.income = chart_data["income"]

    st.session_state.expenses = chart_data["expenses"]

    st.session_state.savings = chart_data["savings"]

    st.session_state.saving_rate = chart_data["saving_rate"]

# Refresh UI once after storing everything
st.rerun()
# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.caption("💰 AI Personal Finance Coach")

with col2:
    st.caption("Powered by OpenRouter + Gemini")

with col3:
    st.caption("Built with ❤️ using Streamlit")

st.markdown(
    """
<div class="footer">

<b>AI Personal Finance Coach</b><br>

Budget Planning • Goal Planning • Risk Analysis • Financial Reports • Knowledge Assistant

<br><br>

© 2026 Personal Finance Coach

</div>
""",
    unsafe_allow_html=True
)