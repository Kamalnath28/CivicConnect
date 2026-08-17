from flask import Flask,render_template,request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/report", methods=["GET", "POST"])
def report():

    if request.method == "POST":

        category = request.form["category"]
        location = request.form["location"]
        description = request.form["description"]

        print("Category:", category)
        print("Location:", location)
        print("Description:", description)

    return render_template("report.html")


if __name__ == "__main__":
    app.run(debug=True)