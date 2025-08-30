from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# إعداد الاتصال بالداتابيس
db = mysql.connector.connect(
    host="localhost",
    user="AH",
    password="12Secure",
    database="XDB"
)

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    if request.method == "POST":
        search = request.form.get("search")
        cursor = db.cursor(dictionary=True)
        query = "SELECT * FROM people WHERE NAME LIKE %s OR `DIAL` LIKE %s"
        cursor.execute(query, (f"%{search}%", f"%{search}%"))
        results = cursor.fetchall()
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
