
from flask import Flask, render_template, request, url_for, redirect
# from productos import Producto
# para ejecutar= python  -m flask run
app = Flask(__name__)

@app.route("/")
def homepage():
    return "Hello World. <a href='/agur'>pinchar aqui</a> para ir a agur "

# if "__name__" == "__main__":
@app.route("/agur")
def agur():
    return "<h1>AGUR</h1>"


@app.route("/lambda")
def calcularlamba():
    posneg= lambda x: "Positivo" if x>0 else "Negativo"
    return posneg(10)

@app.route("/pagina1")
def pagina1(): #no tiene nada que ver con el nombre con el nombre de html
    return app.send_static_file("pagina1.html")
  
@app.route("/pagina2")
def pagina2(): #no tiene nada que ver con el nombre con el nombre de html
    return app.send_static_file("pagina2.html")

# @app.route("/dinamica1")
# def dinamica1(): #no tiene nada que ver con el nombre con el nombre de html
#     nombre= "mansle"
#     edad= 20
#     frutas=["coco", "zapato", "recola", "pomelo", "remolacha","ALFOMBRA"]
#     return render_template("pagina1.html", nombre=nombre, edad=edad)
# @app.route("/productos")
# def dinamica1(): #no tiene nada que ver con el nombre con el nombre de html
#     p1= Producto(1, "Raqueta", 5.99, "/images/tree.jpg")
#     p2= Producto(2, "Balon", 9.99, "")
#     p3= Producto(3, "Lavadora", 19.99, "")

#     listaProductos = [p1, p2, p3]

#     return render_template("pagina2.html",listaProductos=listaProductos)

@app.route("/dashboard/<string:username>")
def dashboard(username):
    return f"ya estas dentro {username}"

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method=="GET":
        return render_template("login.html")
    else: #POST
        username =request.form["username"]
        password =request.form["password"]

    if username == "eze" and password=="pass":
        return redirect("/dashboard")
    else:
        return "Payaso. contraseña o usuario"
    



if "__name__"== "__main__":
    app.run(debug=True)

    
