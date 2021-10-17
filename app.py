from flask import Flask
import os
import socket

app = Flask(__name__)

inc = 0
@app.route("/")
def index():
    html = "{inc}"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())
@app.route("/stat")
def stat()
    inc = inc + 1;
    html = "{inc}"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())
@app.route("/about")
def about():
    html = "<h3>Hello, Khudoyshukur</h3>"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
