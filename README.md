# 🔗 URL Shortener

> Project 16 of my Python/Flask portfolio — a web app that shortens long URLs into clean, shareable links.

## Features
- Paste any valid URL and get a short link instantly
- Redirects correctly when the short link is visited
- Detects duplicate URLs and reuses existing short codes
- Clean dark-themed UI with one-click copy to clipboard

## Tech Stack
- **Backend:** Python, Flask
- **Frontend:** HTML, CSS (no frameworks)
- **Storage:** In-memory dictionary (no database needed)

## How to Run

```bash
# 1. Install dependencies
pip install flask

# 2. Run the app
python app.py

# 3. Open in browser
http://127.0.0.1:5000
```

## How It Works
1. User pastes a URL into the form
2. Flask generates a random 6-character code
3. The code maps to the original URL in memory
4. Visiting `localhost:5000/<code>` redirects to the original URL


