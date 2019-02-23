from flask import Flask

app = Flask(__name__)
@app.route("/")
def index():
    return "hey!!.."
@app.route("/home")
def home():
    return"my home page"
@app.route("/contact")
def contact():
    return"my contact"
if(__name__=="__main__"):
    app.run()


