from flask import Flask, render_template, request, redirect, url_for
import string
import random

app = Flask(__name__)

# In-memory storage (dictionary)
url_map = {}

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

@app.route('/', methods=['GET', 'POST'])
def index():
    short_url = None
    error = None

    if request.method == 'POST':
        original_url = request.form.get('url', '').strip()

        if not original_url:
            error = "Please enter a URL."
        elif not original_url.startswith(('http://', 'https://')):
            error = "URL must start with http:// or https://"
        else:
            # Check if URL already shortened
            for code, url in url_map.items():
                if url == original_url:
                    short_url = request.host_url + code
                    return render_template('index.html', short_url=short_url)

            # Generate new short code
            code = generate_short_code()
            while code in url_map:
                code = generate_short_code()

            url_map[code] = original_url
            short_url = request.host_url + code

    return render_template('index.html', short_url=short_url, error=error)

@app.route('/<code>')
def redirect_url(code):
    original_url = url_map.get(code)
    if original_url:
        return redirect(original_url)
    return render_template('index.html', error="Short URL not found or has expired.")

if __name__ == '__main__':
    app.run(debug=True)