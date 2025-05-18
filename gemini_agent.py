import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access your API key and initialize Gemini client correctly
api_key = os.getenv("GEMINI_API_KEY")
#client = genai.Client(api_key=api_key)
genai.configure(api_key=api_key)

def build_gmail_search_query(natural_question: str) -> str:
    model = genai.GenerativeModel("gemini-2.0-flash")
    system_prompt = f"""
You are an AI expert at writing Gmail search queries.
Convert the following user question into a Gmail search query syntax.
Only output the Gmail query string. Do not explain anything.

IMPORTANT RULES:
1. For "this month" queries in May 2025, ALWAYS use exactly:
   after:2025/05/01 before:2025/05/31
2. Include the ENTIRE day in date ranges
3. Never skip any days in the range

Examples:
"Swiggy orders this month" -> "Swiggy after:2025/05/01 before:2025/05/31"
"IRCTC last week" -> "IRCTC after:2025/05/10 before:2025/05/17"
"OTP from SBI yesterday" -> "OTP SBI after:2025/05/17 before:2025/05/18"

User Query:
{natural_question}
"""
    response = model.generate_content(system_prompt)
    return response.text.strip().strip('"')

def summarize_emails_with_query(user_query: str, snippets: list[str]) -> str:
    model = genai.GenerativeModel("gemini-2.0-flash")
    combined_emails = "\n\n".join(snippets[:50])  # Increased to match max_results
    final_prompt = f"""
You are an assistant who summarizes Gmail content and answers user queries.
When analyzing expenses or orders:
1. Include ALL transactions from the entire date range
2. Pay special attention to dates at the start of the month
3. List each transaction with its date
4. Calculate the total amount accurately

EMAIL SNIPPETS:
{combined_emails}

USER QUESTION:
{user_query}

TASK: Answer the question based on ALL emails in the snippets. For expenses/orders:
1. List each transaction with its date
2. Show the total amount
3. Mention if you find orders from early May 2025 (1st-3rd)
"""
    response = model.generate_content(final_prompt)
    return response.text
