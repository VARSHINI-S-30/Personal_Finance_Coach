import streamlit as st


def render_sidebar():

    with st.sidebar:

        st.title("💰 Personal Finance Coach")

        st.markdown("---")

        st.markdown("### 🤖 AI Features")

        st.markdown("""
✅ Budget Planning

✅ Goal Planning

✅ Financial Risk Analysis

✅ Financial Knowledge Assistant

✅ Monthly Report Generator

✅ PDF Report Download

✅ Conversation Memory

✅ Automatic Tool Calling
""")

        st.markdown("---")

        st.markdown("### 📊 Supported Questions")

        st.info("""
• Create my monthly budget

• Analyze my spending

• Can I buy a laptop?

• Financial health score

• Explain SIP

• Generate monthly report

• Generate PDF report
""")

        st.markdown("---")

        st.caption("Powered by OpenRouter + Streamlit")