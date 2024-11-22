from flask import Flask

app = Flask(__name__)
@app.route("/")

def myfunc():
    return("Hello, my first flask server")

if __name__=='__main__':
    app.run()
