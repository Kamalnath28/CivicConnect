from flask import Flask, render_template, request
import os
import psycopg
from dotenv import load_dotenv

# Load values from .env
load_dotenv()

app = Flask(__name__)


def get_db_connection():
    connection = psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    return connection


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/report", methods=["GET", "POST"])
def report():

    if request.method == "POST":

        category = request.form["category"]
        location = request.form["location"]
        description = request.form["description"]

        connection = get_db_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO complaints (category, location, description)
            VALUES (%s, %s, %s)
            """,
            (category, location, description)
        )

        connection.commit()

        cursor.close()
        connection.close()

        print("Complaint saved successfully!")

    return render_template("report.html")


if __name__ == "__main__":
    app.run(debug=True)