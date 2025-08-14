import cohere
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Cohere client
co = cohere.Client(os.getenv("COHERE_API_KEY"))

def generate_optimized_prompt(user_input: str) -> str:
    """
    Takes raw user input and generates an AI-optimized prompt.
    """
    if not user_input.strip():
        return "⚠️ Please provide some input."

    prompt = (
        "You are a professional prompt engineer. "
        "Convert the following user request into a perfect, detailed prompt for any AI model:\n\n"
        f"User input: {user_input}\n\nGenerated Prompt:"
    )

    try:
        response = co.generate(
            model="command-r-plus",
            prompt=prompt,
            max_tokens=200,
            temperature=0.7
        )
        return response.generations[0].text.strip()
    except Exception as e:
        return f"⚠️ Error: {str(e)}"
