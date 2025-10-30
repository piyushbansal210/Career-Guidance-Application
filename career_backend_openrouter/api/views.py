import requests
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response

# ==============================
# 🤖 AI Chat via OpenRouter (ChatGPT-5)
# ==============================
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
OPENROUTER_API_KEY = getattr(settings, "OPENROUTER_API_KEY", None)
OPENROUTER_MODEL = getattr(settings, "OPENROUTER_MODEL", "openai/gpt-5")

CHAT_HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json",
}

@api_view(["POST"])
def career_chat(request):
    """POST /api/ai/chat/  Body: {"query":"..."} -> AI reply"""
    user_input = request.data.get("query", "")
    if not user_input:
        return Response({"error": "query is required"}, status=400)

    payload = {
        "model": OPENROUTER_MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful AI career advisor for Australia. Be concise and practical."},
            {"role": "user", "content": user_input},
        ],
    }

    try:
        r = requests.post(OPENROUTER_URL, headers=CHAT_HEADERS, json=payload, timeout=45)
        data = r.json()
        reply = (
            (data.get("choices") or [{}])[0]
            .get("message", {})
            .get("content", "No valid response received.")
        )
        return Response({"response": reply}, status=200)
    except Exception as e:
        return Response({"error": str(e)}, status=500)


# ==============================
# 📰 Career/Technology News via GNews (with your key)
# ==============================
@api_view(["GET"])
def get_latest_news(request):
    url = (
        "https://newsapi.org/v2/top-headlines?"
        "sources=abc-news-au&"
        f"apiKey={settings.NEWS_API_KEY}"
    )
    try:
        res = requests.get(url, timeout=20)
        data = res.json()
        articles = [
            {
                "title": a.get("title"),
                "description": a.get("description"),
                "url": a.get("url"),
                "source": (a.get("source") or {}).get("name"),
            }
            for a in (data.get("articles") or [])
        ]
        return Response({"news": articles}, status=200)
    except Exception as e:
        return Response({"error": str(e)}, status=500)
