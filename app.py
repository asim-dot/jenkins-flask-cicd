from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title='Jenkins CI/CD Demo')

@app.route('/api/status')
def status():
    return {"status": "OK", "message": "Service is running"}

@app.route('/about')
def about():
    return render_template('about.html', title='About This App')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)