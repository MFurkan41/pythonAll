from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:/PythonFiles/Çalışmalarım/KantinAppFlask/products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.secret_key= "kantinapp"

class Product(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(50))
   price = db.Column(db.Integer)
   year = db.Column(db.Integer)
   month = db.Column(db.String(10))


@app.route('/')
def index():
   return render_template("index.html")

@app.route('/solds')
def solds():
   years = [2018,2019,2020,2021]
   return render_template("solds.html",years=years)

@app.route('/solds/<string:year>')
def solds_year(year):
   aylar = ["Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık"]
   month = "Ay"
   request1 = (request.path)
   years = [2018,2019,2020,2021]
   return render_template("solds.html",aylar=aylar,request1=request1,month=month,years=years)

@app.route('/solds/<string:year>/<string:month>')
def solds_month(year,month):
   return ("Yılın : {}, Ayın: {}".format(year,month))

@app.route('/products')
def products():
   products = Product.query.all()
   return render_template("products.html",products=products)
@app.route('/products/addproduct',methods = ["GET","POST"])
def addproduct():
   if request.method == "POST":
      name = request.form.get("name")
      price  = request.form.get("price")

      newProduct = Product(name = name, price = price)
      db.session.add(newProduct)
      db.session.commit()
      return redirect(url_for("products"))
   else:
      return render_template("addproduct.html")

@app.route('/products/deleteproduct/<string:id>')
def deleteproduct(id):
   dProduct = Product.query.filter_by(id=id).first()
   db.session.delete(dProduct)
   db.session.commit()
   return redirect(url_for("products"))
if __name__ == '__main__':
   db.create_all()
   app.run(debug=True)