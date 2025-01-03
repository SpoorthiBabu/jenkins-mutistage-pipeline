from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    conn = sqlite3.connect('database.db')
    conn.execute('CREATE TABLE IF NOT EXISTS visits (count INT)')
    conn.execute('INSERT INTO visits (count) VALUES (1)')
    conn.commit()
    conn.close()
    return "Connected to the database!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
