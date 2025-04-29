from flask import Flask, request, render_template_string
import psycopg2
import os

app = Flask(__name__)

# Read connection string from environment variable
connection_string = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']

# Connect to PostgreSQL
conn = psycopg2.connect(connection_string)
cursor = conn.cursor()

# Create 'users' table if it does not exist
create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    number VARCHAR(20)
);
"""
cursor.execute(create_table_query)
conn.commit()

# HTML Form Template
form_template = """
<!doctype html>
<title>PostgreSQL Form</title>
<h2>Enter User Details</h2>
<form method=post>
  Name: <input type=text name=name><br><br>
  Email: <input type=email name=email><br><br>
  Number: <input type=text name=number><br><br>
  <input type=submit value=Submit>
</form>
{% if message %}
  <p><strong>{{ message }}</strong></p>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        number = request.form["number"]
        sql = "INSERT INTO users (name, email, number) VALUES (%s, %s, %s)"
        cursor.execute(sql, (name, email, number))
        conn.commit()
        message = "Data inserted successfully!"
    return render_template_string(form_template, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
