from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy
from graph import build_graph
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/furkan/Desktop/asd/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.secret_key= "graphcreator"

# Grafik Database
class Graph(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    graph_name= db.Column(db.String(80), unique=True, nullable=False)
    x_name = db.Column(db.String(40), unique=True, nullable=False)
    y_name = db.Column(db.String(40), unique=True, nullable=False)
    x_column = db.Column(db.String(120), unique=True, nullable=False)
    y_column = db.Column(db.String(120), unique=True, nullable=False)



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/create_graph', methods = ["POST","GET"])
def create_graph():
    if request.method == "POST":
        print("")
    elif request.method == "GET":
        numbers = list()
        for i in range(1,100):
            numbers.append(i)
        return render_template("c_graph.html",numbers=numbers)
@app.route('/graphs')
def graphs():
    #These coordinates could be stored in DB
    x1 = [0, 1, 2, 3, 4]
    y1 = [10, 30, 80, 5, 50]
    x2 = [0, 1, 2, 3, 4]
    y2 = [50, 30, 20, 10, 50]
    x3 = [0, 1, 2, 3, 4]
    y3 = [0, 30, 10, 5, 30]
    
    graph1_url = build_graph(x1,y1)
    graph2_url = build_graph(x2,y2)
    graph3_url = build_graph(x3,y3)
 
    return render_template('graphs.html', graph1=graph1_url, graph2=graph2_url, graph3=graph3_url)
 
if __name__ == '__main__':
    app.debug = True
    db.create_all()
    app.run()