from flask import Flask

app = Flask(__name__)

# When the url "/" is accessed, then return the string.
@app.route("/")
def greeting():
    return "<p>My first Flask project!</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug = True)
