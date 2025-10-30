# Career Backend (Django + DRF)

Two endpoints:
- **POST** `/api/ai/chat/` → `{ "query": "Your question here" }` (uses OpenRouter ChatGPT‑5)
- **GET**  `/api/news/latest/?q=career%20OR%20technology&n=10&country=au` (uses your GNews key)

## Setup
```bash
cd career_backend_openrouter
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python3 manage.py runserver
```

## .env (edit this)
```
OPENROUTER_API_KEY=your_openrouter_key_here
OPENROUTER_MODEL=openai/gpt-5
NEWS_API_KEY=your_gnews_api_key_here
SECRET_KEY=django-insecure-change-this
```

## Notes
- Swap `OPENROUTER_MODEL` to any OpenRouter-supported model if needed.
- News endpoint defaults to **Australia** and topic **career OR technology**; override via query params.
