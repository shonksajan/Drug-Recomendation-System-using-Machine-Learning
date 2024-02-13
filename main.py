from flask import Flask,request,render_template


app = Flask(__name__)


# python main
if __name__=="main__":
    app.run(debug=True)