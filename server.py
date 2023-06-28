from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template("index.html")


@app.route('/about')
def about_page():
    return render_template("about.html")


@app.route('/projects')
def projects_page():
    return render_template("projects.html")


@app.route('/certificate')
def cert_page():
    return render_template("cert.html")

if __name__ == "__main__":
    app.run(debug=True)
