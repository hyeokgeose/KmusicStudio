from flask import *

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/search")
def search():
  pass
if __name__ == "__main__":
  app.run(port=5000, debug=True)