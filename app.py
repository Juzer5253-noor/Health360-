from flask import Flask, render_template
import os

app = Flask(__name__)

# Updated with your specific Tableau Public URLs (converted to embed format)
TABLEAU_DASHBOARD_URL = "https://public.tableau.com/views/Health360_17931255272280/HealthCareDashboard"
TABLEAU_STORY_URL = "https://public.tableau.com/views/Health360_17931255272280/Story1"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', viz_url=TABLEAU_DASHBOARD_URL)

@app.route('/story')
def story():
    return render_template('story.html', viz_url=TABLEAU_STORY_URL)

if __name__ == '__main__':
    # Render assigns the PORT environment variable
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
