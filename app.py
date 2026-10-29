from flask import Flask, render_template

app = Flask(__name__)

# Fixed Embed URLs for Tableau Public
DASHBOARD_URL = "https://public.tableau.com/views/Health360_17931255272280/HealthCareDashboard?:embed=y&:showVizHome=n&:jsdebug=n"
STORY_URL = "https://public.tableau.com/views/Health360_17931255272280/Story1?:embed=y&:showVizHome=n&:jsdebug=n"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", tableau_url=DASHBOARD_URL)

@app.route("/story")
def story():
    return render_template("story.html", tableau_url=STORY_URL)

if __name__ == "__main__":
    app.run(debug=True)
