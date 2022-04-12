
from flask import Flask, request

app = Flask(__name__) # contsructor it is very important 


@app.route("/hello", methods = ["GET","POST"]
)
def hello():
    username = request.args.get("UserName")
    return f"welcome {username}"

# Calling the constructor
if __name__ == "__main__":
    app.run(host = "0.0.0.0",port = 8080, debug = True)