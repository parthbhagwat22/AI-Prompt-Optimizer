import streamlit as st
from utils import generate_optimized_prompt

st.set_page_config(page_title="AI Prompt Optimizer", layout="centered")

st.title("📝 AI Prompt Optimizer")
st.markdown(
    """
    **Developed by:** Parth Bhagwat
    This tool helps you turn your idea into a polished, effective AI prompt.
    """
)

# User input
user_input = st.text_area(
    "Enter your idea or request for the AI:",
    height=150,
    placeholder="Example: Write a bedtime story about a space-traveling cat..."
)

# Generate button
if st.button("Generate Optimized Prompt"):
    with st.spinner("Optimizing your prompt..."):
        optimized_prompt = generate_optimized_prompt(user_input)
    st.subheader("AI-Optimized Prompt")
    st.write(optimized_prompt)
else:
    st.info("Enter your request above and click the button to generate a prompt.")
