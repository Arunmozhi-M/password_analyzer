from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    strength = ""

    if request.method == "POST":
        password = request.form["password"]
        print("password:", password)  # Debugging line
        score = 0

        if len(password) >= 8:
            score += 1
        if re.search(r"[A-Z]", password):
            score += 1
        if re.search(r"[a-z]", password):
            score += 1
        if re.search(r"[0-9]", password):
            score += 1
        if re.search(r"[^A-Za-z0-9]", password):
            score += 1

        if score <= 2:
            strength = "Weak"
        elif score <= 4:
            strength = "Medium"
        else:
            strength = "Strong"

    return render_template("index.html", strength=strength)

if __name__ == "__main__":
    app.run(debug=True)