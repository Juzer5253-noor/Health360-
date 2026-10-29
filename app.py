from flask import Flask, render_template

app = Flask(__name__)

# Corrected Tableau Embed URLs from your provided links
DASHBOARD_URL = "https://public.tableau.com/views/Health360_17931255272280/HealthCareDashboard?:embed=y&:showVizHome=n&:apiJS=true"
STORY_URL = "https://public.tableau.com/views/Health360_17931255272280/Story1?:embed=y&:showVizHome=n&:apiJS=true"

@app.route("/")
def index():
    """Renders the Home page with project overview and key statistics."""
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    """Renders the Analytics Dashboard page embedding the Tableau Dashboard."""
    return render_template("dashboard.html", tableau_url=DASHBOARD_URL)

@app.route("/story")
def story():
    """Renders the Patient Risk Story page embedding the Tableau Story."""
    return render_template("story.html", tableau_url=STORY_URL)

if __name__ == "__main__":
    app.run(debug=True)
