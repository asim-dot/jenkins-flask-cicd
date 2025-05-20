from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

# HTML template with some basic styling
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Flask on Vercel</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background-color: #f5f5f5;
        }
        .container {
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            padding: 2rem;
            max-width: 800px;
            text-align: center;
        }
        h1 {
            color: #3498db;
        }
        .info {
            margin: 1.5rem 0;
            padding: 1rem;
            background-color: #f1f9ff;
            border-radius: 4px;
        }
        .time {
            font-weight: bold;
            color: #2c3e50;
        }
        .footer {
            margin-top: 2rem;
            font-size: 0.9rem;
            color: #7f8c8d;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Hello from Flask on Vercel! 🚀</h1>
        <div class="info">
            <p>This Flask application is running as a serverless function.</p>
            <p>Current server time: <span class="time">{{ current_time }}</span></p>
        </div>
        <p>Your request path: <code>{{ path }}</code></p>
        <div class="footer">
            <p>Deployed with ❤️ using Vercel and Git</p>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    # Pass the current time to the template
    return render_template_string(
        HTML_TEMPLATE, 
        current_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        path="/"
    )

@app.route('/<path:path>')
def catch_all(path):
    # Reuse the same template but with the requested path
    return render_template_string(
        HTML_TEMPLATE, 
        current_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        path=path
    )

# For local development
if __name__ == '__main__':
    app.run(debug=True)