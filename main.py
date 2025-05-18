from fastapi import FastAPI
from pydantic import BaseModel
from gmail_utils import fetch_emails_from_query
from gemini_agent import build_gmail_search_query, summarize_emails_with_query

app = FastAPI()

class UserQuery(BaseModel):
    query: str

@app.post("/chat_with_gmail")
def chat_with_gmail(user_input: UserQuery):
    gmail_query = build_gmail_search_query(user_input.query)
    snippets = fetch_emails_from_query(gmail_query)
    result = summarize_emails_with_query(user_input.query, snippets)
    return {"answer": result}
