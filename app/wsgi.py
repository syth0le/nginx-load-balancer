from flask import Flask
import socket

app = Flask(__name__)


@app.route("/")
def root():
    return {"message": f"Hello, this is container: {socket.gethostname()}"}


if __name__ == "__main__":
    app.run(debug=True)
