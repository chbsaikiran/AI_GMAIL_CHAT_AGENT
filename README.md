# Gmail Chat Agent

A FastAPI-based application that allows you to query your Gmail inbox using natural language.

## Setup

1. Create and activate virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Unix/MacOS
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
- Create a `.env` file in the root directory
- Add your Google API key:
```
GOOGLE_API_KEY=your_api_key_here
```

4. Run the application:
```bash
uvicorn main:app --reload
```

## Example Usage

```bash
curl -X POST "http://localhost:8000/chat_with_gmail" \
-H "Content-Type: application/json" \
-d "{\"query\": \"How much did I spend on Amazon this month?\"}"
```

## Example Output
```json
{
  "answer": "You spent approximately ₹2,850 on Amazon in May 2025 across 3 orders."
}
```

